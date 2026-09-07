# Chelmsford SuDS Dataset

Geospatial dataset supporting flood risk and Sustainable Drainage System (SuDS) analysis for Chelmsford, Essex, UK. Produced as part of the AI4MultiGIS project (UKRI CHIST-ERA, grant EP/Z003490/1), Anglia Ruskin University.

Project website: <https://www.ai4multigis.eu>

A clipped sample of the sub-study data is included in this repository at `samples/chelmer-village-cm1-6ea/`. The full dataset is not committed here, for the reasons given under [Data availability](#data-availability).

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
| --- | --- |
| Study area | 342 km², Chelmsford, Essex, UK |
| Coordinate reference system | EPSG:32630 |
| Labelled pixels | 12,847 at 10 m resolution |
| Fused modalities | 35 |
| Class distribution | Severe imbalance; High Risk class is 0.44% of labelled pixels |

## Repository structure

This repository holds documentation, the sample extract, and the script that generates it. The full dataset is archived externally.

```
samples/
└── chelmer-village-cm1-6ea/
    ├── README.md
    ├── data/
    │   ├── vectors/suds_substudy_sample.gpkg
    │   ├── raster/suds_opportunity.tif
    │   └── manifest.json
    └── scripts/build_sample.py
```

The archived full dataset is organised as follows.

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
| --- | --- | --- | --- | --- | --- |
| V1 | OS Open Rivers | Ordnance Survey | Shapefile | 2024 | EPSG:32630 |
| V2 | Road Network | Ordnance Survey | Shapefile | 2024 | EPSG:32630 |
| V3 | Rivers and Sea Flood Risk | Environment Agency | Shapefile | 2024 | EPSG:32630 |
| V4 | Surface Water Flood Risk | Environment Agency | Shapefile | 2024 | EPSG:32630 |
| V5 | Surface Water Flood Risk, CC1 scenario | Environment Agency | Shapefile | 2024 | EPSG:32630 |
| | Building footprints (57,975 polygons) | Microsoft GlobalML | GeoJSON | | EPSG:4326 |

The building footprints layer is supplied in EPSG:4326 and requires reprojection to EPSG:32630 before use with the other layers. Attributes include `centroid_lat`, `centroid_lon`, `height_m`, `confidence`, and `num_vertices`.

### Raster layers

| ID | Layer | Source | Format | Date | CRS |
| --- | --- | --- | --- | --- | --- |
| R1 | DEM/DTM, 1 m LiDAR | Environment Agency | GeoTIFF | 2022 | EPSG:32630 |
| R2 | Land use | UKCEH Land Cover Map | GeoTIFF | 2022 | EPSG:32630 |
| R3 | Sentinel-2 median composite (ALLBANDS, RGB, NDVI, NDWI, NDBI) | Google Earth Engine | GeoTIFF | Oct 2024 to May 2025 | EPSG:32630 |

### Supporting files

| ID | File | Description | Status |
| --- | --- | --- | --- |
| M1 | Sentinel-2 metadata | Acquisition metadata for the composite | Included |
| P1 | Soil Type, NATMAP | National soil classification | Included |

## Data preparation

All vector and raster layers are resampled to a common 10 m grid in EPSG:32630 and fused into a 35-band modality stack. Labels are assigned at 12,847 pixel locations, with the High Risk class making up 0.44% of labels.

## Focused sub-study: Chelmer Village and Beaulieu Park

A detailed sub-study covers Chelmer Village and Beaulieu Park in North Chelmsford (CM1 6EA), examining surface water flood risk and SuDS opportunity at development scale. Note that the sub-study layers are held in EPSG:27700, not the EPSG:32630 used by the wider pilot.

| Property | Value |
| --- | --- |
| Study area | 430 ha, CM1 6EA |
| Buildings | 1,997 |
| Road network | 47.9 km |
| Spatial layers | 19 |
| Coordinate reference system | EPSG:27700 (British National Grid) |

### Sub-study layer inventory

All 19 layers are standardised to EPSG:27700 and verified for geometry validity, spatial alignment, and attribute completeness.

| Dataset | Type | Source | Detail |
| --- | --- | --- | --- |
| Study Boundary | Polygon | CM1 6EA boundary | 430 ha polygon |
| Buildings | Polygon | Microsoft Global ML | 1,997 footprints, reprojected from WGS84 |
| Baseline Flood 0.2 to 1.2 m | Polygon | Environment Agency RoFSW | 5 layers, 29 to 32 ha core |
| CC01 Flood 0.2 to 1.2 m | Polygon | Environment Agency CC01 | 5 layers, 39 to 41 ha |
| DTM 1 m LiDAR | Raster | OS/EA LiDAR | 1 m resolution, 23.1 to 61.5 m AOD |
| WorldCover 2022 | Raster | ESA WorldCover | 7.6 m resolution, 7 land cover classes |
| Geology | Polygon | BGS HydrogeologyUK v5 | Single polygon, Thames Group clay |
| Soil Permeability | Polygon | BGS HydrogeologyUK v5 | Class 3 impermeable, entire site |
| Rainfall | Polygon | Chelmsford Station 2016 to 2025 | 580 mm/yr, monthly values |
| Roads | Line | OS OpenRoads | 595 segments, 47.9 km total |
| Tree Canopy Cover | Polygon | Forest Research 2022 | 2 wards, 8.9% weighted average |

### Completed experiments

Four experiments have been run on the sub-study data, comparing the Environment Agency baseline against the CC01 climate change scenario across five depth thresholds (0.2, 0.3, 0.6, 0.9, 1.2 m).

**Experiment 1, building flood exposure.** Buildings joined against all 10 flood layers and scored by risk band. At 0.2 m, buildings at risk rise from 344 (17.2%) under baseline to 426 (21.3%) under CC01, an increase of 82. High-risk buildings rise from 40 to 73.

**Experiment 2, road network disruption.** Flooded road lengths measured by geometric overlay. At 0.2 m, road length at risk rises from 3.87 km (8.1%) to 5.11 km (10.7%). High-risk road length rises from 0.28 km to 0.45 km, and 0.86 km of A-roads fall within the CC01 zone.

**Experiment 3, SuDS constraint map.** Slope from the DTM, land cover from WorldCover, and flood zone proximity combined into a pixel-level opportunity score. Geology is entirely Thames Group clay, so infiltration SuDS is not viable anywhere on site.

| Classification | Area | Share of study area | Overlap with CC01 flood zone |
| --- | --- | --- | --- |
| High opportunity | 123.4 ha | 28.7% | 20.9 ha |
| Medium opportunity | 223.4 ha | 51.9% | 17.6 ha |
| Low opportunity | 56.7 ha | 13.2% | 2.6 ha |
| Constrained | 26.9 ha | 6.3% | 0.0 ha |
| Total viable | 346.8 ha | 80.6% | 38.5 ha |

**Experiment 4, climate change delta map.** Baseline flood zones spatially subtracted from CC01 zones at each depth to isolate newly created risk.

| Depth | Baseline | CC01 | New area | New buildings | New roads |
| --- | --- | --- | --- | --- | --- |
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
| --- | --- | --- | --- |
| OS Open Rivers | Medium | DTM flow accumulation derivation | Needed for precise SuDS placement in the drainage catchment |
| Fluvial Flood Risk (RoFR) | Medium | DTM elevation proxy below 35 m AOD | Needed for combined river and surface water risk analysis |
| LCM 2022 (UKCEH) | Low | WorldCover 2022 | Fewer land cover classes and lower resolution |
| Sentinel-2 NDWI | Low | Flood polygons and DTM low points | Waterlogged areas outside mapped flood polygons not captured |

All substitutes are defensible at catchment scale, and any derived layers are labelled as proxies in outputs.

### Fitness for further work

The sub-study dataset supports flood exposure analysis at any depth or risk band threshold, building and road risk classification, terrain analysis including slope, aspect and flow direction, land cover characterisation and impervious surface estimation, SuDS constraint and opportunity mapping, and baseline against CC01 comparison.

Three further tasks require additional derivation first. Drainage routing and flow accumulation need a river network derived from the DTM, combined fluvial and surface water risk needs a terrain proxy from DTM low points, and sub-parcel SuDS site design is limited by WorldCover resolution at individual site level.

## Clipped sample

The sub-study data is too large to distribute through this repository, therefore a small extract is provided at `samples/chelmer-village-cm1-6ea/` so that the data structure can be inspected and the processing scripts run without the full archive. Every raster and vector layer is clipped to one shared square box, the vectors are merged into a single GeoPackage, and the raster is compressed. The sample totals 6.46 MB against a 45 MB budget.

### Sample extent

| Property | Value |
| --- | --- |
| CRS | EPSG:27700 (OSGB36 / British National Grid) |
| Box side | 1600 m by 1600 m |
| Centre (E, N) | 572933.0, 210170.6 |
| Bounding box | 572133.0, 209370.6, 573733.0, 210970.6 |
| Approximate WGS84 | 0.49258, 51.75657, 0.51654, 51.77045 |
| Area | 2.56 km² |

The box is centred on the centroid of the study boundary's bounding box, which spans 571585.7, 208722.4 to 574280.2, 211618.8, or 2.69 km by 2.90 km. The sample therefore covers about 33% of that bounding box, which corresponds to roughly 60% of the 430 ha study area itself, since the boundary polygon does not fill its bounding box. Retained feature counts are consistent with this, at 68% of buildings and 65% of road segments.

Every vector layer is clipped to exactly this box. The raster covers the same box snapped to the source 1 m pixel grid, so it lands within one pixel of the vector bounds, 0.42 m on the Y edges. Resampling the class values to force an exact match would have been worse. The box is also stored as a `clip_box` layer inside the GeoPackage, so the extent travels with the data.

### Sample contents

`data/vectors/suds_substudy_sample.gpkg`, 6.20 MB. All 17 source shapefiles merged into one GeoPackage, one layer each, plus `clip_box`. Every layer is EPSG:27700.

| Layer | Geometry | Features (source) | Features (clipped) |
| --- | --- | --- | --- |
| `study_boundary` | Polygon | 1 | 1 |
| `buildings` | MultiPolygon | 1,997 | 1,367 |
| `rofsw_0_2m` | MultiPolygon | 49 | 16 |
| `rofsw_0_3m` | MultiPolygon | 49 | 16 |
| `rofsw_0_6m` | MultiPolygon | 44 | 16 |
| `rofsw_0_9m` | MultiPolygon | 35 | 15 |
| `rofsw_1_2m` | MultiPolygon | 31 | 12 |
| `crofsw_cc01_0_2m` | MultiPolygon | 50 | 16 |
| `crofsw_cc01_0_3m` | MultiPolygon | 49 | 16 |
| `crofsw_cc01_0_6m` | MultiPolygon | 47 | 16 |
| `crofsw_cc01_0_9m` | MultiPolygon | 39 | 16 |
| `crofsw_cc01_1_2m` | MultiPolygon | 35 | 13 |
| `geology` | Polygon | 1 | 1 |
| `soil_permeability` | Polygon | 1 | 1 |
| `roads` | LineString | 595 | 387 |
| `rainfall` | Polygon | 1 | 1 |
| `tree_canopy` | Polygon | 2 | 2 |

Six source layers, the `rofsw_*` set and `roads`, carried an attribute literally named `fid`, which collides with the GeoPackage primary key. It is preserved as `src_fid`.

`data/raster/suds_opportunity.tif`, 0.25 MB. The SuDS opportunity and constraint map from Experiment 3, 1600 by 1600 px at 1 m resolution, reduced from a 32 MB source. It is clipped from 2694 by 2895 px, converted from float32 to uint8 because the values were only ever the integers 0 to 4, compressed with DEFLATE at level 9 with predictor 2, tiled at 256 by 256, and given 255 as its nodata value in place of NaN.

The raster carries an embedded colour table, so it opens as a thematic map rather than needing symbology applied by hand. Without it, a five-class map holding only the values 0 to 4 renders as a near-black image on any viewer that stretches a byte raster across the full 0 to 255 range. Colours follow `CLASS_COLOURS` in `experiment_3_suds_constraint_map.py`.

| Value | Class | Colour |
| --- | --- | --- |
| 0 | Outside study area | white |
| 1 | Constrained | `#d7191c` |
| 2 | Low opportunity | `#ffffbf` |
| 3 | Medium opportunity | `#a6d96a` |
| 4 | High opportunity | `#1a9641` |
| 255 | NoData | transparent |

Class labels are also written as GeoTIFF tags (`CLASS_0` through `CLASS_4`).

`data/manifest.json` records the exact bounds, per-layer feature counts, and the size of every build attempt.

### Reproducing the sample

```bash
pip install geopandas rasterio
python samples/chelmer-village-cm1-6ea/scripts/build_sample.py
```

The script unpacks the source archive, clips every layer to the shared box, and shrinks the box in 100 m steps until the output fits the size budget. It completed on the first pass at 1600 m, leaving around 39 MB of headroom, so `START_SIDE` can be raised for a larger sample. Set `SUDS_RAW_DIR` to the location of the raw dataset.

Note that the sample carries the derived opportunity raster but not the 1 m DTM or WorldCover 2022 layers that produced it, so Experiment 3 cannot be rerun from the sample alone.

The sub-study road layer is taken from `roads.shp` inside the Chelmsford archive, not from the GB-wide OS OpenRoads extract. The copy of that extract in the working delivery was a partial unpack of a truncated archive, with no projection files and incomplete component sets, and did not include the Essex tiles. It is not required for the sample or for any completed experiment.

## Data availability

The full dataset is not held in this repository because of file size limits. It is archived separately, and the DOI will be recorded here once the deposit is published.

## Citation

If you use this dataset, please cite the following related AI4MultiGIS publications:

- Hassan, M., Sardar, B., Islam, S., Imani, M., & Hakiri, A. (2026). From principles to practice: Engineering responsible AI for geospatial intelligence. *SN Computer Science*, 7(6), 692. <https://doi.org/10.1007/s42979-026-05258-0>

- Wu, Z., & Islam, S. (2026). SAM2-based few-shot segmentation for remote sensing imagery with explainable AI. In *Management of Digital EcoSystems* (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 104-115. Springer, Cham. <https://doi.org/10.1007/978-3-032-36554-5_8>

- Hochbauer, H., Basheer, N., Frincu, M., & Islam, S. (2026). Beyond accuracy: Responsible AI and synthetic data in GIS. In *Management of Digital EcoSystems* (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 116-130. Springer, Cham. <https://doi.org/10.1007/978-3-032-36554-5_9>

## License

Source layers are redistributed under the terms of their original providers, including the Environment Agency, Ordnance Survey, British Geological Survey, UKCEH, ESA and Microsoft. Licence terms for each source apply to the derived and clipped layers in this repository and should be checked before reuse.

## Contact

Muhammad Hassan, Research Assistant, AI4MultiGIS Project, Anglia Ruskin University. <Muhammad.hassan@aru.ac.uk>

Raster layers
ID	Layer	Source	Format	Date	CRS
R1	DEM/DTM, 1 m LiDAR	Environment Agency	GeoTIFF	2022	EPSG:32630
R2	Land use	UKCEH Land Cover Map	GeoTIFF	2022	EPSG:32630
R3	Sentinel-2 median composite (ALLBANDS, RGB, NDVI, NDWI, NDBI)	Google Earth Engine	GeoTIFF	Oct 2024 to May 2025	EPSG:32630
Supporting files
ID	File	Description	Status
M1	Sentinel-2 metadata	Acquisition metadata for the composite	Included
P1	Soil Type, NATMAP	National soil classification	Included
Data preparation
All vector and raster layers are resampled to a common 10 m grid in EPSG:32630 and fused into a 35-band modality stack. Labels are assigned at 12,847 pixel locations, with the High Risk class making up 0.44% of labels.

Focused sub-study: Chelmer Village and Beaulieu Park
A detailed sub-study covers Chelmer Village and Beaulieu Park in North Chelmsford (CM1 6EA), examining surface water flood risk and SuDS opportunity at development scale. Note that the sub-study layers are held in EPSG:27700, not the EPSG:32630 used by the wider pilot.

Property	Value
Study area	430 ha, CM1 6EA
Buildings	1,997
Road network	47.9 km
Spatial layers	19
Coordinate reference system	EPSG:27700 (British National Grid)
Sub-study layer inventory
All 19 layers are standardised to EPSG:27700 and verified for geometry validity, spatial alignment, and attribute completeness.

Dataset	Type	Source	Detail
Study Boundary	Polygon	CM1 6EA boundary	430 ha polygon
Buildings	Polygon	Microsoft Global ML	1,997 footprints, reprojected from WGS84
Baseline Flood 0.2 to 1.2 m	Polygon	Environment Agency RoFSW	5 layers, 29 to 32 ha core
CC01 Flood 0.2 to 1.2 m	Polygon	Environment Agency CC01	5 layers, 39 to 41 ha
DTM 1 m LiDAR	Raster	OS/EA LiDAR	1 m resolution, 23.1 to 61.5 m AOD
WorldCover 2022	Raster	ESA WorldCover	7.6 m resolution, 7 land cover classes
Geology	Polygon	BGS HydrogeologyUK v5	Single polygon, Thames Group clay
Soil Permeability	Polygon	BGS HydrogeologyUK v5	Class 3 impermeable, entire site
Rainfall	Polygon	Chelmsford Station 2016 to 2025	580 mm/yr, monthly values
Roads	Line	OS OpenRoads	595 segments, 47.9 km total
Tree Canopy Cover	Polygon	Forest Research 2022	2 wards, 8.9% weighted average
Completed experiments
Four experiments have been run on the sub-study data, comparing the Environment Agency baseline against the CC01 climate change scenario across five depth thresholds (0.2, 0.3, 0.6, 0.9, 1.2 m).

Experiment 1, building flood exposure. Buildings joined against all 10 flood layers and scored by risk band. At 0.2 m, buildings at risk rise from 344 (17.2%) under baseline to 426 (21.3%) under CC01, an increase of 82. High-risk buildings rise from 40 to 73.

Experiment 2, road network disruption. Flooded road lengths measured by geometric overlay. At 0.2 m, road length at risk rises from 3.87 km (8.1%) to 5.11 km (10.7%). High-risk road length rises from 0.28 km to 0.45 km, and 0.86 km of A-roads fall within the CC01 zone.

Experiment 3, SuDS constraint map. Slope from the DTM, land cover from WorldCover, and flood zone proximity combined into a pixel-level opportunity score. Geology is entirely Thames Group clay, so infiltration SuDS is not viable anywhere on site.

Classification	Area	Share of study area	Overlap with CC01 flood zone
High opportunity	123.4 ha	28.7%	20.9 ha
Medium opportunity	223.4 ha	51.9%	17.6 ha
Low opportunity	56.7 ha	13.2%	2.6 ha
Constrained	26.9 ha	6.3%	0.0 ha
Total viable	346.8 ha	80.6%	38.5 ha
Experiment 4, climate change delta map. Baseline flood zones spatially subtracted from CC01 zones at each depth to isolate newly created risk.

Depth	Baseline	CC01	New area	New buildings	New roads
0.2 m	32.1 ha	41.1 ha	+9.0 ha	+277	+1.23 km
0.3 m	30.4 ha	39.8 ha	+9.4 ha	+256	+1.26 km
0.6 m	29.1 ha	39.3 ha	+10.2 ha	+242	+1.26 km
0.9 m	29.0 ha	39.2 ha	+10.2 ha	+241	+1.26 km
1.2 m	29.0 ha	39.2 ha	+10.2 ha	+242	+1.26 km
The new zone stabilises at 10.2 ha from 0.6 m onwards, representing the irreducible climate change footprint and the primary SuDS design target.

Data quality
All 19 layers are confirmed in EPSG:27700 with no CRS mismatches, no null, invalid, or empty geometries, and no null values in critical attribute fields. Flood layers are internally consistent, with extent decreasing as depth increases and CC01 exceeding baseline at every threshold. The DTM contains no elevation outliers.

Minor non-blocking issues are recorded as follows. Among buildings, 41 footprints are under 10 m² and are likely garages or outbuildings, 23 have height recorded as 0 m from unresolved ML detection, and 51 sit just outside the study boundary as edge overspill from the source dataset. Among roads, 2 segments are shorter than 5 m and represent junction topology slivers, while 120 segments (20.2%) are unnamed, which is standard for OS OpenRoads service roads and access tracks. For rasters, WorldCover at 7.6 m resolution against the 1 m DTM is acceptable at catchment scale but limits sub-parcel precision, and tree canopy data covers whole wards with no within-ward variation.

Known gaps
Four datasets from the original plan were not collected. None blocked the completed experiments, and each has a usable substitute.

Missing dataset	Priority	Substitute	Impact
OS Open Rivers	Medium	DTM flow accumulation derivation	Needed for precise SuDS placement in the drainage catchment
Fluvial Flood Risk (RoFR)	Medium	DTM elevation proxy below 35 m AOD	Needed for combined river and surface water risk analysis
LCM 2022 (UKCEH)	Low	WorldCover 2022	Fewer land cover classes and lower resolution
Sentinel-2 NDWI	Low	Flood polygons and DTM low points	Waterlogged areas outside mapped flood polygons not captured
All substitutes are defensible at catchment scale, and any derived layers are labelled as proxies in outputs.

Fitness for further work
The sub-study dataset supports flood exposure analysis at any depth or risk band threshold, building and road risk classification, terrain analysis including slope, aspect and flow direction, land cover characterisation and impervious surface estimation, SuDS constraint and opportunity mapping, and baseline against CC01 comparison.

Three further tasks require additional derivation first. Drainage routing and flow accumulation need a river network derived from the DTM, combined fluvial and surface water risk needs a terrain proxy from DTM low points, and sub-parcel SuDS site design is limited by WorldCover resolution at individual site level.

Clipped sample
The sub-study data is too large to distribute through this repository, therefore a small extract is provided at samples/chelmer-village-cm1-6ea/ so that the data structure can be inspected and the processing scripts run without the full archive. Every raster and vector layer is clipped to one shared square box, the vectors are merged into a single GeoPackage, and the raster is compressed. The sample totals 6.46 MB against a 45 MB budget.

Sample extent
Property	Value
CRS	EPSG:27700 (OSGB36 / British National Grid)
Box side	1600 m by 1600 m
Centre (E, N)	572933.0, 210170.6
Bounding box	572133.0, 209370.6, 573733.0, 210970.6
Approximate WGS84	0.49258, 51.75657, 0.51654, 51.77045
Area	2.56 km²
The box is centred on the centroid of the study boundary's bounding box, which spans 571585.7, 208722.4 to 574280.2, 211618.8, or 2.69 km by 2.90 km. The sample therefore covers about 33% of that bounding box, which corresponds to roughly 60% of the 430 ha study area itself, since the boundary polygon does not fill its bounding box. Retained feature counts are consistent with this, at 68% of buildings and 65% of road segments.

Every vector layer is clipped to exactly this box. The raster covers the same box snapped to the source 1 m pixel grid, so it lands within one pixel of the vector bounds, 0.42 m on the Y edges. Resampling the class values to force an exact match would have been worse. The box is also stored as a clip_box layer inside the GeoPackage, so the extent travels with the data.

Sample contents
data/vectors/suds_substudy_sample.gpkg, 6.20 MB. All 17 source shapefiles merged into one GeoPackage, one layer each, plus clip_box. Every layer is EPSG:27700.

Layer	Geometry	Features (source)	Features (clipped)
study_boundary	Polygon	1	1
buildings	MultiPolygon	1,997	1,367
rofsw_0_2m	MultiPolygon	49	16
rofsw_0_3m	MultiPolygon	49	16
rofsw_0_6m	MultiPolygon	44	16
rofsw_0_9m	MultiPolygon	35	15
rofsw_1_2m	MultiPolygon	31	12
crofsw_cc01_0_2m	MultiPolygon	50	16
crofsw_cc01_0_3m	MultiPolygon	49	16
crofsw_cc01_0_6m	MultiPolygon	47	16
crofsw_cc01_0_9m	MultiPolygon	39	16
crofsw_cc01_1_2m	MultiPolygon	35	13
geology	Polygon	1	1
soil_permeability	Polygon	1	1
roads	LineString	595	387
rainfall	Polygon	1	1
tree_canopy	Polygon	2	2
Six source layers, the rofsw_* set and roads, carried an attribute literally named fid, which collides with the GeoPackage primary key. It is preserved as src_fid.

data/raster/suds_opportunity.tif, 0.25 MB. The SuDS opportunity and constraint map from Experiment 3, 1600 by 1600 px at 1 m resolution, reduced from a 32 MB source. It is clipped from 2694 by 2895 px, converted from float32 to uint8 because the values were only ever the integers 0 to 4, compressed with DEFLATE at level 9 with predictor 2, tiled at 256 by 256, and given 255 as its nodata value in place of NaN.

The raster carries an embedded colour table, so it opens as a thematic map rather than needing symbology applied by hand. Without it, a five-class map holding only the values 0 to 4 renders as a near-black image on any viewer that stretches a byte raster across the full 0 to 255 range. Colours follow CLASS_COLOURS in experiment_3_suds_constraint_map.py.

Value	Class	Colour
0	Outside study area	white
1	Constrained	#d7191c
2	Low opportunity	#ffffbf
3	Medium opportunity	#a6d96a
4	High opportunity	#1a9641
255	NoData	transparent
Class labels are also written as GeoTIFF tags (CLASS_0 through CLASS_4).

data/manifest.json records the exact bounds, per-layer feature counts, and the size of every build attempt.

Reproducing the sample
pip install geopandas rasterio
python samples/chelmer-village-cm1-6ea/scripts/build_sample.py
The script unpacks the source archive, clips every layer to the shared box, and shrinks the box in 100 m steps until the output fits the size budget. It completed on the first pass at 1600 m, leaving around 39 MB of headroom, so START_SIDE can be raised for a larger sample. Set SUDS_RAW_DIR to the location of the raw dataset.

Note that the sample carries the derived opportunity raster but not the 1 m DTM or WorldCover 2022 layers that produced it, so Experiment 3 cannot be rerun from the sample alone.

The sub-study road layer is taken from roads.shp inside the Chelmsford archive, not from the GB-wide OS OpenRoads extract. The copy of that extract in the working delivery was a partial unpack of a truncated archive, with no projection files and incomplete component sets, and did not include the Essex tiles. It is not required for the sample or for any completed experiment.

Data availability
The full dataset is not held in this repository because of file size limits. It is archived separately, and the DOI will be recorded here once the deposit is published.

Citation
If you use this dataset, please cite the following related AI4MultiGIS publications:

Hassan, M., Sardar, B., Islam, S., Imani, M., & Hakiri, A. (2026). From principles to practice: Engineering responsible AI for geospatial intelligence. SN Computer Science, 7(6), 692. https://doi.org/10.1007/s42979-026-05258-0

Wu, Z., & Islam, S. (2026). SAM2-based few-shot segmentation for remote sensing imagery with explainable AI. In Management of Digital EcoSystems (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 104-115. Springer, Cham. https://doi.org/10.1007/978-3-032-36554-5_8

Hochbauer, H., Basheer, N., Frincu, M., & Islam, S. (2026). Beyond accuracy: Responsible AI and synthetic data in GIS. In Management of Digital EcoSystems (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 116-130. Springer, Cham. https://doi.org/10.1007/978-3-032-36554-5_9

License
Source layers are redistributed under the terms of their original providers, including the Environment Agency, Ordnance Survey, British Geological Survey, UKCEH, ESA and Microsoft. Licence terms for each source apply to the derived and clipped layers in this repository and should be checked before reuse.

Contact
Muhammad Hassan, Research Assistant, AI4MultiGIS Project, Anglia Ruskin University. Muhammad.hassan@aru.ac.uk
