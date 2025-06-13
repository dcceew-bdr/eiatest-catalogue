# Scenario 01 - Data Presence

## Details

### Description

This scenario shows how all datasets relevant to a given and time range & area can be listed with their kind.

### Purpose

Shows integration of datasets at a metadata-only level.

### Logic

Retrieve, for each dataset with Bounding Box overlapping a given area and a temporal range overlapping a given time/time range, the Dataset IRI, name, the bounding box polygon, and the EnvThes classification (kind).

### Steps

1. Select an area on the map
2. Select a temporal range on the form
3. Click GO
4. Click on indicated data on the map or list below the map for details

### Postconditions

1. Map shows both the user-defined search area and the bounding boxes of each Dataset overlapped
    * bounding boxes are coloured according to major EnvThes themes
    * clicking on the dataset's areas pops up an info box with temporal range and theme indicated, as well as a link to the Prez location of the object
2. A table of results is shown under the Map
    * showing the same info as the pop-up info box

## Queries

### Template

```
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX schema: <https://schema.org/>

SELECT ?iri ?name ?dataset_bb ?kw ?kw_label
WHERE {
    ?iri
        a schema:Dataset ;
        schema:name ?name ;
        schema:keywords ?kw ;
        geo:hasBoundingBox/geo:asWKT ?dataset_bb ;
    .

    ?kw schema:name ?kw_label .

    BIND (XXXX^^geo:wktLiteral AS ?input_area)

    FILTER geof:sfIntersects(?input_area, ?dataset_bb)
}
ORDER BY ?name
```

| **File**          | **Parameter Variable**        | **Parameter Values**                                                                            | **Expected results**                     |
|-------------------|-------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
| `query-01.sparql` | `XXXX`, WKT Literal (polygon) | `POLYGON ((141.5 -25, 141.5 -28.5, 146 -28.5, 146 -25, 141.5 -25))` - SE Qld                    | AusTraits, BDR                           |
| `query-02.sparql` | As above                      | `POLYGON ((148.8 -35.35, 148.8 -35.53, 149 -35.53, 149 -35.35, 148.8 -35.35))` - Within the ACT | ANSIS, AusTraits, BDR, HCAS, NVIS, SPRAT |


### Test Data

Area 1 = "POLYGON ((148.65395325019938 -35.447281913902835, 148.88490001016882 -35.44653208676007, 148.88190070159777 -35.57400270102891, 148.6517037687711 -35.57250304674339, 148.65395325019938 -35.447281913902835))"
5

Area 2 = "POLYGON ((149.2335696315512 -35.77645602957353, 149.38578454153105 -35.773456721002496, 149.38428488724554 -35.89642837241479, 149.2335696315512 -35.897928026700306, 149.2335696315512 -35.77645602957353))"
4

Area 3 = "POLYGON ((148.5242331545023 -34.9996351096764, 148.77167611161238 -34.95464548111092, 148.9261405030205 -34.986138221106756, 148.98012805729905 -35.11060952680456, 148.9261405030205 -35.19459016679343, 148.81666574017785 -35.233581178216845, 148.7266864830469 -35.254576338214065, 148.61721172020427 -35.226082906789266, 148.51973419164574 -35.23058186964581, 148.3832656516638 -35.220084289647204, 148.35027325738247 -35.14810088394245, 148.36676945452314 -35.05062335538393, 148.4987390316485 -35.04012577538532, 148.5362303887864 -35.03262750395774, 148.54072935164297 -35.01763096110258, 148.5242331545023 -34.9996351096764))"
4

Australia = "POLYGON ((153.8 -10, 112.7 -10, 112.7 -43.9, 153.8 -43.9, 153.8 -10))"

ACT = "POLYGON ((148.75 -35.12, 148.75 -35.95, 149.425 -35.95, 149.425 -35.12, 148.75 -35.12))"