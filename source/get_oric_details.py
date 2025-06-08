import httpx

orcids = [
    "https://orcid.org/0000-0001-5640-5910" ,
    "0000-0001-5728-9827" ,
    "0000-0001-5945-438X" ,
    "0000-0001-7328-345X" ,
    "0000-0001-8305-3236" ,
    "0000-0001-8338-9143" ,
    "0000-0001-9277-5142" ,
    "0000-0001-9353-0067" ,
    "0000-0002-0693-1899" ,
    "0000-0002-0712-5143" ,
    "0000-0002-0962-5117" ,
    "0000-0002-1773-6597" ,
    "0000-0002-3046-0417" ,
    "0000-0002-3767-2690" ,
    "0000-0002-4680-8115" ,
    "0000-0002-4964-6107" ,
    "0000-0002-6012-8458" ,
    "0000-0002-6033-2766" ,
    "0000-0002-8766-2829" ,
    "0000-0002-9105-640X" ,
    "0000-0002-9699-2272" ,
    "0000-0002-9843-6616" ,
    "0000-0003-0360-8321" ,
    "0000-0003-1116-9402" ,
    "0000-0003-2008-7062" ,
    "0000-0003-2120-0071" ,
    "0000-0003-3568-2606" ,
]

for orcid in orcids:
    orcid = orcid.replace("https://orcid.org/", "")

    response = httpx.get(
        f"https://pub.orcid.org/v3.0/{orcid}",
        headers={"Accept": "application/json"}
    )
    if response.is_success:
        j = response.json()
        given_name = j["person"]["name"]["given-names"]["value"]
        family_name = j["person"]["name"]["family-name"]["value"]
        template = \
"""
<https://orcid.org/{orcid}>
    a schema:Person ;
    schema:name "{name}" ;
    schema:email ""^^xsd:anyURI ;
.
"""
        print(template.format(orcid=orcid, name=given_name + " " + family_name))


