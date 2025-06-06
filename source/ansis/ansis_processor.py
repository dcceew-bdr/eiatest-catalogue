import json
from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import GEO, PROV, RDF, RDFS, SDO
from _ANSIS import ANSIS
from pathlib import Path

D = Namespace("https://linked.data.gov.au/dataset/eiatest/ansis/")
TERN = Namespace("https://w3id.org/tern/ontologies/tern/")

lu_sid_authorities = {
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

def make_quantity_value(g, value, unit) -> BNode:
    qv = BNode()
    g.add((qv, RDF.type, SDO.QuantitativeValue))
    g.add((qv, SDO.value, Literal(value)))
    g.add((qv, SDO.unitCode, make_iri(unit)))
    return qv

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
    "vegetables/flowers": URIRef("https://linked.data.gov.au/def/alum/3.4"),
    "quarry/mining": URIRef("https://linked.data.gov.au/def/alum/5.8"),
}

if __name__ == "__main__":
    g = Graph()

    fc = URIRef("https://linked.data.gov.au/dataset/eiatest/ansis/SoilSites")

    for f in Path(__file__).parent.glob("3c*.json"):
        data = json.load(open(f))

        for d in data["data"]:
            #
            # Values
            #

            # IRI
            id = d["id"]

            # disturbance
            disturbances = d.get("disturbance", None)
            disturbance_values = []
            if disturbances is not None:
                for disturbance in disturbances:
                    disturbance_values.append(disturbance["result"])

            # elevation
            elevations = d.get("elevation", None)
            elevation_values = []
            if elevations is not None:
                for elevation in elevations:
                    elevation_values.append(elevation["result"]["value"])

            # geometry
            wkt = d["geometry"]["result"].replace("SRID=4283;", "")

            # land use
            land_uses = d.get("landUse", None)
            land_use_values = []
            if land_uses is not None:
                for land_use in land_uses:
                    land_use_values.append(land_use["result"]["value"])

            # scoped identifier
            sid = d["scopedIdentifier"][0]["value"]
            sid_authority = d["scopedIdentifier"][0]["authority"]

            # site visit
            site_visits = d.get("siteVisit", None)
            outcrop_types = []
            runoff_type = None
            soil_profile_types = []
            if site_visits:
                for site_visit in site_visits:
                    # land surfaces
                    land_surface = site_visit.get("landSurface", None)
                    if land_surface is not None:
                        outcrop =  land_surface.get("outcrop", None)
                        if outcrop is not None:
                            outcrop_types.append(outcrop[0]["abundance"]["result"])
                        runoff = land_surface.get("runoff", None)
                        if runoff is not None:
                            runoff_type = runoff["result"]

                    # soil profiles
                    soil_profiles = site_visit.get("soilProfile", None)
                    if soil_profiles is not None:
                        for soil_profile in soil_profiles:
                            classifications_values = []
                            depth_value = None
                            drainage_value = None
                            permeability_value = None
                            substrate_value = None

                            # classification
                            classifications = soil_profile.get("classifications", None)
                            if classifications is not None:
                                for classification in classifications:
                                    classifications_values.append(classification["result"]["value"])

                            # depth
                            depth = soil_profile.get("depth", None)
                            if depth is not None:
                                depth_value = depth["result"]["value"]
                                                            
                            # drainage
                            drainage = soil_profile.get("drainage", None)
                            if drainage is not None:
                                drainage_value = drainage["result"]
                                
                            # permeability
                            permeability = soil_profile.get("permeability", None)
                            if permeability is not None:
                                permeability_value = permeability["result"]

                            # soil layers
                            # not done

                            # substrate
                            substrate = soil_profile.get("substrate", None)
                            if substrate is not None:
                                substrate_value = substrate["lithology"]["result"]

                            soil_profile_types.append((classifications_values, depth_value, drainage_value, permeability_value, substrate_value))

            #
            # RDF
            #

            # IRI
            iri = URIRef(D + id)
            g.add((iri, RDF.type, ANSIS.SoilSite))
            g.add((iri, RDF.type, GEO.Feature))
            g.add((iri, SDO.isPartOf, fc))
            g.add((fc, SDO.hasPart, iri))

            # disturbance
            for disturbance_value in disturbance_values:
                g.add((iri, ANSIS.disturbance, make_iri(disturbance_value)))

            # elevation
            for elevation_value in elevation_values:
                elev = make_quantity_value(g, elevation_value, "unit:M")
                g.add((iri, ANSIS.elevation, elev))

            # geometry
            geom = BNode()
            g.add((iri, GEO.hasGeometry, geom))
            g.add((geom, RDF.type, GEO.Geometry))
            g.add((geom, GEO.asWKT, Literal(wkt, datatype=GEO.wktLiteral)))

            # land use
            for land_use_value in land_use_values:
                lu = lu_land_uses[land_use_value]
                if lu is not None:
                    g.add((iri, ANSIS.hasLandUse, lu))

            # scoped identifier
            g.add((iri, SDO.identifier, Literal(sid, datatype=lu_sid_authorities[sid_authority])))

            # site visit
            # land surfaces
            for site_visit_value in site_visits:
                for outcrop_type in outcrop_types:
                    g.add((iri, ANSIS.hasOutcrop, make_iri(outcrop_type)))

                if runoff_type is not None:
                    g.add((iri, ANSIS.runoff, make_iri(runoff_type)))

                # soil profiles
                for soil_profile_type in soil_profile_types:
                    sp = BNode()
                    g.add((iri, ANSIS.relatedProfile, sp))

                    # classification
                    for classification_value in soil_profile_type[0]:
                        g.add((sp, ANSIS.classification, make_iri(classification_value)))
                    # depth
                    if soil_profile_type[1] is not None:
                        g.add((sp, ANSIS.depth, make_quantity_value(g, soil_profile_type[1], "unit:CentiM")))
                    # drainage
                    if soil_profile_type[2] is not None:
                        g.add((sp, ANSIS.drainage, make_iri(soil_profile_type[2])))
                    # permeability
                    if soil_profile_type[3] is not None:
                        g.add((sp, ANSIS.permeability, make_iri(soil_profile_type[3])))
                    # substrate
                    if soil_profile_type[4] is not None:
                        g.add((sp, ANSIS.hasSubstrate, make_iri(soil_profile_type[4])))

        for k, v in ansis_namespaces.items():
            g.bind(k, v)
        g.bind("tern", TERN)
        g.bind("alum", "https://linked.data.gov.au/def/alum/")
        g.bind("ss", "https://linked.data.gov.au/dataset/eiatest/ansis/SoilSites")
        g.bind("ansisdata", "https://linked.data.gov.au/dataset/eiatest/ansis/")


g.serialize(destination="ansis-data.ttl", format="turtle")