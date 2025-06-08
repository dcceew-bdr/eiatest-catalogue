# extracts labels for all LTER terms in the LTER vocab TSV dump archived at https://github.com/lter/vocab/blob/master/sssom/lter-envo.sssom.tsv
import csv
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, SDO

g = Graph()
with open("lter-vocab.tsv") as f:
    data = csv.reader(f, delimiter="\t")
    data.__next__()
    for line in data:
        iri = URIRef(line[0].replace("LTER:", "https://vocab.lternet.edu/vocab/vocab/?tema="))
        lbl = Literal(line[1])
        g.add((iri, SDO.name, lbl))
g.serialize("lter-vocab.ttl", format="longturtle")