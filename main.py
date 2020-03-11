

## read file 
## clean data 
## make api call to weather service 
## save data in a new dataset
import pandas as pa




def start() :
    file1 = readOrginalFile("chicago_crimes_2016.csv")
    for label, row in file1.iterrows():
        print(label)
        print(row)



def readOrginalFile(file) : 
    df = pa.read_csv("data/" + file)
    return df
     

def getWeather(lat, lon) :
    API_KEY = ""
    API_URL = ""
    FORMATED_URL = API_URL + "/" + lat + "," + lon
    # TODO: check if weather is already exited to reduced API cost 
    # response = requests.get(FORMATED_URL)


# RUN
start()