import discord
from discord.ext import commands
from discord import app_commands


class Nasa(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="apod", description="Get the Astronomy Picture of the Day."
    )
    @app_commands.checks.cooldown(1, 3600, key=lambda i: i.guild_id)
    async def get_apod(self, interaction: discord.Interaction):
        """Get the Astronomy Picture of the Day."""
        URL = f"https://api.nasa.gov/planetary/apod?api_key={self.bot.nasa_api_key}"
        async with self.bot.http_session.get(
            URL,
            headers={"Content-Type": "application/json"},
        ) as response:
            data = await response.json()

        embed = discord.Embed(
            title=data["title"],
            description=data["explanation"],
            color=discord.Color.blue(),
        )
        embed.set_image(url=data["url"])
        embed.set_footer(
            text=f"Requested by: {interaction.user} - {data['date']}",
            icon_url=interaction.user.avatar.url,
        )

        await interaction.response.send_message(embed=embed)

    @get_apod.error
    async def reminder_set_error(
        self, interaction: discord.Interaction, error: app_commands.AppCommandError
    ):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f"Command is on cooldown. Retry in {round(error.retry_after)} seconds.",
                ephemeral=True,
            )
app_commands
    app_commands.command(name="test", description="Test command for neovim")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hola, soy una prueba")

async def setup(bot):
    await bot.add_cog(Nasa(bot))
