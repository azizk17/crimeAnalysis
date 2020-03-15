

# read file
# clean data
# make api call to weather service
# save data in a new dataset
import pandas as pa
from pandas.io.json import json_normalize

import requests as req
import time
import json
from datetime import datetime


def start2():
    rowsLimit = 10
    # read orginal dataset file
    file1 = readOrginalFile("chicago_crimes_2016.csv")
    content = file1.head(rowsLimit)
    # pick required attributes
    content[["ID", "Date", "Latitude", "Longitude"]]
    # make api call on each row to get weather details
    # save weather details as JSON for now
    content['Weather_details'] = content.apply(get_weather, axis=1)
    # save to file
    content.to_csv("data/fil4.csv", index=False)
    # res = json_normalize(content['Weather_details'])



def readOrginalFile(file):
    df = pa.read_csv("data/" + file)
    return df


def saveDataToFile():
    df = pa.to_csv("data/weather.csv", index=False)


def cleanData():
    print("clean")


def updateFile():
    print("Update File")


def saveNewFile():
    print("Save File")
    df = pa


def get_weather(row):
    print('is weather called: ' + str(row['Date']))
    api_key = ""
    api_url = "https://api.darksky.net/forecast/" + api_key + "/"
    # Measurements units
    units = "si"
    # convert time to unix format
    lat = str(row["Latitude"])
    log = str(row["Longitude"])
    formatedDate = convertDate(str(row["Date"]))
    # build url query
    query = api_url + lat + "," + log + "," + formatedDate + \
        "?units=" + units + "&exclude=currently,flags"
    try:
        weatherData = {}
        response = (req.get(query).text)
        json_response = json.loads(response)
        for items in json_response['hourly']['data']:
            if items['time'] == int(formatedDate):
                weatherData = {
                    "time": items['time'],
                    "summary": items["summary"],
                    "temperature": items["temperature"],
                    "humidity": items["humidity"],
                    "pressure": items["pressure"],
                    "windSpeed": items["windSpeed"],
                    "cloudCover": items["cloudCover"],
                    "visibility": items["visibility"]
                }
                break
        return weatherData

    except Exception as e:
        raise e


# convert date format
def convertDate(date):
    fmt = ("%m/%d/%Y %I:%M:%S %p")
    # d = "05/03/2016 04:00:00 PM"
    epochDate = int(time.mktime(time.strptime(date, fmt)))

    # test converted date
    # print("Orginal date: " + d)
    # print(time.strftime(fmt, time.localtime(epochDate)))
    return str(epochDate)


# RUN
# getWeather("41.880658", "-87.731212", d)
# d = datetime.date(2015,1,5)


start2()
