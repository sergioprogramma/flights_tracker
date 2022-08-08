TEQUILA_ENDPOINT = "-"
TEQUILA_API_KEY = "-"

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def iata_code(self, city_dict):
        tequila_endpoint = TEQUILA_ENDPOINT
        tequila_location = f"{tequila_endpoint}/locations/query"
        city = city_dict["city"]
        headers = {"apikey": TEQUILA_API_KEY}
        iata_parms = {
                "term": city,
                "location_types": "city",
        }
        iata_data = requests.get(url=tequila_location, headers=headers, params=iata_parms )
        iata_response = iata_data.json()
        iata_code = iata_response['locations'][0]["code"]
        return iata_code