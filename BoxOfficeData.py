
# coding: utf-8

# ### Reading in movie box office data from boxofficemojo

# In[91]:

import requests
from bs4 import BeautifulSoup
import pickle
import time


# In[92]:

import os
os.getcwd()
os.chdir('/Users/ItelinaMa/Documents/Metis/Luther')


# In[93]:

urllist = ['http://www.boxofficemojo.com/daily/?view=bymovie&yr=2015&page=1&sort=title&order=ASC&p=.htm', 'http://www.boxofficemojo.com/daily/?view=bymovie&yr=2015&page=2&sort=title&order=ASC&p=.htm', 'http://www.boxofficemojo.com/daily/?view=bymovie&yr=2014&sort=title&order=ASC&p=.htm', 'http://www.boxofficemojo.com/daily/?view=bymovie&yr=2014&page=2&sort=title&order=ASC&p=.htm', 'http://www.boxofficemojo.com/daily/?view=bymovie&yr=2014&page=3&sort=title&order=ASC&p=.htm']
url = urllist[1]


# In[94]:

def returnSoup(urllist):
    soups = []
    for url in urllist:
        response = requests.get(url)
        while response.status_code != 200:
            time.sleep(2)
            response = requests.get(url)
        print response.status_code #Remember to come back later and write a function that tells this to repeat if one of the status codes returns negative
        soup = BeautifulSoup(response.text)
        soups.append(soup)
    return soups


# In[95]:

soups = returnSoup(urllist)


# In[96]:

def makeData(soups):
    releasegross = []
    movienames = []
    releasedate =[]
    studio = []
    for soup in soups:
        tablelength = len(soup.find_all('table')[1].find_all('tr'))
        for i in range(2, tablelength):
            releasegross.append(soup.find_all('table')[1].find_all('tr')[i].find_all('td')[3].text)
            movienames.append(soup.find_all('table')[1].find_all('tr')[i].find_all('td')[0].text)
            releasedate.append(soup.find_all('table')[1].find_all('tr')[i].find_all('td')[4].text)
            studio.append(soup.find_all('table')[1].find_all('tr')[i].find_all('td')[1].text)
    boxoffice ={}
    for i, item in enumerate(movienames):
        boxoffice[item] = zip(studio, releasegross, releasedate)[i]
    return boxoffice


# In[97]:

boxoffice = makeData(soups)


# In[98]:

len(boxoffice) == 461


# In[100]:

with open('boxofficedata.pkl', 'w') as picklefile:
    pickle.dump(boxoffice, picklefile)

