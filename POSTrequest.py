import requests
import json

post_url = "https://httpbin.org/post"

payload = {
    "script_name" : "devops_atm",
    "action": "trigger_deployment",
    "environment": "staging",
    "version" : "v1.5.0"
    }

response = requests.post(post_url, json=payload , timeout=1)
response.raise_for_status()

dummp = json.dumps(response.json() , indent=4)
print(dummp)