

SHEETY_PRICES_ENDPOINT = '-'

import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        self.sheety_endpoint = SHEETY_PRICES_ENDPOINT
        sheety_response = requests.get(url=self.sheety_endpoint)
        sheety_response.raise_for_status()
        self.destination_data = sheety_response.json()
        return self.destination_data

    def update_code(self, city_dict):
        row_id = city_dict["id"]
        row_code = city_dict["iataCode"]
        sheety_update = f"{self.sheety_endpoint}/{row_id}"
        update_params = {
            "sheet1": {
                "iataCode": row_code
            }
        }
        update_row = requests.put(url=sheety_update, json=update_params)
        update_row.raise_for_status()
