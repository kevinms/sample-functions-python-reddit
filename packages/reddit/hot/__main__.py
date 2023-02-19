import praw
import os

def main(args):

  reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent="my user agent",
  )

  titles = []
  for submission in reddit.subreddit("godot").hot(limit=10):
    print(submission.title)
    titles.append(submission.title)

  return {
    'body': {
        'hot_titles': titles
      }
    }
