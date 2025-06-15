# Scenario 05 - Occurrences by Trait

## Details

### Description

### Purpose

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

