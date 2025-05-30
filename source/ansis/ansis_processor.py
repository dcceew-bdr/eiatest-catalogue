import json
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import PROV, RDF, RDFS, SDO
from _ANSIS import ANSIS
from pathlib import Path

D = Namespace("https://linked.data.gov.au/dataset/eiatest/ansis/")
TERN = Namespace("https://w3id.org/tern/ontologies/tern/")

lu_authorities = {
    "NSW Govt": URIRef("https://linked.data.gov.au/org/nsw"),
    "CSIRO": URIRef("https://linked.data.gov.au/org/csiro"),
}


ansis_namespaces = {
    "ansis":    "https://anzsoil.org/def/au/domain/",
    "asc":      "http://anzsoil.org/def/au/asc/",
    "asls":     "https://anzsoil.org/def/au/domain/asls-code/",
    "doi":      "https://doi.org/",
    "geo":      "http://www.opengis.net/ont/geosparql#",
    "lf":       "http://anzsoil.org/def/au/asls/landform/",
    "ls":       "http://anzsoil.org/def/au/asls/land-surface/",
    "nil":      "http://www.opengis.net/def/nil/OGC/0/",
    "prop":     "https://anzsoil.org/def/au/property/",
    "prov":     "http://www.w3.org/ns/prov#",
    "proj":     "https://linked.data.gov.au/def/project#",
    "scm":      "http://anzsoil.org/def/au/scm/",
    "sosa":     "http://www.w3.org/ns/sosa/",
    "sp":       "http://anzsoil.org/def/au/asls/soil-profile/",
    "subst":    "http://anzsoil.org/def/au/asls/substrate/",
    "qudt":     "http://qudt.org/schema/qudt/",
    "spmile":   "http://anzsoil.org/def/au/spm/spmile/",
    "unit":     "https://qudt.org/2.1/vocab/unit/",
}

def make_iri(value):
    prefix, val = value.split(":")
    namespace = ansis_namespaces.get(prefix)
    return URIRef(f"{namespace}{val}")
    

lu_land_uses = {
    "National/State Parks": URIRef("https://linked.data.gov.au/def/alum/1.1.3"),
    "improved pasture": URIRef("https://linked.data.gov.au/def/alum/3.2"),
    "softwood plantation": URIRef("https://linked.data.gov.au/def/alum/3.1.2"),
    "timber/scrub/unused": URIRef("https://linked.data.gov.au/def/alum/1.3"),
    "volun./native pasture": URIRef("https://linked.data.gov.au/def/alum/2.1"),
    "other": None,
    "orchards/vineyards": URIRef("https://linked.data.gov.au/def/alum/3.4"),
    "cropping": URIRef("https://linked.data.gov.au/def/alum/3.3"),
    "logged native forest": URIRef("https://linked.data.gov.au/def/alum/2.2"),
    "urban": URIRef("https://linked.data.gov.au/def/alum/5.4"),
}

if __name__ == "__main__":
    g = Graph()

    for f in Path(__file__).parent.glob("3c*.json"):
        data = json.load(open(f))

        for d in data["data"]:
            id = d["scopedIdentifier"][0]["value"]
            iri = URIRef(D + id)

            id_authority = d["scopedIdentifier"][0]["authority"]

            wkt = d["geometry"]["result"].replace("SRID=4283;", "")

            disturbances = d.get("disturbance", None)
            if disturbances:
                for disturbances in disturbances:
                    g.add((iri, ANSIS.disturbance, make_iri(disturbances["result"])))

            land_uses = d.get("landUse", None)
            if land_uses:
                for land_use in land_uses:
                    lu = lu_land_uses.get(land_use["result"]["value"])

                    if lu:
                        g.add((iri, ANSIS.hasLandUse, lu))
                    else:
                        print(land_use["result"]["value"])
            #
            # site_visits = d.get("siteVisit", None)
            #
            #
            #
            # site_visit = d["siteVisit"][0]["endedAtTime"]
            #
            # soil_profile_classification = d["siteVisit"][0]["soilProfile"][0]["classification"][0]["result"]["value"]
            # soil_profile_depth = d["siteVisit"][0]["soilProfile"][0]["depth"]["result"]["value"]

            g.add((iri, RDF.type, ANSIS.SoilSite))
            g.add((iri, RDF.type, TERN.Site))
            g.add((iri, PROV.wasAttributedTo, lu_authorities[id_authority]))

        for k, v in ansis_namespaces.items():
            g.bind(k, v)

print(g.serialize(format="turtle"))