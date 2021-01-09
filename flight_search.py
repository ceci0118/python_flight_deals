import requests
from datetime import date
from dateutil.relativedelta import relativedelta
import os

TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')
tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
tequila_location_endpoint = "https://tequila-api.kiwi.com/locations/query"

headers = {
    'apikey': TEQUILA_API_KEY,
    'Accept': 'application/json'
}

# search flight in one year range
TODAY = date.today().strftime("%d/%m/%Y")
SIX_MONTH = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
NEXT_YEAR = (date.today() + relativedelta(years=+1)).strftime("%d/%m/%Y")


#test
# search_params = {
#     'fly_from': 'YYZ',
#     'fly_to': 'YOW',
#     'date_from': TODAY,
#     'date_to': SIX_MONTH,
#     'flight_type': 'round',
#     'nights_in_dst_from': 7,
#     'nights_in_dst_to': 28,
#     'price_to': 500,
#     'curr': 'CAD',
#     'max_stopovers': 0
# }
#
# flight_res = requests.get(url=tequila_search_endpoint, params=search_params, headers=headers)
# # print(len(flight_res.json()['data']))
# valid_data = len(flight_res.json()['data'])
# if valid_data != 0:
#     print(flight_res.json()['data'][0])



#This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def get_flight_price(self, code, price):
        search_params = {
            'fly_from': 'YYZ',
            'fly_to': code,
            'date_from': TODAY,
            'date_to': SIX_MONTH,
            'flight_type': 'round',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'price_to': price,
            'curr': 'CAD',
            "one_for_city": 1,
            'max_stopovers': 0
        }

        flight_res = requests.get(url=tequila_search_endpoint, params=search_params, headers=headers)

        valid_data = len(flight_res.json()['data'])
        if valid_data != 0:
            return flight_res.json()['data'][0]





    def get_iata_code(self, city):
        location_params = {
            'term': city,
            'location_types': 'city'
        }
        location_res = requests.get(url=tequila_location_endpoint, params=location_params, headers=headers)
        code = location_res.json()['locations'][0]['code']
        return code



