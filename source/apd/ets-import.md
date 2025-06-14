# Ecological Trait-data Standard (ETS) Import steps

ETS is used by the AusTraits data.


* source/apd/ets.ttl is a Turtle format copy of <https://github.com/EcologicalTraitData/ETS/blob/master/ets.owl>

These steps are used to convert source/apd/ets.ttl to resources/models/ets.ttl

* add namespace prefix `PREFIX att: <http://rs.tdwg.org/dwc/terms/attributes/>`
* replace `cc:license <http://creativecommons.org/licenses/by/4.0/> ;` with `schema:license <http://purl.org/NET/rdflicense/cc-by4.0> ;`
    * make machine-understandable license
* add `schema:citation "Schneider, F.D., Jochum, M., Le Provost, G., Ostrowski, A., Penone, C. and Simons, N.K. (2019) Ecological Trait-data Standard Vocabulary, v0.10, URL: https://terminologies.gfbio.org/terms/ets/pages/ , DOI: 10.5281/zenodo.2605377" ;`

* replace

```
    a
        rdfs:Class ,
        owl:Class ;
```

with 

```
    a owl:Class ;
```

* replace

```
    a
        rdf:Property ,
        owl:DatatypeProperty ;
```

with 

```
    a owl:DatatypeProperty ;
```

* replace `dcterms:description` with `skos:definition`
* replace `rdfs:label` with `skos:prefLabel`
* remove `dcterms:issued "2017-11-14" ;` from Class definitions
* add prefix `PREFIX ets: <http://terminologies.gfbio.org/terms/ETS/>`
* convert Class `rdfs:comment` to `skos:scopeNote`
* convert property `rdfs:comment` to `skos:example` when the literal starts with "Example"
* removed `PREFIX dc: <http://purl.org/dc/elements/1.1/>`, replacing use with `dcterms:`

* improved all labels with cameCase to spaced
* Agent (People) name to ORCIDs
* Agent (Org) name to IRI
* made OntPub 1.2 valid