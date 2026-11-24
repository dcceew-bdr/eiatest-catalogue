"""Refresh or check the catalogue's selected TDWG label cache."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from urllib.request import Request, urlopen

from rdflib import Graph, Literal, Namespace, RDFS, URIRef

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[1] / "resources/background/labels/dwc.ttl"
SNAPSHOT = HERE / "snapshot.json"
NAME = URIRef("https://schema.org/name")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
SOURCES = {
    "core": "https://rs.tdwg.org/dump/terms.ttl",
    "organizedInClass": "https://rs.tdwg.org/dwc/terms/attributes/organizedInClass.ttl",
    "status": "https://rs.tdwg.org/dwc/terms/attributes/status.ttl",
}


def render(labels):
    lines = ['PREFIX schema: <https://schema.org/>', '']
    for iri, value in sorted(labels.items()):
        label = Literal(value["value"], lang=value["language"])
        lines.append(f"<{iri}> schema:name {label.n3()} .")
    return ("\n".join(lines) + "\n").encode()


def candidate(terms):
    g, artifacts = Graph(), {}
    for key, url in SOURCES.items():
        with urlopen(Request(url, headers={"Accept": "text/turtle"}), timeout=60) as response:
            data = response.read()
            g += Graph().parse(data=data, format="turtle")
            artifacts[key] = {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                              "sha256": hashlib.sha256(data).hexdigest()}
    labels = {}
    for term in sorted(terms):
        choices = []
        for predicate in (SKOS.prefLabel, RDFS.label):
            values = list(g.objects(URIRef(term), predicate))
            choices = [v for v in values if isinstance(v, Literal) and v.language == "en"]
            if not choices:
                choices = [v for v in values if isinstance(v, Literal) and not v.language]
            if choices:
                break
        if len(set(choices)) != 1:
            raise ValueError(f"Missing or ambiguous English label: {term}")
        label = choices[0]
        labels[term] = {"value": str(label), "language": label.language}
    return {"sources": artifacts, "labels": labels}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "refresh"))
    parser.add_argument("--online", action="store_true")
    args = parser.parse_args()
    current = json.loads(SNAPSHOT.read_text()) if SNAPSHOT.exists() else None
    if args.command == "check":
        if current is None or OUTPUT.read_bytes() != render(current["labels"]):
            raise ValueError("Cached labels do not match the recorded source labels")
        if args.online:
            upstream = candidate(current["labels"])
            changed = [term for term in current["labels"] if current["labels"][term] != upstream["labels"][term]]
            print(json.dumps({"changed_labels": changed}, indent=2))
            return 1 if changed else 0
        print(f"Verified {len(current['labels'])} recorded TDWG labels")
        return 0
    terms = set(str(s) for s in Graph().parse(OUTPUT).subjects(NAME, None))
    if current is not None and terms != set(current["labels"]):
        raise ValueError("Term selection changed; review the selected label set before refreshing")
    snapshot = candidate(terms)
    SNAPSHOT.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n")
    OUTPUT.write_bytes(render(snapshot["labels"]))
    print(f"Refreshed {len(terms)} labels; term IRIs and schema:name predicate preserved")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"DwC label check failed: {exc}", file=sys.stderr)
        sys.exit(2)
