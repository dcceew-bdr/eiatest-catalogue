import json
from pathlib import Path
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, RDFS, SKOS, XSD, GEO, SDO
REFAREAS_DS = URIRef("https://linked.data.gov.au/dataset/eiatest/refareas")
REFAREAS_ST_FC = URIRef("https://linked.data.gov.au/dataset/eiatest/refareas/st")
REFAREAS_CAPAD_FC = URIRef("https://linked.data.gov.au/dataset/eiatest/refareas/capad2024")
REFAREAS_RAMSAR_FC = URIRef("https://linked.data.gov.au/dataset/eiatest/refareas/ramsar-uc")
TERN = Namespace("https://w3id.org/tern/ontologies/tern/")

from shapely.geometry import shape

g = Graph()

for i, feature in enumerate(json.load(open("ACT.geojson"))["features"]):
    fid = i
    f_iri = URIRef(REFAREAS_ST_FC + "/ACT")
    g.add((f_iri, RDF.type, GEO.Feature))
    g.add((f_iri, SDO.name, Literal(f"Australian Capital Territory")))
    geom = BNode()
    g.add((f_iri, GEO.hasGeometry, geom))
    g.add((geom, RDF.type, GEO.Geometry))
    g.add((geom, GEO.asWKT, Literal(shape(feature["geometry"]).wkt, datatype=GEO.wktLiteral)))

    g.add((REFAREAS_ST_FC, RDFS.member, f_iri))


for i, feature in enumerate(json.load(open("CAPAD.geojson"))["features"]):
    fid = i
    f_iri = URIRef(REFAREAS_CAPAD_FC + "/" + feature["properties"]["PA_PID"])
    g.add((f_iri, RDF.type, GEO.Feature))
    g.add((f_iri, SDO.name, Literal(feature["properties"]["NAME"])))
    geom = BNode()
    g.add((f_iri, GEO.hasGeometry, geom))
    g.add((geom, RDF.type, GEO.Geometry))
    g.add((geom, GEO.asWKT, Literal(shape(feature["geometry"]).wkt, datatype=GEO.wktLiteral)))

    g.add((f_iri, SDO.additionalType, Literal(feature["properties"]["TYPE_ABBR"])))
    g.add((f_iri, SDO.dateIssued, Literal(feature["properties"]["GAZ_DATE"], datatype=XSD.date)))
    g.add((f_iri, SDO.jurisdiction, Literal(feature["properties"]["EPBC"])))

    g.add((REFAREAS_CAPAD_FC, RDFS.member, f_iri))
    print(f"CAPAD {i}, {feature["properties"]["PA_PID"]}")

for i, feature in enumerate(json.load(open("RAMSAR.geojson"))["features"]):
    fid = i
    f_iri = URIRef(REFAREAS_RAMSAR_FC + "/" + feature["properties"]["REFCODE"])
    g.add((f_iri, RDF.type, GEO.Feature))
    g.add((f_iri, SDO.name, Literal(feature["properties"]["RAM_NAME"])))
    g.add((f_iri, SDO.description, Literal(feature["properties"]["POLY_TYPE_"])))
    geom = BNode()
    g.add((f_iri, GEO.hasGeometry, geom))
    g.add((geom, RDF.type, GEO.Geometry))
    g.add((geom, GEO.asWKT, Literal(shape(feature["geometry"]).wkt, datatype=GEO.wktLiteral)))

    g.add((REFAREAS_RAMSAR_FC, RDFS.member, f_iri))
    print(f"RAMSAR {i}, {feature["properties"]["REFCODE"]}")

g.parse(Path(__file__).parent / "refareas-metadata.ttl")
g.serialize(destination="refareas.ttl", format="longturtle")
