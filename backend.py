import requests

API_KEY = "36ee6b3ce9714741da28f988efbc52c7"


def get_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [i['main']['temp'] for i in filtered_data]
    if kind == "Sky":
        filtered_data = [i['weather']['main'] for i in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind = "Temperature"))

