import requests
import re
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from string import whitespace
from newsapi import NewsApiClient
from constant import *

def callApi(preference):

    #API Init
    newsapi = NewsApiClient(api_key='60941ffff9a04202b7b6f8124c3a2a46')

    #API set preference

    call = {'q':None, 'sources':None, 'domains':None, 'from':None, 'to':None, 'language':'en', 'sort_by':None, 'country':None, 'category':None, 'page_size':None,'page':None}

    for key in preference.keys():
        call[key] = preference[key]

    '''     GET EVERYTHING CALL CAN TAKE FOLLOWING

        q                   sources
        country             category
        page_size           page

    '''

    #API call for top headline articles
    response = newsapi.get_top_headlines(q=call['q'],sources=call['sources'],country=call['country'],category=call['category'],page_size=call['page_size'],page=call['page'])

    #API call for all news articles
    '''     GET EVERYTHING CALL CAN TAKE FOLLOWING

        q                   sources
        domains             from
        to                  language
        sort_by             page_size
        page

    '''
   # response = newsapi.get_everything(q=call['q'],sources=call['sources'],domains=call['domains'],from_param=call['from'],to=call['to'],language=call['language'],sort_by=call['sort_by'],page_size=call['page_size'],page=call['page'])

#    url = "https://newsapi.org/v2/top_headlines?q="+preference+"&from=2019-02-09&sortBy=publishedAt&apiKey=60941ffff9a04202b7b6f8124c3a2a46";
    urls = {}
#    response = requests.get(url)

    return response


def calculateWordCount(content):

    char_counter = 0
   # content_copy = content[:]
    characters = re.sub('\[\+[0-9]* chars\]$','',str(content))
    num_count_length = 0
    if(str(characters) != str(content)):
        num_count = content[len(characters)+2:-7]

        for c in num_count:
            num_count_length = num_count_length*10 + int(c)

    char_counter = num_count_length + len(characters)
    return int(char_counter/WORD_SIZE)


    # r = requests.get(url)
    # soup = BeautifulSoup(r.content, features="html.parser")
    #
    # text_p = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    # c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))
    #
    # text_div = (''.join(s.findAll(text=True)) for s in soup.findAll('div'))
    # c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))
    #
    # total = c_div + c_p
    # return dictionaryCount(total)

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
