import discord
from discord import app_commands
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="userinfo", description="Get user info")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):

        member = member or interaction.user

        embed = discord.Embed(
            title=f"{member.name}",
            color=discord.Color.purple()
        )
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%d %b %Y"))
        embed.add_field(name="Account Created", value=member.created_at.strftime("%d %b %Y"))

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(UserInfo(bot))