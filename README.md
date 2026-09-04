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

## Citation

If you use this dataset, please cite the following related AI4MultiGIS publications:

- Hassan, M., Sardar, B., Islam, S., Imani, M., & Hakiri, A. (2026). From principles to practice: Engineering responsible AI for geospatial intelligence. *SN Computer Science*, 7(6), 692. [https://doi.org/10.1007/s42979-026-05258-0](https://link.springer.com/article/10.1007/s42979-026-05258-0)

- Wu, Z., & Islam, S. (2026). SAM2-based few-shot segmentation for remote sensing imagery with explainable AI. In *Management of Digital EcoSystems* (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 104–115. Springer, Cham. [https://doi.org/10.1007/978-3-032-36554-5_8](https://link.springer.com/chapter/10.1007/978-3-032-36554-5_8)

- Hochbauer, H., Basheer, N., Frincu, M., & Islam, S. (2026). Beyond accuracy: Responsible AI and synthetic data in GIS. In *Management of Digital EcoSystems* (MEDES 2025), Communications in Computer and Information Science, vol. 3104, pp. 116–130. Springer, Cham. [https://doi.org/10.1007/978-3-032-36554-5_9](https://link.springer.com/chapter/10.1007/978-3-032-36554-5_9)

## License

## Contact

Muhammad Hassan, Research Assistant, AI4MultiGIS Project, Anglia Ruskin University.
Muhammad.hassan@aru.ac.uk
