import json
from constant import *
from wbCrawl import *
from urllib.request import urlopen
from wbCrawl import *

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
            if wordCount/time < READING_SPEED:
                url = {}
                url["url"] = response.json()["articles"][i]["url"]
                url["title"] = response.json()["article"][i]["title"]
                url["author"] = response.json()["article"][i]["author"]
                url["urlToImage"] = response.json()["article"][i]["urlToImage"]
                url["readTime"] = wordCount/READING_SPEED
                url["wordCount"] = wordCount
                urls[counter] = url
                counter = counter + 1
                urlCounter = i
                if counter > MAX_NUM_ARTICLES:
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
            if wordCount/time < READING_SPEED:
                url = {}
                url["url"] = response.json()["articles"][i]["url"]

                url["wordCount"] = wordCount
                urls[count] = url
                counter  = i
                count = count + 1
                if count > MAX_NUM_ARTICLES:
                    break

    urls["counter"] = counter

    return urls