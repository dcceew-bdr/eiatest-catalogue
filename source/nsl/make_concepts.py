from pathlib import Path

p = Path(__file__).parent.parent.resolve().parent / "resources/datasets/non-spatial/nsl.ttl"
with open(p) as f:
    tcs = []
    doc_new = ""
    for line in f:
        if line.startswith(":"):
            parts = line.split("#")

            tcs.append(parts[0])
            doc_new += parts[0]
            doc_new += "\n"
            doc_new += "\ta skos:Concept ;\n"
            doc_new += "\trdfs:isDefinedBy cs: ;\n"
            doc_new += "\tskos:definition \"" + parts[1].strip() + "\"@en ;\n"
            doc_new += "\tskos:inScheme cs: ;\n"
            doc_new += "\tskos:prefLabel \"" + parts[1].strip() + "\"@en ;\n"
            doc_new += "\tskos:topConceptOf cs: ;\n"
            doc_new += ".\n\n"
        else:
            doc_new += line
    doc_new += "\n\n"

    doc_new += "\n".join(f"\t{x} ," for x in tcs)
    Path(p.with_suffix(".2.ttl")).write_text(doc_new)