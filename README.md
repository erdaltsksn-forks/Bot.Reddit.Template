# Reddit Bot Skeleton<br>
This can be pretty easily converted into a functional bot.  Need to configure the following:<br><br>

reddit = praw.Reddit(<br>
    client_id="CLIENT_ID",<br>
    client_secret="CLIENT_SECRET",<br>
    password="BOT PASSWORD",<br>
    user_agent="BOT USER AGENT",<br>
    username="BOT USERNAME",<br>
)<br><br>

#variables<br>
keywords = {"KEYWORD01","KEYWORD02","KEYWORD03"}  #Words the bot looks for<br>
target_sub = "SUBNAME"    #Where the bot looks for the words<br>
confirmation = "HELLO WORLD!" #String to print to the console to track when the script starts<br>
comments_file = "FILENAME"  #Comment IDs that have been replied to already are stored here.<br>
bot_username = "BOT USERNAME"   #Bot's username, because I'm too lazy to pull it from reddit.<br>
<br><br>

After configuring, the bot will crawl the Comments Stream of the subreddit.  This gives you the most recent 100 comments.<br>  
The bot looks at the comments to see if they've been responded to already, and makes sure they're not comments that it posted itself<br>
If the comment includes a keyword, the bot will pull a quote from the content.py file and post it<br>
Lastly it adds the comment ID to a list to ensure it doesn't double comment.<br>