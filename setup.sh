#!/bin/bash

# One-time setup script to create venv and install dependencies

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install praw python-dotenv

echo "🟢 Setup complete! Run './run_reddit.sh subreddit_name fetching_limit' to start."
