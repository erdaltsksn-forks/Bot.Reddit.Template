# Reddit Bot Skeleton

This can be pretty easily converted into a functional bot. Need to configure
the following items that are :

```python
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="BOT PASSWORD",
    user_agent="BOT USER AGENT",
    username="BOT USERNAME"
)
```

## Variables

- `bot_username` = [YOURBOTUSERNAMEHERE,"B0tRank"]
  - Bot's username, because I'm too lazy to pull it from reddit.
- `target_sub` = "SUBNAME"
  - Where the bot looks for the words.
- `subreddit` = reddit.subreddit(target_sub)
  - Making the code look prettier.
- `keywords` = []
  - Words the bot looks for.
- `consoleoutput` = ["NEEDFIVEOUTPUTS,CHECKCODE"]
  - Strings to print to the console to help with general awareness
- `healthchecks` = "HTTP/URL.COM"
  - Ping checker for uptime. [https://healthchecks.io/](https://healthchecks.io/)
    is an awesome resource.

After configuring, the bot will crawl the Comments Stream of the subreddit. This
gives you the most recent 100 comments.

The bot looks at the comments to see if they've been responded to already, and
makes sure they're not comments that it posted itself.

If the comment includes a keyword, the bot will pull a quote from the `content.py`
file and post it.

Lastly it adds the comment ID to a list to ensure it doesn't double comment.

## Usage

If you're not sure how to run this bot, it's super easy. Just download the latest
version of Python for your OS, make sure you select the option to add Python to
the path, then open up a new cmd / powershell instance in the folder and execute
the following command.

```bash
python engine.py
```
