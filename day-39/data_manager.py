import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/b64624a52c6e68107128dab5d399749d/flightDeals/prices'


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.headers_sheety = {"Authorization": "Basic cmFkeXI6aW91aGdpeWR0ZWRhZHNmYXNkZmdo"} #os.environ["SHEETY_PASSWORD"]
        # {"Authorization": "Basic cmFkeXI6aW91aGdpeWR0ZWRhZHNmYXNkZmdo"}
        self.prices = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers_sheety)
        response.raise_for_status()
        self.prices = response.json()['prices']
        return self.prices

    def add_data(self, new_row):
        response = requests.post(url=SHEETY_PRICES_ENDPOINT, json=new_row, headers=self.headers_sheety)
        response.raise_for_status()
        print(response)

    def update_destination_codes(self):
        for city in self.prices:
            update_row = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=update_row, headers=self.headers_sheety)
            response.raise_for_status()
            print(response.text)
