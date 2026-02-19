🚀 Tech News Discord Bot

A modular, multi-server Discord bot built with Python that delivers real-time tech news using slash commands and automated RSS feeds.

<hr>

✨ Features

Slash commands (/news, /userinfo, /serverinfo, /about)

Topic-based tech news search

Auto-posts latest tech news every 30 minutes

Multi-server support

Modular architecture using Cogs

Cloud deployment ready

Environment variable configuration

RSS-based news fetching (TechCrunch feed)

<hr>

🛠 Tech Stack

Python 3.13

discord.py

feedparser (RSS parsing)

Railway (cloud hosting)

<hr>

Project Structure
REGANBOT
├── bot.py
├── requirements.txt
├── commands/
│   ├── __init__.py
│   ├── news.py
│   ├── serverinfo.py
│   ├── userinfo.py
│   └── about.py

<hr>

⚙️ Setup (Local Development)

CLONE REPOSITORY
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

CREATE VIRTUAL ENVIRONMENT
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

INSTALL DEPENDECIES
pip install -r requirements.txt

CREATE .ENV FILE
DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=your_channel_id_here

RUN BOT
python bot.py

<hr>

DEPLOYMENT (Railway)
1) Push project to GitHub
2) Create new Railway project
3) Connect repository
4) Add environment variables:
    DISCORD_TOKEN
    CHANNEL_ID
5) Deploy

<hr>

🔐 Required Discord Settings

In Discord Developer Portal:

Enable Message Content Intent

Enable Server Members Intent

Add OAuth2 scopes:

bot

applications.commands

<hr>

📜 Slash Commands

| Command              | Description                     |
| -------------------- | ------------------------------- |
| `/news topic:<text>` | Get latest tech news on a topic |
| `/serverinfo`        | View server information         |
| `/userinfo`          | View user details               |
| `/about`             | About the bot                   |

<hr>

🧠 Lessons Learned

Proper environment variable management

Handling privileged intents

Avoiding multiple event loops

Modular command loading

Production debugging in cloud environments

<hr>

🔮 Roadmap

Per-server configuration system

Admin-set news channels

AI-generated article summaries

Button-based pagination

Database integration

<hr>

📬 Author

Built by Yas Raj Bhatnagar
Open to feedback and collaboration.

<hr>


