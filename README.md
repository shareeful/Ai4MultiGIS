# Chelmsford SuDS Dataset (AI4MultiGIS Pilot 1)

Geospatial dataset supporting flood risk and Sustainable Drainage System (SuDS) analysis for Chelmsford, Essex, UK. Produced as part of the AI4MultiGIS project (UKRI CHIST-ERA, grant EP/Z003490/1), Anglia Ruskin University.

## Overview

| Property | Value |
|---|---|
| Study area | 342 km², Chelmsford, Essex, UK |
| Coordinate reference system | EPSG:32630 |
| Labelled pixels | 12,847 at 10 m resolution |
| Fused modalities | 35 |
| Class distribution | Severe imbalance; High Risk class is 0.44% of labelled pixels |

## Repository structure

```
data/
├── vector/
│   ├── V1_os_open_rivers.shp
│   ├── V2_road_network.shp
│   ├── V3_ea_rivers_sea_flood_risk.shp
│   ├── V4_ea_surface_water_risk.shp
│   ├── V5_ea_surface_water_cc1.shp
│   └── chelmsford_buildings.geojson
├── raster/
│   ├── R1_dem_dtm_lidar.tif
│   ├── R2_landuse_ukceh_lcm.tif
│   └── R3_sentinel2_composite/
│       ├── allbands.tif
│       ├── rgb.tif
│       ├── ndvi.tif
│       ├── ndwi.tif
│       └── ndbi.tif
├── metadata/
│   └── M1_sentinel2_metadata.json
└── labels/
    └── labelled_pixels.geojson
```

## Layer descriptions

### Vector layers

| ID | Layer | Source | Format | Year | CRS |
|---|---|---|---|---|---|
| V1 | OS Open Rivers | Ordnance Survey | Shapefile | 2024 | EPSG:32630 |
| V2 | Road Network | Ordnance Survey | Shapefile | 2024 | EPSG:32630 |
| V3 | Rivers and Sea Flood Risk | Environment Agency | Shapefile | 2024 | EPSG:32630 |
| V4 | Surface Water Flood Risk | Environment Agency | Shapefile | 2024 | EPSG:32630 |
| V5 | Surface Water Flood Risk, CC1 scenario | Environment Agency | Shapefile | 2024 | EPSG:32630 |
| — | Building footprints (57,975 polygons) | Microsoft GlobalML | GeoJSON | — | EPSG:4326 |

The building footprints layer is supplied in EPSG:4326 and requires reprojection to EPSG:32630 before use with the other layers. Attributes include `centroid_lat`, `centroid_lon`, `height_m`, `confidence`, and `num_vertices`.

### Raster layers

| ID | Layer | Source | Format | Date | CRS |
|---|---|---|---|---|---|
| R1 | DEM/DTM, 1 m LiDAR | Environment Agency | GeoTIFF | 2022 | EPSG:32630 |
| R2 | Land use | UKCEH Land Cover Map | GeoTIFF | 2022 | EPSG:32630 |
| R3 | Sentinel-2 median composite (ALLBANDS, RGB, NDVI, NDWI, NDBI) | Google Earth Engine | GeoTIFF | Oct 2024 – May 2025 | EPSG:32630 |

### Supporting files

| ID | File | Description | Status |
|---|---|---|---|
| M1 | Sentinel-2 metadata | Acquisition metadata for the composite | Included |
| P1 | Soil Type, NATMAP | National soil classification | Pending |

## Data preparation

All vector and raster layers are resampled to a common 10 m grid in EPSG:32630 and fused into a 35-band modality stack. Labels are assigned at 12,847 pixel locations, with the High Risk class making up 0.44% of labels.

## Citation

## License

## Contact

Hassan, Research Assistant, AI4MultiGIS Project, Anglia Ruskin University.
