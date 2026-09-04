# Chelmsford SuDS Dataset

Geospatial dataset supporting flood risk and Sustainable Drainage System (SuDS) analysis for Chelmsford, Essex, UK. Produced as part of the AI4MultiGIS project (UKRI CHIST-ERA, grant EP/Z003490/1), Anglia Ruskin University.

Project website: [https://www.ai4multigis.eu](https://www.ai4multigis.eu)

## About AI4MultiGIS

AI4MultiGIS, standing for AI Integrated Framework for Intelligent Geospatial Handling and Robust Operation in MultiGIS Applications, is a project that aims to deliver an integrated framework optimizing the processing chain of MultiGIS data, so that GIS-enabled applications and services can operate robustly. The framework spans the full MultiGIS process, from data collection through remote sensing, GPS surveys and environmental sensors, to data integration via cloud storage and spatial databases, multidimensional spatial and spectral processing with AI-based pattern recognition, visualization through interactive maps and simulations, and decision-making support for policy and strategic planning.

## Objectives of AI4MultiGIS

**Automated data collection and preprocessing**
- Develop AI-driven approaches to integrate real-time IoT data, remote sensing insights, and diverse datasets.
- Address challenges in spatial data accuracy, synchronization, and inconsistencies.
- Reduce data integration time by at least 30% and uncertainty levels by 20%.

**Real-time spatiotemporal data processing**
- Implement a federated reinforcement learning framework for processing vast multi-dimensional geospatial data.
- Optimize computing efficiency for faster decision-making and response time.

**Geostatistical AI analysis and decision support**
- Develop a cloud-integrated AI platform for multi-modal GIS data interpretation.
- Enhance predictive analytics capabilities using machine learning models.

**Responsible AI governance and policy development**
- Establish policies and best practices to ensure the fairness, transparency, and compliance of AI-enabled MultiGIS applications with the EU AI Act and other global regulations.
- Improve fairness in decision-making by at least 50%.

## SuDS pilot

This dataset supports the Chelmsford Sustainable Drainage System (SuDS) pilot, which applies the AI4MultiGIS framework to flood risk and drainage analysis for Chelmsford, Essex. It fuses vector and raster geospatial layers covering hydrology, terrain, land use, satellite imagery and building footprints into a common resampled stack, used to model and label flood risk across the study area.

## Dataset overview

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

## Focused sub-study: Chelmer Village and Beaulieu Park

A detailed sub-study covers Chelmer Village and Beaulieu Park in North Chelmsford (CM1 6EA), examining surface water flood risk and SuDS opportunity at development scale.

| Property | Value |
|---|---|
| Study area | 430 ha, CM1 6EA |
| Buildings | 1,997 |
| Road network | 47.9 km |
| Spatial layers | 19 |
| Coordinate reference system | EPSG:27700 (British National Grid) |

### Sub-study layer inventory

All 19 layers are standardised to EPSG:27700 and verified for geometry validity, spatial alignment, and attribute completeness.

| Dataset | Type | Source | Detail |
|---|---|---|---|
| Study Boundary | Polygon | CM1 6EA boundary | 430 ha polygon |
| Buildings | Polygon | Microsoft Global ML | 1,997 footprints, reprojected from WGS84 |
| Baseline Flood 0.2–1.2 m | Polygon | Environment Agency RoFSW | 5 layers, 29–32 ha core |
| CC01 Flood 0.2–1.2 m | Polygon | Environment Agency CC01 | 5 layers, 39–41 ha |
| DTM 1 m LiDAR | Raster | OS/EA LiDAR | 1 m resolution, 23.1–61.5 m AOD |
| WorldCover 2022 | Raster | ESA WorldCover | 7.6 m resolution, 7 land cover classes |
| Geology | Polygon | BGS HydrogeologyUK v5 | Single polygon, Thames Group clay |
| Soil Permeability | Polygon | BGS HydrogeologyUK v5 | Class 3 impermeable, entire site |
| Rainfall | Polygon | Chelmsford Station 2016–2025 | 580 mm/yr, monthly values |
| Roads | Line | OS OpenRoads | 595 segments, 47.9 km total |
| Tree Canopy Cover | Polygon | Forest Research 2022 | 2 wards, 8.9% weighted average |

### Completed experiments

Four experiments have been run on the sub-study data, comparing the Environment Agency baseline against the CC01 climate change scenario across five depth thresholds (0.2, 0.3, 0.6, 0.9, 1.2 m).

**Experiment 1 — Building flood exposure.** Buildings joined against all 10 flood layers and scored by risk band. At 0.2 m, buildings at risk rise from 344 (17.2%) under baseline to 426 (21.3%) under CC01, an increase of 82. High-risk buildings rise from 40 to 73.

**Experiment 2 — Road network disruption.** Flooded road lengths measured by geometric overlay. At 0.2 m, road length at risk rises from 3.87 km (8.1%) to 5.11 km (10.7%). High-risk road length rises from 0.28 km to 0.45 km, and 0.86 km of A-roads fall within the CC01 zone.

**Experiment 3 — SuDS constraint map.** Slope from the DTM, land cover from WorldCover, and flood zone proximity combined into a pixel-level opportunity score. Geology is entirely Thames Group clay, so infiltration SuDS is not viable anywhere on site.

| Classification | Area | Share of study area | Overlap with CC01 flood zone |
|---|---|---|---|
| High opportunity | 123.4 ha | 28.7% | 20.9 ha |
| Medium opportunity | 223.4 ha | 51.9% | 17.6 ha |
| Low opportunity | 56.7 ha | 13.2% | 2.6 ha |
| Constrained | 26.9 ha | 6.3% | 0.0 ha |
| Total viable | 346.8 ha | 80.6% | 38.5 ha |

**Experiment 4 — Climate change delta map.** Baseline flood zones spatially subtracted from CC01 zones at each depth to isolate newly created risk.

| Depth | Baseline | CC01 | New area | New buildings | New roads |
|---|---|---|---|---|---|
| 0.2 m | 32.1 ha | 41.1 ha | +9.0 ha | +277 | +1.23 km |
| 0.3 m | 30.4 ha | 39.8 ha | +9.4 ha | +256 | +1.26 km |
| 0.6 m | 29.1 ha | 39.3 ha | +10.2 ha | +242 | +1.26 km |
| 0.9 m | 29.0 ha | 39.2 ha | +10.2 ha | +241 | +1.26 km |
| 1.2 m | 29.0 ha | 39.2 ha | +10.2 ha | +242 | +1.26 km |

The new zone stabilises at 10.2 ha from 0.6 m onwards, representing the irreducible climate change footprint and the primary SuDS design target.

### Data quality

All 19 layers are confirmed in EPSG:27700 with no CRS mismatches, no null, invalid, or empty geometries, and no null values in critical attribute fields. Flood layers are internally consistent, with extent decreasing as depth increases and CC01 exceeding baseline at every threshold. The DTM contains no elevation outliers.

Minor non-blocking issues are recorded as follows. Among buildings, 41 footprints are under 10 m² and are likely garages or outbuildings, 23 have height recorded as 0 m from unresolved ML detection, and 51 sit just outside the study boundary as edge overspill from the source dataset. Among roads, 2 segments are shorter than 5 m and represent junction topology slivers, while 120 segments (20.2%) are unnamed, which is standard for OS OpenRoads service roads and access tracks. For rasters, WorldCover at 7.6 m resolution against the 1 m DTM is acceptable at catchment scale but limits sub-parcel precision, and tree canopy data covers whole wards with no within-ward variation.

### Known gaps

Four datasets from the original plan were not collected. None blocked the completed experiments, and each has a usable substitute.

| Missing dataset | Priority | Substitute | Impact |
|---|---|---|---|
| OS Open Rivers | Medium | DTM flow accumulation derivation | Needed for precise SuDS placement in the drainage catchment |
| Fluvial Flood Risk (RoFR) | Medium | DTM elevation proxy below 35 m AOD | Needed for combined river and surface water risk analysis |
| LCM 2022 (UKCEH) | Low | WorldCover 2022 | Fewer land cover classes and lower resolution |
| Sentinel-2 NDWI | Low | Flood polygons and DTM low points | Waterlogged areas outside mapped flood polygons not captured |

All substitutes are defensible at catchment scale, and any derived layers are labelled as proxies in outputs.

### Fitness for further work

The sub-study dataset supports flood exposure analysis at any depth or risk band threshold, building and road risk classification, terrain analysis including slope, aspect and flow direction, land cover characterisation and impervious surface estimation, SuDS constraint and opportunity mapping, and baseline against CC01 comparison.

Three further tasks require additional derivation first. Drainage routing and flow accumulation need a river network derived from the DTM, combined fluvial and surface water risk needs a terrain proxy from DTM low points, and sub-parcel SuDS site design is limited by WorldCover resolution at individual site level.

## Citation

If you use this dataset, please cite the following related AI4MultiGIS publications:

- Hassan, M., Sardar, B., Islam, S., Imani, M., & Hakiri, A. (2026). From principles to practice: Engineering responsible AI for geospatial intelligence. *SN Computer Science*, 7(6), 692. [https://doi.org/10.1007/s42979-026-05258-0](https://link.springer.com/article/10.1007/s42979-026-05258-0)

- Wu, Z., & Islam, S. (2026). SAM2-based few-shot segmentation for remote sensing imagery with explainable AI. In *Management of Digital EcoSystems* (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 104–115. Springer, Cham. [https://doi.org/10.1007/978-3-032-36554-5_8](https://link.springer.com/chapter/10.1007/978-3-032-36554-5_8)

- Hochbauer, H., Basheer, N., Frincu, M., & Islam, S. (2026). Beyond accuracy: Responsible AI and synthetic data in GIS. In *Management of Digital EcoSystems* (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 116–130. Springer, Cham. [https://doi.org/10.1007/978-3-032-36554-5_9](https://link.springer.com/chapter/10.1007/978-3-032-36554-5_9)

## License

## Contact

Muhammad Hassan, Research Assistant, AI4MultiGIS Project, Anglia Ruskin University.
Muhammad.hassan@aru.ac.uk
