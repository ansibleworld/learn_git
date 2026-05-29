import requests
import time

url = "https://httpbin.org/status/100,200,300,400"

max_retries = 2
delay = 2

for retry in range(1, max_retries + 1):
    try:
        response = requests.get(url, timeout=10)

        # Raise exception for 4xx and 5xx
        response.raise_for_status()

        print(f"Success with status code {response.status_code}")
        break

    except requests.exceptions.HTTPError as error:
        status = error.response.status_code
        print(f"Failed with status code {status}")

        # Stop retrying for client-side errors
        if 400 <= status < 500:
            print("Client-side error")
            break

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    if retry < max_retries:
        print(f"Retrying in {delay} seconds...")
        time.sleep(delay)

else:
    print("All retries failed")