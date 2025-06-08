import httpx

terms = [
    "C104788" ,
    "C112332" ,
    "C114082" ,
    "C119321" ,
    "C13445" ,
    "C14329" ,
    "C15222" ,
    "C16342" ,
    "C16410" ,
    "C17248" ,
    "C1751" ,
    "C18814" ,
    "C19142" ,
    "C25180" ,
    "C25208" ,
    "C25244" ,
    "C25245" ,
    "C25274" ,
    "C25285" ,
    "C25326" ,
    "C25336" ,
    "C25390" ,
    "C25429" ,
    "C25443" ,
    "C25496" ,
    "C25554" ,
    "C28359" ,
    "C38024" ,
    "C41167" ,
    "C41546" ,
    "C44476" ,
    "C45306" ,
    "C48919" ,
    "C48920" ,
    "C49287" ,
    "C53322" ,
    "C53414" ,
    "C53452" ,
    "C54154" ,
    "C54647" ,
    "C61372" ,
    "C61427" ,
    "C62103" ,
    "C62230" ,
    "C62254" ,
    "C62690" ,
    "C62695" ,
    "C63848" ,
    "C64657" ,
    "C68594" ,
    "C70827" ,
    "C72076" ,
]

for term in terms:
    print(term)
    url = f"https://evsexplore.semantics.cancer.gov/evsexplore/api/v1/concept/ncit/{term}?include=full&limit=100"
    pid = f"https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/{term}"
    r = httpx.get(url)
    name = r.json()["name"]
    print(name)
    open("../resources/background/labels/evs.ttl", "a").write(f"<{pid}> schema:name \"{name}\" .\n>")