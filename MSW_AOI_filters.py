# MSW imagery API

# Taken from geojson.io
geo_json_geometry = {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -117.15270996093749,
          39.03545292971819
        ],
        [
          -117.15648651123047,
          39.033319472320926
        ],
        [
          -117.17794418334961,
          38.99050337619313
        ],
        [
          -117.16455459594725,
          38.97769352767186
        ],
        [
          -117.12747573852539,
          38.974757610940586
        ],
        [
          -117.09829330444337,
          39.032519409191565
        ],
        [
          -117.11151123046875,
          39.047719059771914
        ],
        [
          -117.13983535766602,
          39.045052690922034
        ],
        [
          -117.15270996093749,
          39.03545292971819
        ]
      ]
    ]
  }

# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2010-07-01T00:00:00.000Z",
    "lte": "2021-08-29T00:00:00.000Z"
  }
}

# filter any images which are more than 50% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.2
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
MSW = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}