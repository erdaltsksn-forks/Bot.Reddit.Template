#!/usr/bin/python
#Required
import random
import requests
import pdb
import os
import praw
import re
from responses import dude_quotes

#Reddit Authentication
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

#variables
keywords = []  #Words the bot looks for
target_sub = ""    #Where the bot looks for the words
subreddit = reddit.subreddit(target_sub)    #Making the code look prettier.
count = [0,0,0,0]
bot_username = ""

#Get count of keywords
for submission in subreddit.hot():
    for comment in submission.comments:
        if comment.author != bot_username:   
            lower_body = comment.body.lower() 
            for i in range(len(keywords)):
                if keywords[i] in lower_body:
                    count[i] = count[i]+1
                elif keywords[i] in lower_body:
                    count[i] = count[i]+1
                elif keywords[i] in lower_body:
                    count[i] = count[i]+1
                elif keywords[i] in lower_body:
                    count[i] = count[i]+1
for i in range(len(keywords)):
    one = keywords[i]
    three = count[i]
    two = " count: "
    four = "\n"
    print(one,two,three,four)
