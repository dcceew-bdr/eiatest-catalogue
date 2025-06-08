from urllib.parse import quote_plus
import httpx

terms = [
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
]

for term in terms:
    pid_encoded = quote_plus(term)
    url = f"https://data.bioontology.org/ontologies/CRISP/classes/{pid_encoded}?display=all&apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb"
    r = httpx.get(url)

    if r.is_success:
        print(f'<{term}> schema:name "{r.json()["prefLabel"]}" .')