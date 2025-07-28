from pathlib import Path
import geopandas as gpd
import pandas as pd
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, RDFS, SKOS, XSD, GEO, SDO

# gdb_path = Path(__file__).parent / "NVIS_V7_0_VECTOR_STATE_FILES_PRE_ALL" / "NVIS_V7_0_VECTOR_STATE_FILES_PRE.gdb"
gdb_path = Path(__file__).parent / "NVIS_V7_0_VECTOR_STATE_FILES_EXT_ALL" / "NVIS_V7_0_VECTOR_STATE_FILES_EXT.gdb"


lut_flat = "NVIS7_0_LUT_AUST_FLAT"
lut_detail = "NVIS7_0_LUT_AUST_DETAIL"
act  = "NVIS7_0_AUST_EXT_ACT"

gdf_flat = gpd.read_file(gdb_path, layer=lut_flat)
gdf_act = gpd.read_file(gdb_path, layer=act, crs=9473)
gdf_act_2 = gdf_act.to_crs(4326)
gdf_act_2['geometry'] = gdf_act_2.geometry.force_2d()
gdf_act_2['geometry'] = gdf_act_2.geometry.set_precision(0.000001)

df = pd.merge(gdf_act_2, gdf_flat, left_on='NVISDSC1', right_on='NVIS_ID', how='left')


DS_NS = Namespace("https://linked.data.gov.au/dataset/eiatest/nvis/")
NVIS_VEG_NS = Namespace("https://linked.data.gov.au/dataset/eiatest/nvis-veg/")

fc = URIRef("https://linked.data.gov.au/dataset/eiatest/nvis/act")

g = Graph()
g.bind("", "https://linked.data.gov.au/dataset/eiatest/nvis/")

g.parse("nvis-metadata.ttl")

for index, row in df.iterrows():
    fid = str(row['MAPUNT_IDENTIFIER'])
    f_iri = DS_NS[fid]
    g.add((f_iri, RDF.type, GEO.Feature))
    geom = BNode()
    g.add((geom, RDF.type, GEO.Geometry))
    g.add((geom, GEO.asWKT, Literal(row['geometry'].wkt, datatype=GEO.wktLiteral)))
    g.add((f_iri, GEO.hasGeometry, geom))
    g.add((f_iri, SDO.additionalType, NVIS_VEG_NS[str(row['MVG_NUMBER']).zfill(4)]))
    g.add((f_iri, SDO.additionalType, NVIS_VEG_NS["1" + str(row['MVS_NUMBER']).zfill(3)]))

    g.add((f_iri, SDO.name, Literal(f"NVIS ACT Area {fid}")))

    g.add((fc, RDFS.member, f_iri))
    g.add((f_iri, SDO.isPartOf, fc))
    print(index)
    # if index >= 1000:
    #     break
print("END")
g.serialize(destination="nvis-act-all.ttl", format="turtle")


# print(gdf_flat.loc[gdf_flat['MVS_NUMBER'] == 32][['MVG_NUMBER']])