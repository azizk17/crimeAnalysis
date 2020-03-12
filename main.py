

## read file 
## clean data 
## make api call to weather service 
## save data in a new dataset
import pandas as pa
import requests as req
import time
from datetime import datetime 

def start() :
    file1 = readOrginalFile("chicago_crimes_2016.csv")
    print(file1.head())
    # pick requied attributes
    content = file1.loc[: , ["ID", "Date", "Latitude", "Longitude"]]
    # drop rows that missing required attributes
    content.dropna(how='any')
    # make api call to get weather details based on location
    # print(content)
    # save to new file
    content.to_csv("data/fil2.csv", index=False)
    # content = file1.loc()
    # for label, row in file1.iterrows():
    #     print(label)
    #     print(row)
    #     print("--------------")



def readOrginalFile(file) : 
    df = pa.read_csv("data/" + file)
    return df


def cleanData() :
    print("clean") 

def updateFile() :
    print("Update File")
def saveNewFile() :
    print("Save File")
    df = pa


def getWeather(lat, lon, date) :
    api_key = ""
    api_url = "https://api.darksky.net/forecast/"+ api_key + "/"

    formatedDate = convertDate(date)
    query = api_url + lat + "," + lon + "," + formatedDate
    # TODO: check if weather is already exited to reduced API cost 

    # convert time to unix format 
    date = convertDate(date)
    response = req.get(query)
    json_response = response.json()
    print(json_response)

## convert date format 
def convertDate(date) :
    fmt = ("%m/%d/%Y %I:%M:%S %p")
    # d = "05/03/2016 04:00:00 PM"
    epochDate = int(time.mktime(time.strptime(date, fmt)))

    print(epochDate)

    #test converted date
    # print("Orginal date: " + d)
    print(time.strftime(fmt, time.localtime(epochDate)))
    return str(epochDate)

# RUN
d = "05/03/2016 04:00:00 PM"

getWeather("41.880658","-87.731212", d)
# d = datetime.date(2015,1,5)


# start()
