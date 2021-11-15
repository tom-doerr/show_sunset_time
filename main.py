import datetime
import requests
import json
import sys
import os

def get_sunset_time(lat, lon):
    """
    This function gets the sunset time of the location based on the lat and lon
    of the city.
    """
    url = "https://api.sunrise-sunset.org/json?lat={0}&lng={1}&formatted=0".format(lat, lon)
    response = requests.get(url)
    json_data = json.loads(response.text)
    sunset = json_data["results"]["sunset"]
    return sunset

def get_time_from_sunset(sunset):
    """
    This function gets the time from the sunset time.
    """
    sunset_utc = datetime.datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S%z")
    sunset_local = sunset_utc.astimezone()
    return sunset_local.strftime("%H:%M")

def get_location():
    """
    This function gets the location of the user.
    """
    url = "http://ipinfo.io/json"
    response = requests.get(url)
    json_data = json.loads(response.text)
    lat = json_data["loc"].split(",")[0]
    lon = json_data["loc"].split(",")[1]
    return lat, lon

def main():
    """
    This function is the main function.
    """
    lat, lon = get_location()
    sunset = get_sunset_time(lat, lon)
    sunset_time = get_time_from_sunset(sunset)
    print(sunset_time)

if __name__ == "__main__":
    main()
