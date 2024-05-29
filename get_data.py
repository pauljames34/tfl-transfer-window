from datetime import datetime
import requests

def get_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

url = "https://api.tfl.gov.uk/Line/elizabeth/Arrivals/910GHANWELL?direction=inbound"
data = get_api_data(url)

if data is not None:
    arrivals = [item['expectedArrival'] for item in data]
    arrivals_datetime = [datetime.fromisoformat(arrival.replace('Z', '+00:00')) for arrival in arrivals]
    arrivals_datetime.sort()
    print(arrivals_datetime)
else:
    print("No data received from API")