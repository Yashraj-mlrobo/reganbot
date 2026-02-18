import discord
from discord import app_commands
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="about", description="About this bot")
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Tech News Bot",
            description="A powerful tech news Discord bot.",
            color=discord.Color.orange()
        )
        embed.add_field(name="Developer", value="Yashraj")
        embed.add_field(name="Hosted On", value="Railway")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(About(bot))