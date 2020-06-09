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
 
#Creating a dataframe
df=pd.DataFrame([tweet.full_text for tweet in tweets],columns=['tweets'])

#Printing the dataframe
df.head()

#Cleaning the data
def cleantext(text):
 text=re.sub("@[A-Za-z0-9]+", '', text)
 text=re.sub("#", '', text)
 text=re.sub('RT[\s]+', '', text)
 text=re.sub("https?:\/\/\S+",'',text)
 return text

#Redefined text dataframe
df['tweets']=df['tweets'].apply(cleantext) 

#printing dataframe(redefined)
df.head()

#Convering to a list
texts=df['tweets'].to_list()
print(df['tweets'].to_list())

#Calling translation function 
translator = Translator()

type(texts[3])
curr = ''.join([i if ord(i) < 128 and i!=';' else ' ' for i in texts[2]])
curr = "".join(curr.split('\n'))

text2 = '_shahkar: Treating Corona Patients + Fasting + Performing SalahMay Allah keep all doctors healthy alive    coronavirus https '

print(curr)
answer = translator.translate(curr)
print(answer.text)

answer= []
for i in range(len(texts)) :
    curr = ''.join([i if ord(i) < 128 and i!=';' else ' ' for i in texts[i]])
    curr = "".join(curr.split('\n'))
    answer.append(translator.translate(curr).text)
print(answer)

#Printing the traslated Dataframe
print(translations)
print(type(translations))

