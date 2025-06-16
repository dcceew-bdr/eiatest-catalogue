# Scenario 05 - Occurrences by Trait

Building on Scenario 4, this scenario allows a user to search for occurrences of taxa according to traits.

## Details

### Description

This scenario links the AusTraits datasets to the BDR ACT occurrences by linking traits to taxa in the National Species List dataset, to which occurrences are also linked via the scientific name of the taxon they observed.

This scenario only uses 6 traits and a handful of occurrences to prove the mapping.

### Purpose

To crosswalk 3 datasets.

### Logic

### Steps

1. User selected a trait from the available subset of traits (6):
2. User Selects "GO" and is shown a list of locations for occurrences of taxa with that trait

### Postconditions

A list of occurrences of the taxa with that trait is shown on the map.

## Queries

For 1: List of traits linked to taxa:

```
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT *
WHERE {
  ?c
  	skos:inScheme <https://w3id.org/APD/traits> ;
    ^skos:member <https://linked.data.gov.au/dataset/eiatest/eia-demo-collection> ;
     skos:definition ?d
  . 
}
ORDER BY ?d
```

For 2: List of taxa per trait:

```
PREFIX schema: <http://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
PREFIX ex: <http://example.com/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT *
WHERE {
  VALUES ?trait {
    <https://w3id.org/APD/traits/perianth_colour_white>  # in the apd-nsl.ttl file, <https://linked.data.gov.au/dataset/eiatest/eia-demo-collection>
  }
  
  ?trait ex:exhibitorOfTrait ?taxa .   
  ?taxa dwc:vernacularName ?vn .
  
  ?occ 
    dwc:scientificNameID ?taxa ;
    geo:hasGeometry/geo:asWKT ?spatial ;
    time:hasTime/time:inXSDDateTime ?temporal ;
  .
  
  ?ds schema:hasPart* ?occ .
  
}
```
