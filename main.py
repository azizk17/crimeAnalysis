

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
    file1 = readOrginalFile("chicago_crimes_2016.csv")
    content = file1.head(rowsLimit)
    content[["ID", "Date", "Latitude", "Longitude"]]
    content['API_response'] = content.apply(get_weather, axis=1)
    res = json_normalize(content['API_response'])
    new_df = res[['summary', 'time']]
    print(content.head(10))


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
        print("is empty" + str(weatherData.empty))
        if not weatherData.empty:
            print("Weather data has data: " + str(weatherData.empty))
        print('is data type correct: ' + str(type(weatherData) is type(content)))
        if (type(weatherData) is type(content)) and not (weatherData.empty):
            print("Im not sure")
            print(weatherData)
            value["time"] = weatherData['time']
            value["summary"] = weatherData["summary"]
            value["temperature"] = weatherData["temperature"]
            value["humidity"] = weatherData["humidity"]
            value["pressure"] = weatherData["pressure"]
            value["windSpeed"] = weatherData["windSpeed"]
            value["cloudCover"] = weatherData["cloudCover"]
            value["visibility"] = weatherData["visibility"]
        # finalData = pa.concat([value, weatherData], sort=False)
        # print(finalData)
        print(key)
        print(value)
        if key == 10:
            print(content)
            break
    # clean data that missing weather details
    content.dropna(how='any')
    print("### Content:   " + str(content))
    # save to file
    content.to_csv("data/fil4.csv", index=False)
    # print save
    print("### Saved ###")
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


def getWeather(lat, lon, date):
    api_key = ""
    api_url = "https://api.darksky.net/forecast/" + api_key + "/"
    # Measurements units
    units = "si"
    # convert time to unix format
    formatedDate = convertDate(date)
    # build url query
    query = api_url + lat + "," + lon + "," + formatedDate + \
        "?units=" + units + "&exclude=currently,flags"
    # TODO: check if weather is already exited to reduced API cost
    # catch api errors
    weatherData = {}

    try:
        response = req.get(query)
        json_response = response.json()
        # print("json responsse : " + str(json_response))
        # print("lat: " + lat + "," + lon + "," + formatedDate)
    # print(json_response['hourly']['data'])
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
    except requests.exceptions.RequestException as e:
        print e
        return e

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


start2()
