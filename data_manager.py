import requests
import pandas as pd

# -----------------------------Local Excel-----------------------------------

deals_data = pd.read_csv('./flight_deals.csv')
deals = deals_data.to_dict('record')
# print(deals)

# -----------------------------Sheety API-----------------------------------

sheety_endpoint = ''
AUTHORIZATION = ""
headers = {
    'Authorization': AUTHORIZATION
}

#---------------------------------------------------------------------------

#This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.des_data = deals

    def getIATAcode(self):
        sheety_res = requests.get(url=sheety_endpoint, headers=headers)
        self.des_data = sheety_res.json()['prices']
        return self.des_data

    def updateIATAcode(self):
        for city in self.des_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, headers=headers)

