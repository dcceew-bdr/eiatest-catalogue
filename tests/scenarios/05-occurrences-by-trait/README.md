# Scenario 05 - Occurrences by Trait

## Details

### Description

### Purpose

### Logic

### Steps

ont:hasContextObject obo:PO_0025034 .  # leaf (218)
ont:hasContextObject obo:PO_0004518 .  # bark (27)
obo:PO_0009001  # fruit (24+)
PO_0000003  # whole plant (89+)

```
PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT *
WHERE {
  ?c a skos:Concept ;
      skos:inScheme <https://linked.data.gov.au/dataset/eiatest/nsl> ;
	.
  
  MINUS {
    ?c dwc:kingdom <https://linked.data.gov.au/dataset/eiatest/nsl/plantae>
  }
}
```

### Postconditions

## Queries

### Template

```

```

| **File**          | **Parameter Variable**        | **Parameter Values**                                                                            | **Expected results**                     |
|-------------------|-------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
| `query-01.sparql` | `XXXX`, WKT Literal (polygon) | `POLYGON ((141.5 -25, 141.5 -28.5, 146 -28.5, 146 -25, 141.5 -25))` - SE Qld                    | AusTraits, BDR                           |
| `query-02.sparql` | As above                      | `POLYGON ((148.8 -35.35, 148.8 -35.53, 149 -35.53, 149 -35.35, 148.8 -35.35))` - Within the ACT | ANSIS, AusTraits, BDR, HCAS, NVIS, SPRAT |

