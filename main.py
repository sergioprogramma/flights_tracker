from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt

dest_email = "-"
my_email = '-'
password = '-'
now = dt.datetime.now()
weekday = now.weekday()
search_flight = FlightSearch()
raw_data = DataManager()
sheet_data = raw_data.get_destination_data()
length_of_sheet = len(sheet_data['sheet1'])
data_flights = FlightData()
notification = NotificationManager()
for i in range(0, length_of_sheet):
    if sheet_data['sheet1'][i]["iataCode"] == "":
        response = search_flight.iata_code(sheet_data['sheet1'][i])
        print(response)
        # Updating list with the returned response from iata_code() method in FlightSearch Class
        sheet_data['sheet1'][i]['iataCode'] = response
        raw_data.update_code(sheet_data['sheet1'][i])
        price_flights = data_flights.get_flights_data(response)
        try:
            price = price_flights['data'][0]['price']
            print(price)
            lowest_price = sheet_data['sheet1'][i]['lowestPrice']
            print(lowest_price)
            dep_city = price_flights['data'][0]['cityFrom']
            dep_airport = price_flights['data'][0]['flyFrom']
            ar_city = price_flights['data'][0]['cityTo']
            ar_airport = price_flights['data'][0]['flyTo']
            first_day = price_flights['data'][0]['local_departure']
            first_day = first_day[:10]
            last_day = price_flights['data'][0]['utc_arrival']
            last_day = last_day[:10]
            if price <= lowest_price:
                notification.send_text(dep_city, dep_airport, ar_city, ar_airport, price, first_day, last_day)
                notification.send_email(dest_email, my_email, password, dep_city, dep_airport, ar_city, ar_airport,
                                        price, first_day, last_day)
        except:
            pass

