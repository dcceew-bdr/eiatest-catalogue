# EIA Test Catalogue Tests

This `tests/` part of this repo contains Docker and Python scripts to run a Fuseki instance to test scenario queries against the catalogue data.

Fuseki can be run from the Taskfile within `fuseki/` by runnign `task fup`.

Once the server is up, datasets can be created, such as the test dataset in `fuseki/data/dataset-config.ttl`.

```
kurra db create http://localhost:3030 --config ./data/dataset-config.ttl
```

You'll see a warning in the docker logs of the `fuseki` service:

```
WARN  GeoAssembler    :: Dataset empty. Spatial Index not constructed. Server will require restarting after adding data and any updates to build Spatial Index.
```

We can add some data and restart the server:
```
kurra db upload ../../resources/datasets/nvis.ttl http://localhost:3030/eiatest-catalogue

task frs
```

Now you should see that the spatial index was created:

```
SpatialIndex    :: Saving Spatial Index - Completed: /fuseki/databases/eiatest-catalogue/spatial.index
```

Which means the following query should now work:

```
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>

SELECT DISTINCT ?dataset
WHERE {
  BIND("POLYGON((112.76 -10.23, 155.48 -10.23, 155.48 -44.28, 112.76 -44.28, 112.76 -10.23))"^^geo:wktLiteral AS ?polygon) #Bounding box of Australia
  ?dataset geo:boundingBox / geo:asWKT ?boundingbox .
  FILTER(geof:sfWithin(?boundingbox, ?polygon))
}
# returns
# 1<https://linked.data.gov.au/dataset/eiatest/nvis>
```

Each scenario is described within subfolder of the `scenario/` folder.