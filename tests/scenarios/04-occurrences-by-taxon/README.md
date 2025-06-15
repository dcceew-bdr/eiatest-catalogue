# Scenario 04 - Occurrences by Taxon

## Details

### Description

This scenario shows how the National Species List can be used to search for occurrences by species or genus or informal grouping name.

### Purpose

Shows simple integration of the NSL & BDR.

### Logic

Retrieve, from the BRD, all Occurrences of either a species (name) or a set of such, depending on selection in the NSL.

### Steps

1. Select an NLS genus/species/subspecies name
2. Click "Show Occurrences" button 

### Postconditions

All Occurences of that Concept or narrower Concepts are shown on the map

## Queries

Find all BDR CASE Occurrences per NSL Taxon Name or narrower Taxon Name.

e.g. `{TAXON-NAME} = "https://linked.data.gov.au/dataset/eiatest/nsl/anas"`

See template below.
 
### Template

```sparql
PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX time: <http://www.w3.org/2006/time#>

SELECT ?o ?space ?time ?taxon_name_pl
WHERE {
	{
      SELECT ?taxon_name ?taxon_name_pl
      WHERE {
	    BIND (<{TAXON-NAME}> AS ?c)
        ?c
          skos:inScheme <https://linked.data.gov.au/dataset/eiatest/nsl> ;
          skos:narrower* ?taxon_name ;
        .
  
  		?taxon_name skos:prefLabel ?taxon_name_pl .
      }
    }
    ?o 
      a dwc:Occurrence ;
  	  dwc:scientificNameID ?taxon_name ;
      geo:hasGeometry/geo:asWKT ?space ;
      time:hasTime/time:inXSDDateTime ?time ;
    .
}
```

| **File**          | **Parameter Variable** | **Parameter Values**                                               | **Expected results** |
|-------------------|------------------------|--------------------------------------------------------------------|----------------------|
| `query-01.sparql` | TAXON-NAME             | `https://linked.data.gov.au/dataset/eiatest/nsl/anas`              | 20 Occurrences       |
| `query-02.sparql` | TAXON-NAME             | `https://linked.data.gov.au/dataset/eiatest/nsl/anas-superciliosa` | 9 Occurrences        |

