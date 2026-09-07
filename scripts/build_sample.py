#!/usr/bin/env python3
"""
Build a GitHub-ready sample of the Chelmsford SuDS Pilot 1 dataset.

Clips every raster and vector layer to one shared square box in the centre of
the study area, merges the vectors into a single GeoPackage, compresses the
raster, and shrinks the box until the whole sample fits inside the size budget.
"""
import json
import os
import shutil
import sqlite3
import tempfile
import zipfile
from pathlib import Path

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.windows import from_bounds
from shapely.geometry import box

# Root of the raw delivered dataset. Override with SUDS_RAW_DIR.
RAW = Path(os.environ.get("SUDS_RAW_DIR", "/Users/muhammadhassan/Downloads/Dataset"))
VECTOR_ZIP = RAW / "Dataset/Dataset validation/Chelmsford_SuDS_Dataset.zip"
RASTER_SRC = RAW / "Dataset/Dataset validation/experiment 3/exp3_suds_opportunity.tif"
OUT = Path(__file__).resolve().parent.parent

BUDGET_BYTES = 45_000_000     # "under 45 MB"
START_SIDE = 1600.0           # metres; square box side length
SHRINK_STEP = 100.0           # metres to trim off the side each round
MIN_SIDE = 200.0

GPKG_NAME = "suds_substudy_sample.gpkg"
TIF_NAME = "suds_opportunity.tif"

# Class legend and colours, from experiment_3_suds_constraint_map.py
# (CLASS_LABELS / CLASS_COLOURS). Embedded as a GeoTIFF colour table so the
# raster renders as a thematic map everywhere instead of a near-black image —
# values 0-4 on a 0-255 grey ramp are all within the darkest 2% of the range.
PALETTE = {
    0: ((255, 255, 255, 255), "Outside study area"),
    1: ((215, 25, 28, 255), "Constrained"),
    2: ((255, 255, 191, 255), "Low Opportunity"),
    3: ((166, 217, 106, 255), "Medium Opportunity"),
    4: ((26, 150, 65, 255), "High Opportunity"),
}


def vector_src():
    """Unpack the Chelmsford archive to a temp dir (once) and return its root."""
    global _VECTOR_SRC
    if _VECTOR_SRC is None:
        dest = Path(tempfile.gettempdir()) / "chelmsford_suds_src"
        if not (dest / "Chelmsford_SuDS_Dataset/01_Boundary/study_boundary.shp").exists():
            dest.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(VECTOR_ZIP) as z:
                z.extractall(dest)
        _VECTOR_SRC = dest / "Chelmsford_SuDS_Dataset"
    return _VECTOR_SRC


_VECTOR_SRC = None


def study_centre():
    """Centre of the study boundary's bounding box, and the full extent."""
    b = gpd.read_file(vector_src() / "01_Boundary/study_boundary.shp")
    minx, miny, maxx, maxy = b.total_bounds
    return ((minx + maxx) / 2.0, (miny + maxy) / 2.0), b.total_bounds, b.crs


def vector_layers():
    """Source shapefiles as (layer_name, path), ordered by the numbered folders."""
    return [(p.stem, p) for p in sorted(vector_src().glob("*/*.shp"))]


# GeoPackage reserves "fid" for its primary key, so a source attribute of that
# name has to be carried across under a different one.
FID_RENAME = "src_fid"

# shapely dimension per geometry type, used to drop stray lower-dimension
# fragments that gpd.clip can leave behind at the cut edge
_DIM = {"Point": 0, "MultiPoint": 0, "LineString": 1, "MultiLineString": 1,
        "LinearRing": 1, "Polygon": 2, "MultiPolygon": 2}


def _tidy(clipped, src):
    """Drop empties and keep only geometries of the source layer's dimension."""
    clipped = clipped[~clipped.geometry.is_empty & clipped.geometry.notna()]
    if clipped.empty:
        return clipped
    want = max(_DIM.get(t, 2) for t in src.geom_type.dropna().unique())
    if (clipped.geom_type == "GeometryCollection").any():
        clipped = clipped.explode(index_parts=False)
        clipped = clipped[~clipped.geometry.is_empty & clipped.geometry.notna()]
    return clipped[clipped.geom_type.map(lambda t: _DIM.get(t, -1)) == want]


def clip_vectors(clip_geom, crs, gpkg_path):
    """Clip each shapefile to the box and write it as a layer in one GeoPackage."""
    clip_gdf = gpd.GeoDataFrame(geometry=[clip_geom], crs=crs)
    report = []
    for name, path in vector_layers():
        src = gpd.read_file(path)
        if src.crs != crs:
            src = src.to_crs(crs)
        renamed = [c for c in src.columns if c.lower() == "fid"]
        if renamed:
            src = src.rename(columns={c: FID_RENAME for c in renamed})
        clipped = _tidy(gpd.clip(src, clip_gdf), src)
        n_out = len(clipped)
        if n_out:
            clipped.to_file(gpkg_path, layer=name, driver="GPKG")
        report.append({
            "layer": name,
            "geom_type": sorted(clipped.geom_type.unique()) if n_out else [],
            "fields": [c for c in clipped.columns if c != "geometry"],
            "features_in": len(src),
            "features_out": n_out,
            "renamed_fid": bool(renamed),
        })
    # the clip box itself, so the sample documents its own extent
    clip_gdf.assign(name="sample_clip_box").to_file(
        gpkg_path, layer="clip_box", driver="GPKG"
    )
    # 18 sequential layer writes leave slack pages behind
    con = sqlite3.connect(gpkg_path)
    con.execute("VACUUM")
    con.close()
    return report


def clip_raster(bounds, tif_path):
    """Clip, downcast the 5-class map to uint8, and DEFLATE-compress it."""
    with rasterio.open(RASTER_SRC) as src:
        win = from_bounds(*bounds, transform=src.transform).round_offsets().round_lengths()
        data = src.read(1, window=win)
        transform = src.window_transform(win)
        src_crs = src.crs

        nodata_mask = ~np.isfinite(data)
        out = np.where(nodata_mask, 255, data).astype("uint8")

        profile = {
            "driver": "GTiff",
            "height": out.shape[0],
            "width": out.shape[1],
            "count": 1,
            "dtype": "uint8",
            "nodata": 255,
            "crs": src_crs,
            "transform": transform,
            "compress": "deflate",
            "predictor": 2,
            "zlevel": 9,
            "tiled": True,
            "blockxsize": 256,
            "blockysize": 256,
        }
    with rasterio.open(tif_path, "w", **profile) as dst:
        dst.write(out, 1)

        colormap = {v: rgba for v, (rgba, _) in PALETTE.items()}
        colormap[255] = (0, 0, 0, 0)          # nodata -> transparent
        dst.write_colormap(1, colormap)
        dst.set_band_description(1, "SuDS opportunity class")

        tags = {
            "source": RASTER_SRC.name,
            "classes": "0-4 SuDS opportunity classes; 255 = nodata",
            "note": "downcast from float32 to uint8 (values were integral 0-4)",
            "legend_source": "experiment_3_suds_constraint_map.py CLASS_COLOURS",
            "CLASS_255": "NoData",
        }
        tags.update({f"CLASS_{v}": label for v, (_, label) in PALETTE.items()})
        dst.update_tags(**tags)
    return {
        "width": out.shape[1],
        "height": out.shape[0],
        "nodata_cells": int(nodata_mask.sum()),
        "classes": sorted(int(v) for v in np.unique(out[~nodata_mask])),
    }


def dir_size(path):
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


def build_at(side, workdir):
    """Build the full sample at a given box side length; return manifest."""
    if workdir.exists():
        shutil.rmtree(workdir)
    (workdir / "vectors").mkdir(parents=True)
    (workdir / "raster").mkdir(parents=True)

    (cx, cy), full_extent, crs = study_centre()
    half = side / 2.0
    bounds = (cx - half, cy - half, cx + half, cy + half)
    geom = box(*bounds)

    gpkg = workdir / "vectors" / GPKG_NAME
    tif = workdir / "raster" / TIF_NAME
    vec_report = clip_vectors(geom, crs, gpkg)
    ras_report = clip_raster(bounds, tif)

    return {
        "side_m": side,
        "bounds": bounds,
        "centre": (cx, cy),
        "full_extent": [float(v) for v in full_extent],
        "crs": str(crs),
        "vectors": vec_report,
        "raster": ras_report,
        "gpkg_bytes": gpkg.stat().st_size,
        "tif_bytes": tif.stat().st_size,
        "total_bytes": dir_size(workdir),
    }


def main():
    workdir = OUT / "data"
    side = START_SIDE
    attempts = []
    while True:
        m = build_at(side, workdir)
        attempts.append({"side_m": side, "total_bytes": m["total_bytes"]})
        print(f"side={side:7.0f} m  total={m['total_bytes']/1e6:8.3f} MB")
        if m["total_bytes"] <= BUDGET_BYTES or side <= MIN_SIDE:
            break
        side -= SHRINK_STEP

    m["attempts"] = attempts
    (workdir / "manifest.json").write_text(json.dumps(m, indent=2, default=str))
    print(json.dumps({k: v for k, v in m.items() if k != "vectors"}, indent=2, default=str))
    return m


if __name__ == "__main__":
    main()
