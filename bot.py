import os
import discord
import feedparser
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

RSS_URL = "https://techcrunch.com/feed/"
last_link = None


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    post_tech_news.start()


@tasks.loop(minutes=30)
async def post_tech_news():
    global last_link
    
    feed = feedparser.parse(RSS_URL)
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("Channel not found!")
        return

    for entry in feed.entries[:5]:
        if entry.link != last_link:
            message = f"📰 **Latest Tech News**\n\n{entry.title}\n{entry.link}"
            await channel.send(message)
            last_link = entry.link
            break


client.run(DISCORD_TOKEN)