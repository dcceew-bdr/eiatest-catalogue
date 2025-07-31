import json
from shapely.geometry import shape
from pathlib import Path
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, RDFS, SKOS, XSD, GEO
HCAS_FC = URIRef("https://linked.data.gov.au/dataset/eiatest/hcas/tiles")
HCAS_NS = Namespace("https://linked.data.gov.au/dataset/eiatest/hcas/")
HCAS_TILES = Namespace("https://linked.data.gov.au/dataset/eiatest/hcas/tile/")
TERN = Namespace("https://w3id.org/tern/ontologies/tern/")

# Paste your full GeoJSON in place of this truncated version
geojson_data = {
"type": "FeatureCollection",
"name": "hcas-lowres-vector2",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
{ "type": "Feature", "properties": { "VALUE": 0.64705884 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.198031 ], [ 149.032591, -35.198031 ], [ 149.032591, -35.124591 ], [ 148.942759, -35.124591 ], [ 148.942759, -35.198031 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.65490198 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.198031 ], [ 149.122423, -35.198031 ], [ 149.122423, -35.124591 ], [ 149.032591, -35.124591 ], [ 149.032591, -35.198031 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.67058825 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.198031 ], [ 149.212254, -35.198031 ], [ 149.212254, -35.124591 ], [ 149.122423, -35.124591 ], [ 149.122423, -35.198031 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.64313728 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.271405 ], [ 148.942759, -35.271405 ], [ 148.942759, -35.198031 ], [ 148.852928, -35.198031 ], [ 148.852928, -35.271405 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.66666669 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.271405 ], [ 149.032591, -35.271405 ], [ 149.032591, -35.198031 ], [ 148.942759, -35.198031 ], [ 148.942759, -35.271405 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.627451 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.271405 ], [ 149.122423, -35.271405 ], [ 149.122423, -35.198031 ], [ 149.032591, -35.198031 ], [ 149.032591, -35.271405 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.64313728 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.271405 ], [ 149.212254, -35.271405 ], [ 149.212254, -35.198031 ], [ 149.122423, -35.198031 ], [ 149.122423, -35.271405 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.59215689 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.212254, -35.271405 ], [ 149.302086, -35.271405 ], [ 149.302086, -35.198031 ], [ 149.212254, -35.198031 ], [ 149.212254, -35.271405 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.40392157 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.344712 ], [ 148.852928, -35.344712 ], [ 148.852928, -35.271405 ], [ 148.763096, -35.271405 ], [ 148.763096, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.60784316 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.344712 ], [ 148.942759, -35.344712 ], [ 148.942759, -35.271405 ], [ 148.852928, -35.271405 ], [ 148.852928, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.65882355 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.344712 ], [ 149.032591, -35.344712 ], [ 149.032591, -35.271405 ], [ 148.942759, -35.271405 ], [ 148.942759, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.64705884 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.344712 ], [ 149.122423, -35.344712 ], [ 149.122423, -35.271405 ], [ 149.032591, -35.271405 ], [ 149.032591, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.63529414 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.344712 ], [ 149.212254, -35.344712 ], [ 149.212254, -35.271405 ], [ 149.122423, -35.271405 ], [ 149.122423, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.63921571 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.212254, -35.344712 ], [ 149.302086, -35.344712 ], [ 149.302086, -35.271405 ], [ 149.212254, -35.271405 ], [ 149.212254, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.60784316 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.302086, -35.344712 ], [ 149.391917, -35.344712 ], [ 149.391917, -35.271405 ], [ 149.302086, -35.271405 ], [ 149.302086, -35.344712 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.36078432 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.417954 ], [ 148.852928, -35.417954 ], [ 148.852928, -35.344712 ], [ 148.763096, -35.344712 ], [ 148.763096, -35.417954 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.50588238 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.417954 ], [ 148.942759, -35.417954 ], [ 148.942759, -35.344712 ], [ 148.852928, -35.344712 ], [ 148.852928, -35.417954 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.61176473 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.417954 ], [ 149.032591, -35.417954 ], [ 149.032591, -35.344712 ], [ 148.942759, -35.344712 ], [ 148.942759, -35.417954 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.61176473 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.417954 ], [ 149.122423, -35.417954 ], [ 149.122423, -35.344712 ], [ 149.032591, -35.344712 ], [ 149.032591, -35.417954 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.65882355 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.417954 ], [ 149.212254, -35.417954 ], [ 149.212254, -35.344712 ], [ 149.122423, -35.344712 ], [ 149.122423, -35.417954 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.61176473 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.302086, -35.417954 ], [ 149.391917, -35.417954 ], [ 149.391917, -35.344712 ], [ 149.302086, -35.344712 ], [ 149.302086, -35.417954 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.35686275 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.491128 ], [ 148.852928, -35.491128 ], [ 148.852928, -35.417954 ], [ 148.763096, -35.417954 ], [ 148.763096, -35.491128 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.42352942 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.491128 ], [ 148.942759, -35.491128 ], [ 148.942759, -35.417954 ], [ 148.852928, -35.417954 ], [ 148.852928, -35.491128 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.59215689 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.491128 ], [ 149.032591, -35.491128 ], [ 149.032591, -35.417954 ], [ 148.942759, -35.417954 ], [ 148.942759, -35.491128 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.627451 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.491128 ], [ 149.122423, -35.491128 ], [ 149.122423, -35.417954 ], [ 149.032591, -35.417954 ], [ 149.032591, -35.491128 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.62352943 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.491128 ], [ 149.212254, -35.491128 ], [ 149.212254, -35.417954 ], [ 149.122423, -35.417954 ], [ 149.122423, -35.491128 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.32156864 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.564236 ], [ 148.852928, -35.564236 ], [ 148.852928, -35.491128 ], [ 148.763096, -35.491128 ], [ 148.763096, -35.564236 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.27843139 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.564236 ], [ 148.942759, -35.564236 ], [ 148.942759, -35.491128 ], [ 148.852928, -35.491128 ], [ 148.852928, -35.564236 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.39215687 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.564236 ], [ 149.032591, -35.564236 ], [ 149.032591, -35.491128 ], [ 148.942759, -35.491128 ], [ 148.942759, -35.564236 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.60784316 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.564236 ], [ 149.122423, -35.564236 ], [ 149.122423, -35.491128 ], [ 149.032591, -35.491128 ], [ 149.032591, -35.564236 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.627451 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.564236 ], [ 149.212254, -35.564236 ], [ 149.212254, -35.491128 ], [ 149.122423, -35.491128 ], [ 149.122423, -35.564236 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.32549021 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.637278 ], [ 148.852928, -35.637278 ], [ 148.852928, -35.564236 ], [ 148.763096, -35.564236 ], [ 148.763096, -35.637278 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.28235295 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.637278 ], [ 148.942759, -35.637278 ], [ 148.942759, -35.564236 ], [ 148.852928, -35.564236 ], [ 148.852928, -35.637278 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.39215687 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.637278 ], [ 149.032591, -35.637278 ], [ 149.032591, -35.564236 ], [ 148.942759, -35.564236 ], [ 148.942759, -35.637278 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.6156863 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.637278 ], [ 149.122423, -35.637278 ], [ 149.122423, -35.564236 ], [ 149.032591, -35.564236 ], [ 149.032591, -35.637278 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.65882355 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.122423, -35.637278 ], [ 149.212254, -35.637278 ], [ 149.212254, -35.564236 ], [ 149.122423, -35.564236 ], [ 149.122423, -35.637278 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.29803923 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.710252 ], [ 148.852928, -35.710252 ], [ 148.852928, -35.637278 ], [ 148.763096, -35.637278 ], [ 148.763096, -35.710252 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.27058825 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.710252 ], [ 148.942759, -35.710252 ], [ 148.942759, -35.637278 ], [ 148.852928, -35.637278 ], [ 148.852928, -35.710252 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.40784314 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.710252 ], [ 149.032591, -35.710252 ], [ 149.032591, -35.637278 ], [ 148.942759, -35.637278 ], [ 148.942759, -35.710252 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.50980395 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.710252 ], [ 149.122423, -35.710252 ], [ 149.122423, -35.637278 ], [ 149.032591, -35.637278 ], [ 149.032591, -35.710252 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.28627452 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.763096, -35.783160 ], [ 148.852928, -35.783160 ], [ 148.852928, -35.710252 ], [ 148.763096, -35.710252 ], [ 148.763096, -35.783160 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.29411766 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.783160 ], [ 148.942759, -35.783160 ], [ 148.942759, -35.710252 ], [ 148.852928, -35.710252 ], [ 148.852928, -35.783160 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.38431373 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.783160 ], [ 149.032591, -35.783160 ], [ 149.032591, -35.710252 ], [ 148.942759, -35.710252 ], [ 148.942759, -35.783160 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.32156864 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.783160 ], [ 149.122423, -35.783160 ], [ 149.122423, -35.710252 ], [ 149.032591, -35.710252 ], [ 149.032591, -35.783160 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.33725491 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.852928, -35.856001 ], [ 148.942759, -35.856001 ], [ 148.942759, -35.783160 ], [ 148.852928, -35.783160 ], [ 148.852928, -35.856001 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.29411766 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 148.942759, -35.856001 ], [ 149.032591, -35.856001 ], [ 149.032591, -35.783160 ], [ 148.942759, -35.783160 ], [ 148.942759, -35.856001 ] ] ] } },
{ "type": "Feature", "properties": { "VALUE": 0.34901962 }, "geometry": { "type": "Polygon", "coordinates": [ [ [ 149.032591, -35.856001 ], [ 149.122423, -35.856001 ], [ 149.122423, -35.783160 ], [ 149.032591, -35.783160 ], [ 149.032591, -35.856001 ] ] ] } }
]
}


# Convert each feature to WKT
from shapely.geometry import shape

g = Graph()
g.bind("", HCAS_TILES)
i = 100000
for i, feature in enumerate(geojson_data["features"]):
    fid = i
    f_iri = HCAS_NS[f"tile/{str(fid).zfill(6)}"]
    g.add((f_iri, RDF.type, GEO.Feature))
    geom = BNode()
    g.add((f_iri, GEO.hasGeometry, geom))
    g.add((geom, RDF.type, GEO.Geometry))
    g.add((geom, GEO.asWKT, Literal(shape(feature["geometry"]).wkt, datatype=GEO.wktLiteral)))
    att = BNode()
    g.add((f_iri, TERN.hasAttribute, att))
    g.add((att, TERN.attribute, URIRef("https://linked.data.gov.au/dataset/eiatest/hcas-attributes/habitat-condition")))
    g.add((att, TERN.hasValue, Literal(feature["properties"]["VALUE"], datatype=XSD.float)))
    g.add((HCAS_FC, RDFS.member, f_iri))

p = Path(__file__).parent.parent.resolve().parent /"resources/datasets/spatial/hcas-act-coarse.ttl"
g.parse(Path(__file__).parent / "hcas-metadata.ttl")
txt = g.serialize(format="longturtle")

open(p, "w").write(txt.replace("ns1:", "tern:"))
