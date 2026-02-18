import discord
from discord import app_commands
from discord.ext import commands
import feedparser

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="news", description="Get latest tech news")
    @app_commands.describe(topic="Enter a topic (AI, blockchain, etc)")
    async def news(self, interaction: discord.Interaction, topic: str):

        await interaction.response.defer()

        url = f"https://news.google.com/rss/search?q={topic}+technology"
        feed = feedparser.parse(url)

        if not feed.entries:
            await interaction.followup.send("No news found.")
            return

        entry = feed.entries[0]

        embed = discord.Embed(
            title=entry.title,
            description=entry.summary[:300] + "...",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Powered by Google News RSS")

        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(News(bot))