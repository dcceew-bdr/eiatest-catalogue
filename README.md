# EIA Test Catalogue

This catalogue was created in mid-2025 to showcase the integration of [Environment Information Australia (EIA)](https://www.dcceew.gov.au/environment/environment-information-australia) datasets.

The catalogue [lists test versions of major Australian environmental datasets](https://eia.testing.bdr.gov.au/catalogs/catalogue:eiatest-datasets/collections) within EIA's scope. It also lists [models](https://eia.testing.bdr.gov.au/catalogs/catalogue:eiatest-models/collections) and [vocabularies](https://eia.testing.bdr.gov.au/catalogs/catalogue:eiatest-vocabs/collections) needed to support the integration of the datasets.

The catalogue tool also provides the [EIA Scenario Demonstrator](https://eia.testing.bdr.gov.au/eia-demo) which describes a series of data discovery scenarios that show off different aspects of the dataset's integration using [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web) and [Knowledge Graph](https://en.wikipedia.org/wiki/Knowledge_graph) methods.


The enterprise data model - a "Supermodel" - within which all elements of this catalogue are positioned is online at:

* **<https://linked.data.gov.au/def/eia-supermodel>**

## License & Rights

The contents of this catalogue, and of the individual dataset within it, are made available for reuse according to Australian government standard practice under the [Creative Commons BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), a copy of the deed of which is contained in this repository in the `LICENSE` file.

_Note that not all the content of all the datasets listed in this catalogue is publicly available: some of it is protected due to environmental or legal sensitivities._

All this work is copyright as follows:

&copy; Department of Climate Change, Energy, the Environment and Water 2025

## Contact

*contact:*  
[Biodiversity Data Repository Team](https://www.dcceew.gov.au/environment/environment-information-australia/biodiversity-data-repository)  
<bdr@dcceew.gov.au>

*publisher:*  
Environment Information Australia  
[Department of Climate Change, Energy, the Environment and Water](https://www.dcceew.gov.au)  
<eia.feedback@dcceew.gov.au>

*creator:*  
[KurrawongAI](https://kurrawong.ai)  
<info@kurrawong.ai>  
<https://orcid.org/0000-0002-8742-7730>

## Catalogue Resources

| Resource                                                                                                                                                                                                  | Role                                                                                                                | Description                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Reference Vocabularies:<br />[`resources/reference/*.ttl`](resources/reference/*.ttl)                                                                                                                     | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                | EIA Reference Vocabularies                                                               |
| Spatial Datasets:<br />[`https--linked.data.gov.au-def-eia-supermodel.ttl`](https--linked.data.gov.au-def-eia-supermodel.ttl)<br />[`resources/datasets/spatial/*.ttl`](resources/datasets/spatial/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                | Spatial EIA Datasets                                                                     |
| Non-Spatial Datasets:<br />[`resources/datasets/non-spatial/*.ttl`](resources/datasets/non-spatial/*.ttl)                                                                                                 | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                | Non-spatial EIA Datasets                                                                 |
| Catalogue Definition:<br />[`catalogue.ttl`](resources/catalogues/catalogue.ttl)                                                                                                                          | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData)                                              | The definition of, and medata for, the container which here is a dcat:Catalog object     |
| Background Details:<br />[`resources/background/*.ttl`](resources/background/*.ttl)                                                                                                                       | [Complete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/CompleteCatalogueAndResourceLabels) | Files containing all the labels and vocab inScheme predicates for the resources' content |

### Installation

To establish a Prez system loaded with all this data:

1. Run Prez as per the [prezdemo repository](https://github.com/Kurrawong/prezdemo)
   * ensure Prez has the `CUSTOM_ENDPOINT=true` environment variable set in the [docker/compose.yml](https://github.com/Kurrawong/prezdemo/blob/main/docker/compose.yml#L20-L22) file

Once running:

2. clear the DB 
   * via the Fuseki UI or using [kurra](https://pypi.org/project/kurra/)
       * `kurra db sparql "DROP ALL" SPARQL_ENDPOINT -u xxx -p yyy`
3. load custom Prez endpoints definition
   * via the Fuseki UI or using [kurra](https://pypi.org/project/kurra/)
       * `kurra db upload config/prez-endpoints.ttl SPARQL_ENDPOINT -g http://prez-system -u xxx -p yyy `
4. sync the data up
   * use [PrezManifest](https://github.com/Kurrawong/prezmanifest)
    * `pm sync manifest.ttl SPARQL_ENDPOINT -u xxx -p yyy`
5. Restart Prez

Go to <http://localhost:3000>