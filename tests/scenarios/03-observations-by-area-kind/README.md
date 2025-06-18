# Scenario 02 - Observations by area and kind

## Details

### Description

Find all the observations from spatial datasets in a given area and filter by EIA Data Kind

### Purpose

To show that observations of different parts of the environment, from different datasets, have common place/time properties and are can be shown together. 

### Logic

### Steps

1. Select an area on the map
2. Select which kinds of observations to show from Datasets categorised according to the EIA Data Kinds observations
    * all those Concepts <= <https://linked.data.gov.au/def/eia-dk/observations-environment>
3. Click GO

### Postconditions

Data is shown on the map and each Observation (Feature) from the dataset is classified according to the EnvThes keywords classifying the Dataset

## Queries

```
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>

SELECT ?observation ?name ?spatiality ?temporality ?envthes_keyword
WHERE {
    {
        SELECT ?d 
        WHERE {
            VALUES ?eia_kind_keyword {
                <KW1>
                <KW2>
            }
            ?d schema:keywords eia_kind_keyword
        }
    }
    
    ?d 
        schema:keywords ?eia_kind_keyword ;
        rdfs:member/rdfs:member ?feature ;
    .
    
    ?feature 
        geo:hasGeometry/geo:asWKT ?spatiality ;
        time:hasTime/time:inXSDDate ?temporality ;
    .
    
    OPTIONAL {
        ?feature schema:name ?name
    }
}
```