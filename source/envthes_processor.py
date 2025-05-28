from rdflib import Graph, Literal
from rdflib.namespace import RDF, SKOS


g = Graph().parse("resources/vocabs/envthes.ttl")

# for s in g.subjects(RDF.type, SKOS.Concept):
#     g.remove((s, SKOS.historyNote, None))
#     g.add((s, SKOS.historyNote, Literal("Small annotations changed from original for the BDR")))
#     for o in g.objects(s, SKOS.prefLabel):
#         if o.language != "en":
#             g.remove((s, SKOS.prefLabel, o))
#             g.add((s, SKOS.altLabel, o))
#
# for s in g.subjects(RDF.type, SKOS.Concept):
#     if g.value(s, SKOS.definition) is None:
#         g.add((s, SKOS.definition, g.value(s, SKOS.prefLabel)))
#
# g.serialize("resources/envthes.2.ttl", format="turtle")

for s in g.subjects(RDF.type, SKOS.Concept):
    if not g.value(s, SKOS.inScheme, None):
        print(s)

for s in g.subjects(SKOS.broader, None):
    if not g.value(s, SKOS.inScheme, None):
        print(s)

for s in g.subjects(SKOS.narrower, None):
    if not g.value(s, SKOS.inScheme, None):
        print(s)