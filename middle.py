import json
from urllib.request import urlopen

def getPreference(preference, time):
    response = callApi(preference)
    urls = {}
    counter = 0
    urlCounter = 0
    if response.json()["status"] != "ok":
        print("Error has occurred")
    else:
        for i in range(response.json()["totalResults"]):
            

            wordCount  = calculateWordCount(response.json()["articles"][i]["url"])
            if wordCount/time < 225:
                url = {}
                url["url"] = response.json()["articles"][i]["url"]
                
                url["wordCount"] = wordCount
                urls[counter] = url
                counter = counter + 1
                urlCounter = i
                if counter >10:
                    break
            
    urls["counter"] = urlCounter
        
    return urls

def getMore(preference, time, counter):
    response = callApi(preference)
    urls = {}
    count = 0
    if  response.json()["status"] != "ok":
        print("Error has occurred")
    else:
        for i in range(counter ,response.json()["totalResults"]):

            wordCount  = calculateWordCount(response.json()["articles"][i]["url"])
            if wordCount/time < 225:
                url = {}
                url["url"] = response.json()["articles"][i]["url"]
                
                url["wordCount"] = wordCount
                urls[count] = url
                counter  = i
                count = count + 1
                if count >counter10Terminate:
                    break
            
    urls["counter"] = counter
        
    return urls