from rdflib import Graph, Literal
from rdflib.namespace import RDF, SKOS


g = Graph().parse("resources/vocabs/envthes.ttl")

cs = []
for s in g.subjects(RDF.type, SKOS.Concept):
    cs.append(str(s))

with open("envthes_concepts.txt", "w") as f:
    for c in sorted(cs):
        f.write("<" + c + "> ,\n")

print("finished")