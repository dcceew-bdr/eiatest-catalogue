# Selected Darwin Core labels

`../../resources/background/labels/dwc.ttl` (relative to the repository root: `resources/background/labels/dwc.ttl`) is a selected label cache for Prez, not a Darwin Core schema. The generator preserves the selected IRIs and the consumer's `schema:name` predicate, using current TDWG English preferred labels (or English RDFS labels as a fallback).

`snapshot.json` records the selected upstream label values, language tags, source URLs, UTC retrieval times and SHA-256 hashes of the source responses. The core labels come from `https://rs.tdwg.org/dump/terms.ttl`; the two utility properties are retrieved from their own TDWG term documents. This includes the utility terms absent from the core-term dump.

From a repository Python environment with its declared RDFLib dependency installed:

```sh
python source/dwc-labels/sync.py check
python source/dwc-labels/sync.py check --online
python source/dwc-labels/sync.py refresh
```

The offline check reproduces the label file from recorded values. The online check compares the selected labels with upstream and exits `1` for drift, without updating files. Unrelated upstream terms and serialization changes do not affect this selected-label cache. An explicit refresh updates the labels and provenance together after successful downloads and label resolution; review both files before committing. Exit `2` indicates an error.

For the complete core-term snapshot, dated release metadata, historical term comparisons and weekly upstream checking, see the ABIS repository's `schemas/background/dwc-metadata/README.md`. Its full dump is independently pinned there. This catalogue's compact snapshot stores only selected label values and response hashes; retrieving the original source bytes requires the upstream publication or the recorded ABIS snapshot when its hash matches.

If needed on the workspace Mac, configure trusted system CAs with `SSL_CERT_FILE=/etc/ssl/cert.pem`; never disable TLS verification.
