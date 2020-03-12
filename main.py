

# read file
# clean data
# make api call to weather service
# save data in a new dataset
import pandas as pa
from pandas.io.json import json_normalize

import requests as req
import time
from datetime import datetime


def start():
    rowsLimit = 10
    file1 = readOrginalFile("chicago_crimes_2016.csv")
    content = file1.head(rowsLimit)
    # pick requied attributes
    content = content.loc[:, ["ID", "Date", "Latitude", "Longitude"]]
    # drop rows that missing required attributes
    content.dropna(how='any')
    # make api call to get weather details based on location
    newData = pa.DataFrame()
    for key, value in content.iterrows():

        lat = str(value["Latitude"])
        log = str(value["Longitude"])
        date = str(value["Date"])
        # print(key)
        # print(value)

        weatherData = getWeather(lat, log,  date)
        value = pa.concat([value, weatherData], sort=False)

        print(value)

        # content["time"] = weatherData['time']
        # content["summary"] = weatherData["summary"]
        # content["temperature"] = weatherData["temperature"]
        # content["humidity"] = weatherData["humidity"]
        # content["pressure"] = weatherData["pressure"]
        # content["windSpeed"] = weatherData["windSpeed"]
        # content["cloudCover"] = weatherData["cloudCover"]
        # content["visibility"] = weatherData["visibility"]
        # finalData = pa.concat([value, weatherData], sort=False)
        # print(finalData)
        # print(key)
        if key == 10:
            break
    content.to_csv("data/fil4.csv", index=False)
# content = file1.loc()
# for label, row in file1.iterrows():
#     print(label)
#     print(row)
#     print("--------------")


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


def getWeather(lat, lon, date):
    api_key = ""
    api_url = "https://api.darksky.net/forecast/" + api_key + "/"
    units = "si"
    formatedDate = convertDate(date)
    query = api_url + lat + "," + lon + "," + formatedDate + \
        "?units=" + units + "&exclude=currently,flags"
    # TODO: check if weather is already exited to reduced API cost

    # convert time to unix format
    response = req.get(query)
    json_response = response.json()
    # print(json_response['hourly']['data'])
    weatherData = {}
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
    return json_normalize(weatherData)


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


start()
