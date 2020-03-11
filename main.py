

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


def getWeather(lat, lon) :
    api_key = ""
    api_url = "https://api.darksky.net/forecast/"+ api_key + "/" 
    query = api_url + lat + "," + lon
    # TODO: check if weather is already exited to reduced API cost 

    # convert time to unix format 
    date = "05/03/2016 09:00:00 PM"
    # recived date formte %d/%m/%Y %H:%M:%S %p
    date_object = datetime.strptime(str, '%d/%m/%Y %H:%M:%S %p')
    # unixtime
    unixTime = time.strftime("%s", "05/03/2016 09:00:00 PM")

    response = req.get(query)
    json_response = response.json()
    print(json_response)

# RUN
# getWeather("41.880658","-87.731212")
# d = datetime.date(2015,1,5)

# unixtime = time.mktime(d.timetuple())
# print(unixtime)
str = "05/03/2016 04:00:00 PM"
date_object = datetime.strptime(str, "%m/%d/%Y %H:%M:%S %p")
print(str)
print(date_object)

unixTime = time.mktime(date_object.timetuple())
print(date_object.strftime("%b %d %Y %H:%M:%S %p"))

print(unixTime)
print(datetime.fromtimestamp(unixTime).strftime('%Y-%m-%d %H:%M:%S %p'))
# start()
