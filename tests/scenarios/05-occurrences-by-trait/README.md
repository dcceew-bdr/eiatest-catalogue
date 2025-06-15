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

### Postconditions

## Queries

### Template

```

```

| **File**          | **Parameter Variable**        | **Parameter Values**                                                                            | **Expected results**                     |
|-------------------|-------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
| `query-01.sparql` | `XXXX`, WKT Literal (polygon) | `POLYGON ((141.5 -25, 141.5 -28.5, 146 -28.5, 146 -25, 141.5 -25))` - SE Qld                    | AusTraits, BDR                           |
| `query-02.sparql` | As above                      | `POLYGON ((148.8 -35.35, 148.8 -35.53, 149 -35.53, 149 -35.35, 148.8 -35.35))` - Within the ACT | ANSIS, AusTraits, BDR, HCAS, NVIS, SPRAT |

