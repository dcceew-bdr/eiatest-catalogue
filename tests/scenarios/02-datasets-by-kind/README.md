# Scenario 02 - Datasets By Kind

## Details

### Description

This scenario indicates what datasets are available by kind - a single vocabulary environmental domain classification of all EIA datasets.

### Purpose

Shows integration of all EIA data on an environmental classification dimension, albeit a simple one.

### Logic



### Steps

### Postconditions

## Queries

### Template

```

```

| **File**          | **Parameter Variable**        | **Parameter Values**                                                                            | **Expected results**                     |
|-------------------|-------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
| `query-01.sparql` | `XXXX`, WKT Literal (polygon) | `POLYGON ((141.5 -25, 141.5 -28.5, 146 -28.5, 146 -25, 141.5 -25))` - SE Qld                    | AusTraits, BDR                           |
| `query-02.sparql` | As above                      | `POLYGON ((148.8 -35.35, 148.8 -35.53, 149 -35.53, 149 -35.35, 148.8 -35.35))` - Within the ACT | ANSIS, AusTraits, BDR, HCAS, NVIS, SPRAT |

