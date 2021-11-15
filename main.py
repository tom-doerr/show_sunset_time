import os
import sys
import time
import datetime
import requests
import json

# get the timezone of your location based on your IP
# https://stackoverflow.com/a/51800122
def get_timezone():
    send_url = 'http://ip-api.com/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['lat']
    lon = j['lon']
    return lat, lon

# get the sunset time for your location
def get_sunset(lat, lon):
    send_url = 'https://api.sunrise-sunset.org/json?lat=' + str(lat) + '&lng=' + str(lon) + '&formatted=0'
    r = requests.get(send_url)
    j = json.loads(r.text)
    sunset = j['results']['sunset']
    return sunset

# convert the time to your timezone
def convert_time(sunset):
    # convert datetime format to string
    sunset_string = str(sunset)
    # get the current time
    current_time = datetime.datetime.now()
    # convert the string to datetime format
    sunset_datetime = datetime.datetime.strptime(sunset_string, '%Y-%m-%dT%H:%M:%S+00:00')
    # calculate the timezone offset
    timezone_offset = current_time - datetime.datetime.utcnow()
    # convert the time to your timezone
    converted_time = sunset_datetime + timezone_offset
    # convert the datetime to string
    converted_time_string = converted_time.strftime('%H:%M')
    return converted_time_string

# main function
def main():
    # get the timezone of your location
    lat, lon = get_timezone()
    # get the sunset time for your location
    sunset = get_sunset(lat, lon)
    # convert the sunset time to your timezone
    converted_time = convert_time(sunset)
    print(converted_time)

# if this is the main thread of execution first load the model and then start the server
if __name__ == "__main__":
    # run the main function
    main()
