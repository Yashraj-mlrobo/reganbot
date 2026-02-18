import os
import discord
import feedparser
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Must be set in Railway

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

RSS_URL = "https://techcrunch.com/feed/"
last_link = None


# ===== LOAD COGS =====
async def load_extensions():
    for file in os.listdir("./commands"):
        if file.endswith(".py") and file != "__init__.py":
            await bot.load_extension(f"commands.{file[:-3]}")
            print(f"Loaded {file}")


# ===== EVENTS =====
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")
    print("Bot is ready.")
    post_tech_news.start()


# ===== AUTO TECH NEWS =====
@tasks.loop(minutes=30)
async def post_tech_news():
    global last_link

    feed = feedparser.parse(RSS_URL)
    channel = bot.get_channel(CHANNEL_ID)

    if channel is None:
        print("Channel not found!")
        return

    for entry in feed.entries[:5]:
        if entry.link != last_link:
            message = f"📰 **Latest Tech News**\n\n{entry.title}\n{entry.link}"
            await channel.send(message)
            last_link = entry.link
            break


# ===== MAIN RUNNER =====
async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


if __name__ == "__main__":
    print("Token loaded:", TOKEN is not None)
    asyncio.run(main())