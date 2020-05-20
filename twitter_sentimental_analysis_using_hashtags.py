# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:12:46 2020

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:12:46 2020

@author: HP
"""

#Importing the libraries
import tweepy
import re
import pandas as pd
import numpy as np
import spacy
from spacy import displacy

consumerKey={'fill in the credentials'}
consumerSecret={'fill in the credentials'}
accessToken={'fill in the credentials'}
accessTokenSecret={'fill in the credentials'}

#Function for user based of twitter
def twitter_set():
  #authenticating the credentails
  authenticate=tweepy.OAuthHandler(consumerKey, consumerSecret)

  #authenticating the access token
  authenticate.set_access_token(accessToken, accessTokenSecret)

  #Creating an API with authenitication
  api=tweepy.API(authenticate)
  return api

#tweet extractor
getTweets=twitter_set()

#etting the tweets using hashtags
tweets=getTweets.search(q="#Enter Hashtag (e.g.#avengers)", count={integer}, tweet_mode="extended")

print("Number of tweets extacted using # key: {}.\n".format(len(tweets)))

#In the above case you can either choose (tweet_mode) or not;
#If you use tweet_mode="extended" then to get the whole tweet use tweet.full_text
#If you don't use tweet_mode="extended" then to get the whole tweet use tweet.text

#printing the tweets
i=1
for tweet in tweets[0:50]:
  print(str(i)+ ') ' +  tweet.full_text)
  print()
  i=i+1
 
