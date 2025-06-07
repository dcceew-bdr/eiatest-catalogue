from rdflib import Graph, Literal, RDF, SKOS

g = Graph().parse("asls-soil-profile.ttl")

# for s in g.subjects(RDF.type, SKOS.Concept):
#     if not g.value(subject=s, predicate=SKOS.definition):
#         l = g.value(subject=s, predicate=SKOS.prefLabel)
#         print(f"sp:{s} skos:definition \"{l}\"@en .")

# for s in g.subjects(RDF.type, SKOS.Concept):
#     if not g.value(subject=s, predicate=SKOS.inScheme):
#         c = str(s).replace("http://anzsoil.org/def/au/asls/soil-profile/", "sp:")
#         c = c.replace("http://anzsoil.org/def/au/asls/substrate/", "subst:")
#         c = c.replace("http://anzsoil.org/def/au/asls/land-surface/", "ls:")
#         print(f"{c} rdfs:isDefinedBy asls:soil-profile .")
#         print(f"{c} skos:inScheme asls:soil-profile .")

for s in g.subjects(RDF.type, SKOS.Concept):
    if not g.value(subject=s, predicate=SKOS.broader):
        c = str(s).replace("http://anzsoil.org/def/au/asls/soil-profile/", "sp:")
        c = c.replace("http://anzsoil.org/def/au/asls/substrate/", "subst:")
        c = c.replace("http://anzsoil.org/def/au/asls/land-surface/", "ls:")
        print(f"{c} skos:topConceptOf asls:soil-profile .")
        print(f"asls:soil-profile skos:hasTopConcept {c} .")