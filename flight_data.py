TEQUILA_ENDPOINT = "-"
TEQUILA_API_KEY = "-"

import requests
import datetime

class FlightData:

    def get_flights_data(self, iatacode):
        tequila_endpoint = TEQUILA_ENDPOINT
        beg = datetime.datetime.now()
        end = beg + datetime.timedelta(days=180)
        today = beg.strftime("%d/%m/%Y")
        end_period = end.strftime("%d/%m/%Y")
        tequila_location = f"{tequila_endpoint}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        iata_parms = {
            "fly_from": "YTO",
            "fly_to": iatacode,
            "date_from": today,
            "date_to": end_period,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "adults": 1
        }
        flights_data = requests.get(url=tequila_location, headers=headers, params=iata_parms)
        flights_response = flights_data.json()
        return flights_response
