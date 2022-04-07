import requests
from pprint import pprint

class DataManager:

    def __init__(self):

        self.sheet_endpoint = "https://api.sheety.co/ac95d112e6c10b5098ba3da54b60334a/flightDeals/prices"

    def putData(self, city, code, price):

        self.sheet_body = {
            "price": {
                "city": city,
                "iataCode": code,
                "lowestPrice": price
                }
            }

        res = requests.post(url=self.sheet_endpoint, json=self.sheet_body)
        return res.raise_for_status(), res.text

    def getData(self):

        r = requests.get(url=self.sheet_endpoint)
        return r.text

