import csv
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, SDO

g = Graph().parse("quantitykind.ttl")
q = """
    PREFIX quantitykind: <http://qudt.org/vocab/quantitykind/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX schema: <https://schema.org/>

    CONSTRUCT {
        ?c schema:name ?l_nolang
    }
    WHERE {
        ?c 
            a qudt:QuantityKind ;
            rdfs:label ?l ;
        .
        
        BIND (STR(?l) AS ?l_nolang)
        
        FILTER (LANG(?l) = "en")
    }
    """
g.query(q).serialize(destination="quantitykind-labels.ttl", format="turtle")