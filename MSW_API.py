import requests
import os
from requests.auth import HTTPBasicAuth
from MSW_AOI_filters import MSW

PLANET_API_KEY = '6ab0e38c88fd4ff0ac59eb277fa8c2be'
# Setup the API Key from the `PL_API_KEY` environment variable

# Stats API request object
stats_endpoint_request = {
    "interval": "day",
    "item types": ["REOrthoTile"],
    "filter": MSW
}

#Fire off the POST request
result = \
    requests.post(
        'https://api.planet.com/data/v1/quick-search', auth=HTTPBasicAuth(os.environ[PLANET_API_KEY],''), json = stats_endpoint_request)

print (result.text)