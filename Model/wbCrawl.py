import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from string import whitespace

def callApi(preference):
    url = "https://newsapi.org/v2/everything?q="+preference+"&from=2019-02-09&sortBy=publishedAt&apiKey=60941ffff9a04202b7b6f8124c3a2a46";
    urls = {}
    response = requests.get(url)
    return response


def calculateWordCount(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")

    text_p = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

    text_div = (''.join(s.findAll(text=True)) for s in soup.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

    total = c_div + c_p
    return dictionaryCount(total)

def dictionaryCount(dictionary):
    count = 0
    for key in dictionary:
        #skip key on empty stirng
        index = 0;
        while((index < len(key)) and (key[index] in whitespace)):
            index = index + 1
        if(index != len(key)):
            count = count + dictionary[key]
    return count

#callApi("URI")
