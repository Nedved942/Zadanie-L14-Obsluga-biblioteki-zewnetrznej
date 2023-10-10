import requests
from datetime import date, timedelta

print("*** Obsługa biblioteki zewnętrznej ***")

# day_from_user = input("Podaj dzień, dla którego chcesz sprawdzić pogodę (YYYY-mm-dd): ")

latitude = "50"
longitude = "50"
searched_date = "2023-10-11"
URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude" \
      f"={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

data = requests.get(URL)
data_dict = data.json()
print(data_dict)
