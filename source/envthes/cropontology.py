iris = [
    "https://cropontology.org/rdf/CO_357:0000007" ,
    "https://cropontology.org/rdf/CO_357:0000022" ,
    "https://cropontology.org/rdf/CO_357:0000048" ,
    "https://cropontology.org/rdf/CO_357:0000085" ,
    "https://cropontology.org/rdf/CO_357:0000086" ,
    "https://cropontology.org/rdf/CO_357:0000101" ,
    "https://cropontology.org/rdf/CO_357:0000111" ,
    "https://cropontology.org/rdf/CO_357:0000113" ,
    "https://cropontology.org/rdf/CO_357:0000133" ,
    "https://cropontology.org/rdf/CO_357:0000151" ,
    "https://cropontology.org/rdf/CO_357:0000159" ,
    "https://cropontology.org/rdf/CO_357:0000242" ,
    "https://cropontology.org/rdf/CO_357:0000245" ,
    "https://cropontology.org/rdf/CO_357:0000249" ,
    "https://cropontology.org/rdf/CO_357:0000250" ,
    "https://cropontology.org/rdf/CO_357:0000251" ,
    "https://cropontology.org/rdf/CO_357:0000255" ,
    "https://cropontology.org/rdf/CO_357:0000257" ,
    "https://cropontology.org/rdf/CO_357:0000268" ,
    "https://cropontology.org/rdf/CO_357:0000273" ,
    "https://cropontology.org/rdf/CO_357:0000281" ,
    "https://cropontology.org/rdf/CO_357:0000287" ,
    "https://cropontology.org/rdf/CO_357:0000289" ,
    "https://cropontology.org/rdf/CO_357:0000304" ,
    "https://cropontology.org/rdf/CO_357:0000429" ,
    "https://cropontology.org/rdf/CO_357:0000454" ,
    "https://cropontology.org/rdf/CO_357:0000455" ,
    "https://cropontology.org/rdf/CO_357:0000512" ,
    "https://cropontology.org/rdf/CO_357:0000513" ,
    "https://cropontology.org/rdf/CO_357:0000514" ,
    "https://cropontology.org/rdf/CO_357:0000515" ,
    "https://cropontology.org/rdf/CO_357:0000516" ,
    "https://cropontology.org/rdf/CO_357:0000518" ,
    "https://cropontology.org/rdf/CO_357:0000519" ,
    "https://cropontology.org/rdf/CO_357:0000524" ,
    "https://cropontology.org/rdf/CO_357:0000526" ,
    "https://cropontology.org/rdf/CO_357:0000527" ,
    "https://cropontology.org/rdf/CO_357:0000532" ,
    "https://cropontology.org/rdf/CO_357:0000534" ,
    "https://cropontology.org/rdf/CO_357:0000535" ,
    "https://cropontology.org/rdf/CO_357:0000536" ,
    "https://cropontology.org/rdf/CO_357:0000539" ,
]
from rdflib import Graph, Literal

g = Graph()
# for iri in iris:
#     g.parse(iri, format="xml")
#     print(len(g))
#
# g.serialize(destination="cropontology-labels.ttl", format="longturtle")

g.parse("cropontology-labels.ttl")

q = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX schema: <https://schema.org/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    
    CONSTRUCT {
      ?c schema:name ?l_str .
    }
    WHERE {
      ?c rdfs:label ?l .
      
      BIND (CONCAT("Crop Ontology: ", STR(?l)) AS ?l_str)
      
      FILTER (LANG(?l) = "en")
    }
    """

g.query(q).serialize(destination="co-labels.ttl", format="turtle")
