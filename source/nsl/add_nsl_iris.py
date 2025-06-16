import csv
from pathlib import Path
from rdflib import Graph, RDF, SKOS, URIRef, Namespace
DWC = Namespace("http://rs.tdwg.org/dwc/terms/")
EX = Namespace("http://example.com/")

nsl_dataset = Path(__file__).parent.parent.resolve().parent / "resources/datasets/non-spatial/nsl.ttl"
bdr_act_dataset = Path(__file__).parent.parent.resolve().parent / "resources/datasets/spatial/bdr-act.ttl"
apd_nsl_act_dataset = Path(__file__).parent.parent.resolve().parent / "resources/datasets/non-spatial/apd-nsl.ttl"
name_match_tsv = Path(__file__).parent / "name_match.tsv"

names = {}
with open(name_match_tsv) as f:
    data = csv.reader(f, delimiter='\t')
    data.__next__()
    for row in data:
        names[URIRef("https://linked.data.gov.au/dataset/eiatest/nsl/" + row[1].replace(":", ""))] = URIRef(row[3])

g = Graph().parse(apd_nsl_act_dataset)

# # nsl.ttl
# for s in g.subjects(RDF.type, SKOS.Concept):
#     n = names.get(s)
#     if n is not None:
#         for p, o in g.predicate_objects(s):
#             g.remove((s, p, o))
#             g.add((n, p, o))
#         for s2, p2 in g.subject_predicates(s):
#             g.remove((s2, p2, s))
#             g.add((s2, p2, n))

# # bdr-act.ttl
# for s, o in g.subject_objects(DWC.scientificNameID):
#     n = names.get(o)
#     if n is not None:
#         g.remove((s, DWC.scientificNameID, o))
#         g.add((s, DWC.scientificNameID, n))

# # apd-nsl.ttl
for s, o in g.subject_objects(EX.exhibitorOfTrait):
    n = names.get(o)
    if n is not None:
        g.remove((s, EX.exhibitorOfTrait, o))
        g.add((s, EX.exhibitorOfTrait, n))

# # # g.bind("dwc", "http://rs.tdwg.org/dwc/terms/")
g.serialize(destination=apd_nsl_act_dataset.with_suffix(".2.ttl"), format="longturtle")

