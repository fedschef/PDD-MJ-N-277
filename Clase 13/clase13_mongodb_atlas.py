#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:45:30 2021

@author: fedschef
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:52:12 2021

@author: fedschef
"""
import tweepy
import json
import pprint
from pymongo import MongoClient

# Project:
# Api Key
# lgjiYaTNwVMhw2ANbmxDwhYwc
# Api Secret Key
# OHUlPPySfSe3K4JEPlBEXOTlAjq1JdKpxaDaXqdTIoQvgQnL7e
# Bearer token
# AAAAAAAAAAAAAAAAAAAAAB2WPQEAAAAArLppA8TWW3UGga6W%2BStT09Px0p0%3Dkx3vnB8lKrJvSG0SLwN4R0mFtTP1F6GdY2M0eIwUeFqKKmPb8k


# App
# API Key:
# Lud8kaOaR0Xxgy7U5PbnLdVvf
# API Secret Key:
# D3Ud3wN38acCgess4xvYoQvPzuRlBhhJQ980wLWbQe5a9k9sz6
# Access Token:
# 1124453217897783296-JsISVSJWnVMCfqql28zAsFE0MKwyGO
# Access Token Secret:
# wvT7ifboZCqf9aNfLdKosyLJhvzcSZb7AzEvU6IVXSRSG

consumer_key = "Lud8kaOaR0Xxgy7U5PbnLdVvf"
consumer_secret_key = "D3Ud3wN38acCgess4xvYoQvPzuRlBhhJQ980wLWbQe5a9k9sz6"
access_token = "1124453217897783296-JsISVSJWnVMCfqql28zAsFE0MKwyGO"
access_token_secret = "wvT7ifboZCqf9aNfLdKosyLJhvzcSZb7AzEvU6IVXSRSG"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

cliente = MongoClient("mongodb://localhost:27017")
user = "federico"
password = "1234"
server = "datacluster.sggre.mongodb.net"
databse = "bigdata"


url = "mongodb+srv://federico:"+password+"@clusterpdd.esivo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)


bd = client['bigdata']
coleccion = bd['tweets']
tweets = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name = 'eanttech', tweet_mode = 'extended').items(500):
    tweet_dict = tweet._json
    tweets.append(tweet_dict)
    print("tweet capturado",tweet._json['full_text'])
coleccion.insert_many(tweets)
                  


#%% 
#Alternativa, solo inserta tweets que son posteriores al ultimo en la BD
# Para esto, primero buscamos el tweet mas reciente (el de menor id)                  
 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:45:30 2021

@author: fedschef
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:52:12 2021

@author: fedschef
"""
import tweepy
import json
import pprint
from pymongo import MongoClient

# Project:
# Api Key
# lgjiYaTNwVMhw2ANbmxDwhYwc
# Api Secret Key
# OHUlPPySfSe3K4JEPlBEXOTlAjq1JdKpxaDaXqdTIoQvgQnL7e
# Bearer token
# AAAAAAAAAAAAAAAAAAAAAB2WPQEAAAAArLppA8TWW3UGga6W%2BStT09Px0p0%3Dkx3vnB8lKrJvSG0SLwN4R0mFtTP1F6GdY2M0eIwUeFqKKmPb8k


# App
# API Key:
# Lud8kaOaR0Xxgy7U5PbnLdVvf
# API Secret Key:
# D3Ud3wN38acCgess4xvYoQvPzuRlBhhJQ980wLWbQe5a9k9sz6
# Access Token:
# 1124453217897783296-JsISVSJWnVMCfqql28zAsFE0MKwyGO
# Access Token Secret:
# wvT7ifboZCqf9aNfLdKosyLJhvzcSZb7AzEvU6IVXSRSG

consumer_key = "Lud8kaOaR0Xxgy7U5PbnLdVvf"
consumer_secret_key = "D3Ud3wN38acCgess4xvYoQvPzuRlBhhJQ980wLWbQe5a9k9sz6"
access_token = "1124453217897783296-JsISVSJWnVMCfqql28zAsFE0MKwyGO"
access_token_secret = "wvT7ifboZCqf9aNfLdKosyLJhvzcSZb7AzEvU6IVXSRSG"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


sort=list({'id': -1}.items())
cliente = MongoClient("mongodb://localhost:27017")
bd = cliente['bigdata']
coleccion = bd['tweets']
ultimo = coleccion.find_one(sort = sort)
if ultimo != None:
    ultimo_tweet_id = ultimo['id']
else:
    ultimo_tweet_id = None    

tweets = []
contador = 0    
for tweet in tweepy.Cursor(api.user_timeline, since_id = ultimo_tweet_id, screen_name = 'alferdez', tweet_mode = 'extended').items(50):
    tweet_dict = tweet._json
    tweets.append(tweet_dict)
#    print("tweet capturado",tweet._json['full_text'])
    contador += 1
if len(tweets)>0:
    coleccion.insert_many(tweets)
    print("Se han insertado "+str(contador)+" tweets")
else:
    print("No hay nuevos tweets")    
                  



                 



client = pymongo.MongoClient("mongodb+srv://federico:<password>@clusterpdd.esivo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test