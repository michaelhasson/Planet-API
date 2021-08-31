import os
import json
import requests
from requests.auth import HTTPBasicAuth
from MSW_AOI_filters import MSW

# API Key stored as an env variable
PLANET_API_KEY = '6ab0e38c88fd4ff0ac59eb277fa8c2be'

item_type = "PSScene4Band"

# API request object
search_request = {
  "item_types": [item_type], 
  "filter": MSW
}

# fire off the POST request
search_result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(PLANET_API_KEY, ''),
    json=search_request)

print(json.dumps(search_result.json(), indent=1))