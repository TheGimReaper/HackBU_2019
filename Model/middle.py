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
    if response["status"] != "ok":
        print("Error has occurred")
    else:
        for i in range(response["totalResults"]):


            wordCount  = calculateWordCount(response["articles"][i]["url"])
            if wordCount/time < READING_SPEED:
                url = {}
                url["url"] = response["articles"][i]["url"]
                url["title"] = response["articles"][i]["title"]
                url["author"] = response["articles"][i]["author"]
                url["source"] = response["articles"][i]["source"]["name"]
                url["urlToImage"] = response["articles"][i]["urlToImage"]
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
    if  response["status"] != "ok":
        print("Error has occurred")
    else:
        for i in range(counter ,response["totalResults"]):

            wordCount  = calculateWordCount(response["articles"][i]["url"])
            if wordCount/time < READING_SPEED:
                url = {}
                url["url"] = response["articles"][i]["url"]

                url["wordCount"] = wordCount
                urls[count] = url
                counter  = i
                count = count + 1
                if count > MAX_NUM_ARTICLES:
                    break

    urls["counter"] = counter

    return urls
