from rdflib import Graph
from pyshacl import validate
from pathlib import Path

# load all labels into data_graph
ref_graph = Graph()
for f in Path(Path(__file__).parent.parent.resolve() / "background").glob("*.ttl"):
    ref_graph.parse(f)

print("loaded labels")

# validate each data file in turn
for f in Path(Path(__file__).parent.parent.resolve() / "resources/datasets").glob("*.ttl"):
    data_graph = Graph().parse(f)
    data_graph +=  ref_graph

    print(f)
    shapes_graph = Graph().parse("validator-geosparql.ttl")
    shapes_graph.parse("../../loci-data-profile/validator.ttl")
    shapes_graph.parse("../../eia-data-profile/validator.ttl")
    v = validate(data_graph, shacl_graph=shapes_graph)

    if not v[0]:
        print(v[2])
        break
    else:
        print("valid")
