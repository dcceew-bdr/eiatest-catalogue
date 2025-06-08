from urllib.parse import quote_plus
import httpx

terms = [
    "http://purl.dataone.org/odo/ECSO_00000018" ,
    "http://purl.dataone.org/odo/ECSO_00000021" ,
    "http://purl.dataone.org/odo/ECSO_00000037" ,
    "http://purl.dataone.org/odo/ECSO_00000310" ,
    "http://purl.dataone.org/odo/ECSO_00000326" ,
    "http://purl.dataone.org/odo/ECSO_00000549" ,
    "http://purl.dataone.org/odo/ECSO_00000572" ,
    "http://purl.dataone.org/odo/ECSO_00000619" ,
    "http://purl.dataone.org/odo/ECSO_00000669" ,
    "http://purl.dataone.org/odo/ECSO_00001127" ,
    "http://purl.dataone.org/odo/ECSO_00001142" ,
    "http://purl.dataone.org/odo/ECSO_00001160" ,
    "http://purl.dataone.org/odo/ECSO_00001164" ,
    "http://purl.dataone.org/odo/ECSO_00001203" ,
    "http://purl.dataone.org/odo/ECSO_00001229" ,
    "http://purl.dataone.org/odo/ECSO_00001231" ,
    "http://purl.dataone.org/odo/ECSO_00001234" ,
    "http://purl.dataone.org/odo/ECSO_00001671" ,
    "http://purl.dataone.org/odo/ECSO_00001677" ,
    "http://purl.dataone.org/odo/ECSO_00001704" ,
    "http://purl.dataone.org/odo/ECSO_00001737" ,
    "http://purl.dataone.org/odo/ECSO_00001738" ,
    "http://purl.dataone.org/odo/ECSO_00001740" ,
    "http://purl.dataone.org/odo/ECSO_00002703" ,
    "http://purl.dataone.org/odo/ECSO_00002723" ,
]

for term in terms:
    pid_encoded = quote_plus(term)
    url = f"https://data.bioontology.org/ontologies/ECSO/classes/{pid_encoded}?display=all&apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb"
    r = httpx.get(url)

    if r.is_success:
        print(f'<{term}> schema:name "{r.json()["prefLabel"]}" .')