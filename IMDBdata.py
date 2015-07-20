# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:10:53 2015

@author: ItelinaMa
"""

from imdb import IMDb
import os
from collections import defaultdict
import pickle

os.chdir('/Users/ItelinaMa/Documents/Metis/Luther')
ia = IMDb()

#Read in box office data
def loadBoxOffice():
    with open("boxofficedata.pkl", 'r') as picklefile: 
        boxoffice = pickle.load(picklefile)
    return boxoffice

movies = loadBoxOffice().keys()
len(movies)

with open("genre.pkl", 'r') as picklefile: 
        genre = pickle.load(picklefile)

movies = set(movies) - set(genre.keys())
len(movies)

for movie in movies:
    if not ia.search_movie(movie):
        genre[movie] = 'N/A'
        print(movie, "not found")
    else:
        firstmatch = ia.search_movie(movie)[0]
        ia.update(firstmatch)
        if firstmatch.has_key('genres') == 1:
            genre[movie] = firstmatch['genres']
            print(movie)
        else:
            genre[movie] = 'N/A'
            print(movie, 'genre not found')

with open('genre.pkl', 'w') as picklefile:
    pickle.dump(genre, picklefile)


'''getting director, cast, and runtime data'''

with open("director.pkl", 'r') as picklefile: 
    director = pickle.load(picklefile)

with open("cast.pkl", 'r') as picklefile: 
    cast = pickle.load(picklefile)

with open("runtime.pkl", 'r') as picklefile: 
    runtime = pickle.load(picklefile)

for movie in movies:
    if not ia.search_movie(movie):
        print(movie, "not found")
        director[movie] = 'N/A'
        cast[movie] = 'N/A'
        runtime[movie] = 'N/A'
    else:
        print(movie)        
        firstmatch = ia.search_movie(movie)[0]
        ia.update(firstmatch)
        if firstmatch.has_key('director') == 1:
            director[movie] = firstmatch['director'][0]['name']
        elif firstmatch.has_key('director') == 0:
            director[movie] = 'N/A'
        if firstmatch.has_key('cast') == 1:
            for item in firstmatch['cast']:
                cast[movie].append(item['name'])
        elif firstmatch.has_key('cast') == 0:
            cast[movie] = 'N/A'
        if firstmatch.has_key('runtime') == 1:
            for item in firstmatch['runtime']:
                runtime[movie].append(item)
        elif firstmatch.has_key('runtime') == 0:
            runtime[movie] = 'N/A'
        
    
with open('director.pkl', 'w') as picklefile:
    pickle.dump(director, picklefile)

with open('cast.pkl', 'w') as picklefile:
    pickle.dump(cast, picklefile)

with open('runtime.pkl', 'w') as picklefile:
    pickle.dump(runtime, picklefile)


'''Additional Information'''

'''
values = [u'music department', 'sound crew', 'rating', 'costume designer', 'make up', 'producer','mpaa', 'writer', 'visual effects', 'production manager', 'editor', u'costume department', 'sound mix', 'cinematographer', 'art direction', 'original music']


values1 = values[:5]
additional1 = defaultdict(list)
for movie in movies:
    if not ia.search_movie(movie):
        additional1[movie] = 'N/A'
    else:
        firstmatch = ia.search_movie(movie)[0]
        ia.update(firstmatch)
        for v in values1:
            if firstmatch.has_key(v) == 1:
                additional1[movie].append(firstmatch[v])
            elif firstmatch.has_key(v) == 0:
                additional1[movie].append('N/A')


values2 = values[5:10]    
additional2 = defaultdict(list)
for movie in movies:
    if not ia.search_movie(movie):
        additional2[movie] = 'N/A'
    else:
        firstmatch = ia.search_movie(movie)[0]
        ia.update(firstmatch)
        for v in values2:
            if firstmatch.has_key(v) == 1:
                additional2[movie].append(firstmatch[v])
            elif firstmatch.has_key(v) == 0:
                additional2[movie].append('N/A')
'''

