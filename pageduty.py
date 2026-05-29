import requests
import json
def get_incident_summary(api_url: str, api_key: str, service_id: str) -> Optional[List[str]]:
    if not api_url.strip():
        raise ValueError
    if not api_key.strip():
        raise ValueError
    if not service_id.strip():
        raise ValueError
    api_url = api_url.strip()
    service_id = service_id.strip()
    api_key = api_key.strip()
    url = f"{api_url}/incidents"
    params = {
        "service_ids[]" : service_id,
        "statuses[]": 'triggered' }
                  
    headers = {
        "Authorization" : f"Bearer {api_key}"
    }
    try:
        response = requests.get(url, headers=headers , params=params)
        response.raise_for_status()
        result = response.json()
        incidents = result.get("incidents" , [])
        if not incidents:
            return []
        final_result = []
        for items in incidents:
            summary = f"[{items['urgency'].upper()}] {items['id']}: {items['title']}"
            final_result.append(summary)
        return final_result
    except requests.exceptions.HTTPError:
        return None

