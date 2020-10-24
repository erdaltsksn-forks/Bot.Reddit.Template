# Reddit Bot Skeleton<br>
This can be pretty easily converted into a functional bot.  Need to configure the following items that are :<br><br>

reddit = praw.Reddit(<br>
    client_id="CLIENT_ID",<br>
    client_secret="CLIENT_SECRET",<br>
    password="BOT PASSWORD",<br>
    user_agent="BOT USER AGENT",<br>
    username="BOT USERNAME"<br>
)<br><br>

#variables<br>
bot_username = [YOURBOTUSERNAMEHERE,"B0tRank"]<br>   #Bot's username, because I'm too lazy to pull it from reddit.
target_sub = "SUBNAME"<br>    #Where the bot looks for the words
subreddit = reddit.subreddit(target_sub)<br>    #Making the code look prettier.

keywords = ()<br>  #Words the bot looks for
consoleoutput = ["NEEDFIVEOUTPUTS,CHECKCODE"]<br>    #Strings to print to the console to help with general awareness
healthchecks = "HTTP/URL.COM" <br>  #Ping checker for uptime.  https://healthchecks.io/ is an awesome resource.



After configuring, the bot will crawl the Comments Stream of the subreddit.  This gives you the most recent 100 comments.<br>  
The bot looks at the comments to see if they've been responded to already, and makes sure they're not comments that it posted itself<br>
If the comment includes a keyword, the bot will pull a quote from the content.py file and post it<br>
Lastly it adds the comment ID to a list to ensure it doesn't double comment.<br>

If you're not sure how to run this bot, it's super easy.  Just download the latest version of Python for your OS, make sure you select the option to add Python to the path, then open up a new cmd / powershell instance in the folder and execute "python engine.py"
