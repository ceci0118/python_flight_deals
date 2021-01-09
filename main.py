#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGINAL_CODE = 'YOW'

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# -------------------------Update IATA on Google sheets-------------------------------

def updateSheetData():
    sheet_data = data_manager.getIATAcode()
    for row in sheet_data:
        if row['iataCode'] == '':
            row['iataCode'] = flight_search.get_iata_code(row['city'])
    data_manager.des_data = sheet_data
    data_manager.updateIATAcode()

# -------------------------Flights data-------------------------------------

des_data = data_manager.des_data

for city in des_data:
    des_code = city['IATA Code']
    des_price = city['Lowest Price']
    flight_price = flight_search.get_flight_price(des_code, des_price)

    if flight_price:
        # print(flight_price)
        price = flight_price['price']
        city_from = flight_price['cityFrom']
        code_from = flight_price['flyFrom']
        city_to = flight_price['cityTo']
        code_to = flight_price['flyTo']
        date_from = flight_price['route'][0]['local_departure'].split('T')[0]
        date_to = flight_price['route'][1]['local_departure'].split('T')[0]
        link = flight_price['deep_link']

        message = f"🤑LOW PRICE ALERT! Only ${price} to fly from {city_from}-{code_from} to {city_to}-{code_to}, " \
                  f"from {date_from} to {date_to}\n Link: {link}"
        print(message)
        notification_manager.send_sms(message)







