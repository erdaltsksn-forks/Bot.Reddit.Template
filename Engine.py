#!/usr/bin/python
#Required
import random
import requests
import pdb
import os
import praw
import re
from content import quotes
import logging
from datetime import datetime

#################################################################
#################################################################
######################    Configurables   #######################
#################################################################
#################################################################
#These variables are what need to be configured in order for your bot to function
#Reddit Authentication

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

bot_username = ["","B0tRank"]   #Bot's username, because I'm too lazy to pull it from reddit.
target_sub = ""    #Where the bot looks for the words
subreddit = reddit.subreddit(target_sub)    #Making the code look prettier.

keywords = ("")  #Words the bot looks for
#Started, bot rater detected, good bot detected, bad bot detected, something to say for non-useful data
consoleoutput = ["","Ignoring comments from the bot rater...","Thanking a voter!","Apoligizing and deleting.",""]    #Strings to print to the console to help with general awareness
healthchecks = "https://hc-ping.com/410095e0-2d5f-455b-b365-1544106980b1"   #Ping checker for uptime.  https://healthchecks.io/ is an awesome resource.
timeout = 10
j=0

data_file = ["comment_list.txt","bot_ratings.txt"]  #Persistant storage
rating_report = ["Time: ","Comment ID","Comment Body","Comment Link","Parent ID","Parent Body","Parent Link"]

bot_feedback = (
                ('good bot','Thank you!'),
                ('bad bot','Sorry about that.')
                )

#################################################################
#################################################################
##################    Some Initialization   #####################
#################################################################
#################################################################
#This is what runs the bot.  It runs until you stop it, or it crashes.

#Configure logging, but doesn't seem to do much...
logging.basicConfig(
     filename=(bot_username[0]+".log"),
     level=logging.INFO, 
     format= '[%(asctime)s] (%(pathname)s:%(lineno)d) %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )

#Check if Comments File exists
if not os.path.isfile(data_file[0]):
    #Initialize array if it doesn't exist
    comments_processed = []
else:
    #Read commands into array if it exists
    with open(data_file[0], "r") as f:
        comments_processed = f.read()
        comments_processed = comments_processed.split("\n")
        comments_processed = list(filter(None, comments_processed))
  
#Start abiding  
print(consoleoutput[0])

#################################################################
#################################################################
######################    Primary Loop   ########################
#################################################################
#################################################################
#This is what runs the bot.  It runs until you stop it, or it crashes.
#This is all configured already, don't need to fuss with it unless you want to.

#Runs for the last 100 comments / any new comments
for comment in subreddit.stream.comments(): 
    requests.get(healthchecks, timeout=timeout) #Pings HealthChecks.io for uptime alerts
    lower_body = comment.body.lower()   #Casts the body to lowercase
    i=0

    #Ignore comments from the Bot Rater
    if comment.author == bot_username[1] and bot_username[0] in comment.body.lower() and comment.id not in comments_processed:
        print(consoleoutput[1])
        #Append ID to Processed list
        comments_processed.append(comment.id)  
        #Log comment in reply list
        with open(data_file[0], "w") as f: 
            for comment_id in comments_processed:
                f.write(comment_id + "\n")    
         
    #Respond to bot votes
    for i in range(2):
        #Body = good/bad bot, comment ID isn't in the list, and parent author is me
        if (lower_body == bot_feedback[i][0]) and (comment.id not in comments_processed) and (bot_username[0] in str((reddit.comment(comment.id).parent()).author)):
            #Notify console
            print(consoleoutput[i+2])
            #Reply to the user's rating with either a thanks or an apology
            comment.reply(bot_feedback[i][1])
            #Append ID to processed list
            comments_processed.append(comment.id)
            #Open our text file and replace its contents with the comments_processed variable.
            with open(data_file[0], "w") as f:  
                for comment_id in comments_processed:
                    f.write(comment_id + "\n")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            #Write comment information to the ratings file to track good and bad stuff
            with open(data_file[1], "a") as f: 
                f.write(rating_report[0]+ dt_string + "\n\n")	
                f.write(rating_report[1]+comment.id + "\n")
                f.write(rating_report[2]+comment.body + "\n")
                f.write(rating_report[3]+comment.permalink + "\n")
                f.write(rating_report[4]+reddit.comment(comment.id).parent().id + "\n")
                f.write(rating_report[5]+reddit.comment(comment.id).parent().body + "\n")
                f.write(rating_report[6]+reddit.comment(comment.id).parent().permalink + "\n\n\n\n")
            #Delete the comment if it has less than ten upvotes and gets a bad bot
            if reddit.comment(comment.id).parent().score < 10 and bot_feedback[1][0] in comment.body:
                print(consoleoutput[4])
                reddit.comment(comment.id).parent().delete()
                
    #Run through other comments
    else:
        for i in keywords:  #Go through all variables in keywords[] array
            if i in lower_body and comment.id not in comments_processed and comment.author != bot_username[0]: #If the body has a keyword, it hasn't been processed, and it's not me 
                print("User: ",comment.author,"\n","Body: :",comment.body,"\n","Link: ",comment.link_permalink,"\n\n\n") #Dump URL to console
                comment.reply(random.choice(quotes)) #Reply with a quote!
                comments_processed.append(comment.id)  #Append ID to Processed list
                with open(data_file[0], "w") as f:  #Open our text file and replace its contents with the comments_processed variable.
                    for comment_id in comments_processed:
                        f.write(comment_id + "\n")
            else:
                print(j,consoleoutput[4])
                j = j+1