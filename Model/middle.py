import json
import re
from constant import *
from wbCrawl import *
from urllib.request import urlopen
from wbCrawl import *


def getPreference(preference, time):
    response = callApi(preference)
    urls = {}
    urls["articles"] = []
    counter = 0
    urlCounter = 0
    if response["status"] != "ok":
        print("Error has occurred")
    else:
        pagecount = response["totalResults"]
        if(pagecount > PAGE_SIZE):
             pagecount = PAGE_SIZE
        for i in range(pagecount):
            wordCount  = calculateWordCount(response["articles"][i]["content"])
            if wordCount/time < READING_SPEED:
                url = {}
                url["url"] = response["articles"][i]["url"]
                url["title"] = response["articles"][i]["title"]
                url["author"] = response["articles"][i]["author"]
                url["source"] = response["articles"][i]["source"]["name"]
                url["urlToImage"] = response["articles"][i]["urlToImage"]
                url["readTime"] = wordCount/READING_SPEED
                url["wordCount"] = wordCount
                urls["articles"].append(url)
                counter = counter + 1
                urlCounter = i
                if counter > MAX_NUM_ARTICLES:
                    break

    urls["counter"] = urlCounter

    return urls

def getMore(preference, time, counter):
    response = callApi(preference)
    urls = {}
    urls["articles"] = []
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
                urls["articles"].append(url)
                counter  = i
                count = count + 1
                if count > MAX_NUM_ARTICLES:
                    break

    urls["counter"] = counter

    return urls

def getTime(start_location, end_location):

    time_sec = 0
    time_min = 0

    origin = ''
    destination = ''

    origin += str(start_location['lat'])+','+str(start_location['lng'])
    destination += str(end_location['lat'])+','+str(end_location['lng'])

    origin += "+ON"
    destination += "+ON"

    response = calculateTime(origin, destination)

    if response.json()["status"] != "OK":
        print("Error has occurred")
    else:
        time_sec = response["rows"][0]["elements"]["duration"]["value"]
        time_min = int(time_sec/60)

    return time_min
