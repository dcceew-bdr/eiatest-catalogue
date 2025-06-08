from urllib.parse import quote_plus
import httpx

terms = [
    "http://purl.bioontology.org/NEMO/ontology/NEMO.owl#NEMO_3768000" ,
    "http://purl.bioontology.org/NEMO/ontology/NEMO.owl#NEMO_8906000" ,
    "http://purl.bioontology.org/ontology/CSP/0074-5454" ,
    "http://purl.bioontology.org/ontology/CSP/0467-2841" ,
    "http://purl.bioontology.org/ontology/CSP/0604-0425" ,
    "http://purl.bioontology.org/ontology/CSP/0632-5038" ,
    "http://purl.bioontology.org/ontology/CSP/1035-8189" ,
    "http://purl.bioontology.org/ontology/CSP/1354-4287" ,
    "http://purl.bioontology.org/ontology/CSP/2253-9046" ,
    "http://purl.bioontology.org/ontology/CSP/2340-7524" ,
    "http://purl.bioontology.org/ontology/CSP/2340-8793" ,
    "http://purl.bioontology.org/ontology/CSP/2341-3000" ,
    "http://purl.bioontology.org/ontology/CSP/2683-4779" ,
    "http://purl.bioontology.org/ontology/CSP/4000-0286" ,
    "http://purl.bioontology.org/ontology/CSP/4001-0048" ,
    "http://purl.bioontology.org/ontology/CSP/5002-0017" ,
    "http://purl.bioontology.org/ontology/CSP/5004-0025" ,
    "http://purl.bioontology.org/ontology/MESH/D000068098" ,
    "http://purl.bioontology.org/ontology/MESH/D000071421" ,
    "http://purl.bioontology.org/ontology/MESH/D001467" ,
    "http://purl.bioontology.org/ontology/MESH/D001947" ,
    "http://purl.bioontology.org/ontology/MESH/D002980" ,
    "http://purl.bioontology.org/ontology/MESH/D005740" ,
    "http://purl.bioontology.org/ontology/MESH/D006790" ,
    "http://purl.bioontology.org/ontology/MESH/D006859" ,
    "http://purl.bioontology.org/ontology/MESH/D008962" ,
    "http://purl.bioontology.org/ontology/MESH/D009032" ,
    "http://purl.bioontology.org/ontology/MESH/D009587" ,
    "http://purl.bioontology.org/ontology/MESH/D010103" ,
    "http://purl.bioontology.org/ontology/MESH/D012273" ,
    "http://purl.bioontology.org/ontology/MESH/D012399" ,
    "http://purl.bioontology.org/ontology/MESH/D012641" ,
    "http://purl.bioontology.org/ontology/MESH/D013025" ,
    "http://purl.bioontology.org/ontology/MESH/D013718" ,
    "http://purl.bioontology.org/ontology/MESH/D013995" ,
    "http://purl.bioontology.org/ontology/MESH/D015331" ,
    "http://purl.bioontology.org/ontology/MESH/D018481" ,
    "http://purl.bioontology.org/ontology/MESH/D018895" ,
    "http://purl.bioontology.org/ontology/MESH/D019245" ,
    "http://purl.bioontology.org/ontology/MESH/D020304" ,
    "http://purl.bioontology.org/ontology/MESH/D033342" ,
    "http://purl.bioontology.org/ontology/MESH/D052918" ,
    "http://purl.bioontology.org/ontology/MESH/D054750" ,
    "http://purl.bioontology.org/ontology/MESH/D057075" ,
    "http://purl.bioontology.org/ontology/MESH/D058865" ,
    "http://purl.bioontology.org/ontology/MESH/D059000" ,
    "http://purl.bioontology.org/ontology/MESH/D061005" ,
    "http://purl.bioontology.org/ontology/MESH/D011156" ,
    "http://purl.bioontology.org/ontology/NCIM/C0311420" ,
    "http://purl.bioontology.org/ontology/npo#NPO_1407" ,
    "http://purl.bioontology.org/ontology/npo#NPO_1802" ,
    "http://purl.bioontology.org/ontology/npo#NPO_199" ,
    "http://purl.bioontology.org/ontology/npo#NPO_669" ,
]

for term in terms:
    pid_encoded = quote_plus(term)
    url = f"https://data.bioontology.org/ontologies/MESH/classes/{pid_encoded}?display=all&apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb"
    r = httpx.get(url)

    if r.is_success:
        print(f'<{term}> schema:name {r.json()["prefLabel"]} .')