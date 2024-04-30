import discord
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(name="silksong")
    async def silksong_release_date(self, interaction: discord.Interaction):
        """Returns embed with Official Silksong release date 🤡."""
        embed = discord.Embed(
            title="Silksong release date! 🤡",
            description="Silksong will release in: <t:1739588400:R>",
            color=discord.Color.blue(),
        )
        embed.set_footer(
            text=f"Requested by: {interaction.user}", icon_url=interaction.user.avatar.url
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Misc(bot))