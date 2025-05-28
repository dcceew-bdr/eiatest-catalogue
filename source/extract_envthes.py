from pathlib import Path
from rdflib import Graph
from rdflib.namespace import SDO, SKOS


g = Graph().parse(Path(__file__).parent.parent.resolve().parent / "eiatest-catalogue/resources/reference/envthes.ttl")

g2 = Graph()

for s, o in g.subject_objects(SKOS.inScheme):
    g2.add((s, SKOS.inScheme, o))

for s, o in g.subject_objects(SKOS.prefLabel):
    g2.add((s, SDO.name, o))

for s, o in g.subject_objects(SKOS.definition):
    g2.add((s, SDO.description, o))

g2.bind("", "http://vocabs.lter-europe.net/EnvThes/")
g2.bind("cs", "http://vocabs.lter-europe.net/EnvThes")
g2.serialize(destination="envthes-labels.ttl", format="longturtle")