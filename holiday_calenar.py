import requests
from datetime import datetime

def is_today_a_public_holiday(country_code: str) -> bool:
    if not isinstance(country_code , str):
        raise TypeError
    today = datetime.today()
    current_year = datetime.today().year
    search_url = "https://api.example.com/v1/holidays"
    query_param = {
        "country" : country_code,
        "year" : current_year
    }

    response = requests.get(search_url , params=query_param , timeout=30)
    response_json = response.json()

    for responses in response_json:
        if responses["holiday"] == today:
            return True
        else:
            return False