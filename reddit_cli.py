import praw
import os
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# CLI arguments
parser = argparse.ArgumentParser(description="Fetch latest Reddit posts from a subreddit.")
parser.add_argument("subreddit", help="Subreddit name to fetch posts from")
parser.add_argument("--limit", type=int, default=5, help="Number of posts to fetch (default: 5)")
args = parser.parse_args()

# Init Reddit client
try:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    subreddit = reddit.subreddit(args.subreddit)

    print(f"\nFetching {args.limit} latest posts from r/{args.subreddit}...\n")
    for post in subreddit.new(limit=args.limit):
        print(f"Title: {post.title}")
        print(f"Author: {post.author}")
        print(f"Upvotes: {post.score}")
        print("-" * 40)

except Exception as e:
    print("Something went wrong!")
    print(e)
