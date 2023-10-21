import requests
from pprint import pprint
from datetime import date, timedelta
from json import dumps, loads

print("*** Obsługa biblioteki zewnętrznej ***")

# try:
#     with open("warehouse.json") as file_stream:
#         warehouse_txt_data = file_stream.read()
#
#         if not warehouse_txt_data:
#             print("Plik jest pusty.")
#         else:
#             warehouse = loads(warehouse_txt_data)
# except FileNotFoundError:
#     print("Nie pobrano danych z pliku.")
# except JSONDecodeError as e:
#     print(f"Wystąpił nieoczekiwany błąd {e}.")


with open("history_weather_forecast.json") as file_stream:
    history_weather_forecast = file_stream.read()
    history_weather_forecast = loads(history_weather_forecast)

# day_from_user = input("Podaj dzień, dla którego chcesz sprawdzić pogodę (YYYY-mm-dd): ")
day_from_user = "2022-12-02"

# try:
#     day_from_user = day_from_user
# except:
#     pass

if day_from_user:
    searched_date = day_from_user
else:
    searched_date = str(date.today() + timedelta(days=1))

if searched_date in history_weather_forecast:
    rain_sum = history_weather_forecast[searched_date]
else:
    latitude = "51.248258"  # Szerokość geograficzna
    longitude = "22.535016"  # Długość geograficzna
    URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude" \
          f"={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&" \
          f"start_date={searched_date}&end_date={searched_date}"
    data = requests.get(URL)
    data_dict = data.json()
    # pprint(data_dict)
    rain_sum = data_dict['daily']['rain_sum'][0]
    history_weather_forecast[searched_date] = rain_sum

    with open("history_weather_forecast.json", "w") as file_stream:
        file_stream.write(dumps(history_weather_forecast))

if rain_sum > 0:
    print("Będzie padać.")
elif rain_sum == 0:
    print("Nie będzie padać.")
else:
    print("Nie wiem.")
