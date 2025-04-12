#!/bin/bash

# Usage: ./run_reddit.sh subreddit_name [limit]

SUBREDDIT=$1
LIMIT=${2:-5}  # Default to 5 if not provided

if [ -z "$SUBREDDIT" ]; then
  echo "Please provide a subreddit name!"
  echo "Usage: ./run_reddit.sh subreddit_name [limit]"
  exit 1
fi

# Activate virtualenv if needed
source venv/bin/activate

# Run the Python CLI
python reddit_cli.py "$SUBREDDIT" --limit "$LIMIT"
