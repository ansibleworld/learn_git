import requests
import json

url = "https://api.example.com/v1/holidays"

try:
    response = requests.get(url, timeout=5)

    response.raise_for_status()

    print(json.dumps(response.json(), indent=2))

except requests.exceptions.HTTPError as err:

    try:
        details = err.response.json()

        err_details = json.dumps(details, indent=2)

        print(err_details)

    except ValueError:
        print("Response is not valid JSON")