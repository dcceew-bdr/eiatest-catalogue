from pathlib import Path
import csv
from rdflib import Graph, URIRef, Literal, Namespace, RDF, SKOS, SDO, XSD, RDFS

VEG = Namespace("https://linked.data.gov.au/dataset/eiatest/nvis-veg/")

cs = URIRef(str(VEG).strip("/"))

g = Graph()
with open(Path(__file__).parent / "nvis-veg-groups.csv") as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        c = URIRef(VEG[row[0]])
        g.add((
            c,
            RDF.type,
            SKOS.Concept,
        ))
        g.add((
            c,
            SDO.color,
            Literal("#000000", datatype=VEG.rgb),
        ))
        g.add((
            c,
            SKOS.inScheme,
            cs
        ))
        g.add((
            c,
            RDFS.isDefinedBy,
            cs
        ))
        g.add((
            c,
            SKOS.prefLabel,
            Literal(row[1], lang="en"),
        ))
        g.add((
            c,
            SKOS.definition,
            Literal(row[1], lang="en"),
        ))
        g.add((
            c,
            SKOS.notation,
            Literal(row[0].strip("0"), datatype=VEG.mvgNumber),
        ))

        g.add((
            c,
            SKOS.topConceptOf,
            cs
        ))

        g.add((
            cs,
            SKOS.hasTopConcept,
            c
        ))

g.parse(
    data="""
PREFIX : <https://linked.data.gov.au/dataset/eiatest/nvis-veg/>
PREFIX cs: <https://linked.data.gov.au/dataset/eiatest/nvis-veg>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<https://linked.data.gov.au/dataset/eiatest/nvis-veg>
    a skos:ConceptScheme ;
    skos:altLabel "ALUM" ;
    skos:definition "Major and minor vegetation groups used in the NVIS data product, based on key dominant genera of flora, height and percentage cover, and represent the broader generic vegetation type denoted by the dominant stratum"@en ;
    skos:historyNote "2025-06: Created from PDFs" ;
    skos:prefLabel "NVIS Major Vegetation Groups and Major Vegetation Subgroups"@en ;
    schema:citation "https://www.dcceew.gov.au/environment/environment-information-australia/national-vegetation-information-system/data-products"^^xsd:anyURI ;
    schema:creator <https://linked.data.gov.au/def/dcceew> ;
    schema:dateCreated "2025-06-19"^^xsd:date ;
    schema:dateModified "2025-06-19"^^xsd:date ;
    schema:keywords
        <http://vocabs.lter-europe.net/EnvThes/20537> ;  # vegetation cover
    schema:publisher <https://linked.data.gov.au/def/dcceew> ;
    schema:version "1" ;
.
    """,
    format="turtle",
)

g.serialize(destination=Path(__file__).parent.parent.resolve().parent / "resources/vocabularies/nvis-veg.ttl", format="longturtle")