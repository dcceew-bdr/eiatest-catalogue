# Scenario 01 - Data Presence

## Details

### Description

This scenario shows how all datasets relevant to a given area can be listed with their kind given.

### Purpose

Shows integration of datasets at a metadata-only level.

### Logic

Retrieve, for each dataset with Bounding Box overlapping a given area, Dataset IRI, name, the bounding box polygon, and the EnvThes classification (kind).

### Steps

1. Select an area on the map
2. Click GO
3. Click on indicated data on the map or list below the map for details

### Postconditions

1. Map shows both the user-defined search area and the bounding boxes of each Dataset overlapped
    * bounding boxes are coloured according to major EnvThes themes
2. A table of results is shown under the Map
3. Map and table results ar clickable to reveal more dataset details
    * Dataset details can be any/all Dataset metadata

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

    FILTER geof:sfOverlaps(XXXX, ?dataset_bb)
}
ORDER BY ?name
```

| **File**          | **Parameter Variable**        | **Parameter Values**                                                                            | **Expected results**                     |
|-------------------|-------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
| `query-01.sparql` | `XXXX`, WKT Literal (polygon) | `POLYGON ((141.5 -25, 141.5 -28.5, 146 -28.5, 146 -25, 141.5 -25))` - SE Qld                    | AusTraits, BDR                           |
| `query-02.sparql` | As above                      | `POLYGON ((148.8 -35.35, 148.8 -35.53, 149 -35.53, 149 -35.35, 148.8 -35.35))` - Within the ACT | ANSIS, AusTraits, BDR, HCAS, NVIS, SPRAT |