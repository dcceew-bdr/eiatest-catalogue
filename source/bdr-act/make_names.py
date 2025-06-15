from pathlib import Path

p = Path(__file__).parent.parent.resolve().parent / "resources/datasets/spatial/bdr-act.ttl"
with open(p) as f:
    doc_new = ""
    for line in f.readlines():
        if line.startswith("    dwc:scientificNameID"):
            parts = line.split("\"")
            rep = parts[1].strip().replace(" ", "-").replace(".", "").lower()
            iri = "nsl:" + rep
            line_new = parts[0] + iri + parts[2]
            doc_new += line_new
        else:
            doc_new += line
    Path(p.with_suffix(".2.ttl")).write_text(doc_new)