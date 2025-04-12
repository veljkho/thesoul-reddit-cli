# TheSoul Reddit CLI Tool

A simple Python CLI tool that fetches the latest posts from any subreddit using the Reddit API.

## Features

- Authenticates via Reddit OAuth using PRAW
- Fetches latest posts from any subreddit
- Prints title, author, and upvote count
- Supports custom post limits via CLI
- Works in a secure `.env`-based setup

---

## Requirements

- Python 3.x preinstalled on your machine
- Reddit account with API keys
- Bash terminal (macOS, Linux, WSL)

---

## Getting Started

### 1. Clone the Project

```bash
git clone https://github.com/veljkho/thesoul-reddit-cli.git
cd thesoul-reddit-cli
```

### 2. Add Your Reddit API Credentials

Copy `env.example` to `.env` and fill in your keys (or use existing from the example env):

```bash
cp env.example .env
```

Then edit `.env`:

```env
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=script by u/veljkho
```

> You can create your Reddit App here: https://www.reddit.com/prefs/apps

---

### 3. Run the Setup Script

```bash
chmod +x setup.sh run_reddit.sh
./setup.sh
```

This will:
- Create a virtual environment
- Install required dependencies (`praw`, `python-dotenv`)

---

### 4. Run the Tool

```bash
./run_reddit.sh subreddit_name [limit]
```

#### Examples:
```bash
./run_reddit.sh wordpress      # fetches 5 posts
./run_reddit.sh wordpress 10   # fetches 10 posts
```

---

## Project Structure

```
thesoul-reddit-cli/
├── reddit_cli.py        # Main Python CLI script
├── run_reddit.sh        # Bash runner script
├── setup.sh             # One-time environment setup
├── .env.example         # Environment variable template
└── README.md            # You’re reading it!
```

---

## Credits

Built with ❤️ using Python and [PRAW](https://praw.readthedocs.io/).

---
