# Chelmer Village and Beaulieu Park (CM1 6EA) — clipped sample

A small, GitHub-safe extract of the Chelmsford SuDS sub-study, provided so the
data structure can be inspected and `scripts/build_sample.py` run without the
full archive.

Full documentation — dataset overview, layer inventory, the four completed
experiments, sample extent and per-layer feature counts, licensing and citation
— is in the [repository README](../../README.md).

```
chelmer-village-cm1-6ea/
├── README.md
├── data/
│   ├── vectors/suds_substudy_sample.gpkg   17 layers + clip_box, EPSG:27700
│   ├── raster/suds_opportunity.tif         SuDS opportunity classes, 1 m
│   └── manifest.json                       exact bounds and build record
└── scripts/build_sample.py                 regenerates everything above
```

| Property | Value |
| --- | --- |
| CRS | EPSG:27700 (OSGB36 / British National Grid) |
| Bounding box | 572133.0, 209370.6, 573733.0, 210970.6 |
| Box size | 1600 m by 1600 m, 2.56 km² |

The raster is a five-class thematic map with an embedded colour table: 1
Constrained, 2 Low, 3 Medium, 4 High opportunity, 0 outside the study area.
Its values are 0 to 4, so any viewer that ignores the colour table and stretches
a byte raster over 0 to 255 will show it as near-black.

## Rebuilding

```bash
pip install geopandas rasterio
SUDS_RAW_DIR=/path/to/raw/dataset python scripts/build_sample.py
```
