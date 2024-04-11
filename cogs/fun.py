import discord
from discord.ext import commands
from discord import app_commands

from cogs.utils.avatar_mods import AvatarMods
from cogs.utils.executor import in_executor

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(name="8bit")
    @app_commands.describe(member="The member to convert the avatar of.")
    async def eight_bit(self, interaction: discord.Interaction,  member: discord.Member = None):
        """Converts the avatar to an 8-bit version."""
        if member:
            avatar_bytes = await member.avatar.replace(size=1024).read()
        else:
            avatar_bytes = await interaction.user.avatar.replace(size=1024).read()

        avatar = await in_executor(
            AvatarMods.apply_effect,
            avatar_bytes,
            AvatarMods.eight_bit_effect,
            "8bit.png",
        )
        
        embed = discord.Embed(
            title="Here's your 8-bit avatar!",
            color=discord.Color.blue(),
        )
        embed.set_footer(
            text=f"Requested by: {interaction.user}", icon_url=interaction.user.avatar.url
        )
        embed.set_image(url=f"attachment://8bit.png")
        
        await interaction.response.send_message(embed=embed, file=avatar)

    @app_commands.command(name="pixelate")
    @app_commands.describe(member="The member to convert the avatar of.")
    async def pixelate(self, interaction:discord.Interaction, distortion: int, member: discord.Member = None):

        if member:
            avatar_bytes = await member.avatar.replace(size=1024).read()
        else:
            avatar_bytes = await interaction.user.avatar.replace(size=1024).read()

        avatar = await in_executor(
            AvatarMods.apply_effect,
            avatar_bytes,
            AvatarMods.pixelate,
            "8bit.png",
            distortion,
        )
        embed = discord.Embed(
            title="Here's your pixelated avatar!",
            color=discord.Color.blue(),
        )
        embed.set_footer(
            text=f"Requested by: {interaction.user}", icon_url=interaction.user.avatar.url
        )
        embed.set_image(url=f"attachment://8bit.png")
        await interaction.response.send_message(embed=embed, file=avatar)

async def setup(bot):
    await bot.add_cog(Fun(bot))