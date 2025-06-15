from rdflib import Graph, URIRef, RDFS

# go-basic.owl from https://geneontology.org/docs/download-ontology/
g = Graph().parse("go-basic.owl", format='xml')
print(len(g))

concepts = [
    "http://purl.obolibrary.org/obo/GO_0000003" ,
    "http://purl.obolibrary.org/obo/GO_0002164" ,
    "http://purl.obolibrary.org/obo/GO_0006833" ,
    "http://purl.obolibrary.org/obo/GO_0009399" ,
    "http://purl.obolibrary.org/obo/GO_0009505" ,
    "http://purl.obolibrary.org/obo/GO_0009507" ,
    "http://purl.obolibrary.org/obo/GO_0009521" ,
    "http://purl.obolibrary.org/obo/GO_0009539" ,
    "http://purl.obolibrary.org/obo/GO_0009579" ,
    "http://purl.obolibrary.org/obo/GO_0009760" ,
    "http://purl.obolibrary.org/obo/GO_0009761" ,
    "http://purl.obolibrary.org/obo/GO_0009845" ,
    "http://purl.obolibrary.org/obo/GO_0009856" ,
    "http://purl.obolibrary.org/obo/GO_0009877" ,
    "http://purl.obolibrary.org/obo/GO_0009900" ,
    "http://purl.obolibrary.org/obo/GO_0010162" ,
    "http://purl.obolibrary.org/obo/GO_0010228" ,
    "http://purl.obolibrary.org/obo/GO_0015979" ,
    "http://purl.obolibrary.org/obo/GO_0016265" ,
    "http://purl.obolibrary.org/obo/GO_0019253" ,
    "http://purl.obolibrary.org/obo/GO_0019684" ,
    "http://purl.obolibrary.org/obo/GO_0019685" ,
    "http://purl.obolibrary.org/obo/GO_0019954" ,
    "http://purl.obolibrary.org/obo/GO_0022900" ,
    "http://purl.obolibrary.org/obo/GO_0031099" ,
    "http://purl.obolibrary.org/obo/GO_0036377" ,
    "http://purl.obolibrary.org/obo/GO_0040007" ,
    "http://purl.obolibrary.org/obo/GO_0044403" ,
    "http://purl.obolibrary.org/obo/GO_0045333" ,
    "http://purl.obolibrary.org/obo/GO_0048492" ,
    "http://purl.obolibrary.org/obo/GO_0060756" ,
    "http://purl.obolibrary.org/obo/GO_0062074" ,
    "http://purl.obolibrary.org/obo/GO_0072519" ,
    "http://purl.obolibrary.org/obo/GO_0085030" ,
    "http://purl.obolibrary.org/obo/GO_0085035" ,
    "http://purl.obolibrary.org/obo/GO_0090406" ,
    "http://purl.obolibrary.org/obo/GO_0090546" ,
]

# concepts = [ "http://purl.obolibrary.org/obo/GO_0045333" ]

for concept in concepts:
    print(f'<{concept}> schema:name "{g.value(subject=URIRef(concept), predicate=RDFS.label)}" .')