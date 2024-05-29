from datetime import datetime
import pytz
import requests
from datetime import datetime, timezone
import pytz
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
    current_time = datetime.now(timezone.utc)
    arrivals = [item['expectedArrival'] for item in data]
    arrivals_datetime = [datetime.fromisoformat(arrival.replace('Z', '+00:00')) for arrival in arrivals]
    arrivals_datetime.sort()
    uk_tz = pytz.timezone('Europe/London')
    time_now = datetime.now(uk_tz)
    print(f"The time is now: {time_now.strftime('%H:%M')}")
    for arrival in arrivals_datetime:
        arrival_uk_time = arrival.astimezone(uk_tz)
        if arrival_uk_time >= time_now:
            print(arrival_uk_time.strftime('%H:%M'))
else:
    print("No data received from API")