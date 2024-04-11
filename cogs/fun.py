import discord
from discord.ext import commands

from cogs.utils.avatar_mods import AvatarMods
from cogs.utils.executor import in_executor

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="8bit")
    async def eight_bit(self, ctx, member: discord.Member = None):

        if member:
            avatar_bytes = await member.avatar.replace(size=1024).read()
        else:
            avatar_bytes = await ctx.author.avatar.replace(size=1024).read()

        async with ctx.typing():

            avatar = await in_executor(
                AvatarMods.apply_effect,
                avatar_bytes,
                AvatarMods.eight_bit_effect,
                "8bit.png",
            )

            embed = discord.Embed(
                title="8-bit avatar!",
                color=discord.Color.gold(),
            )
            embed.set_footer(
                text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar.url
            )
            embed.set_image(url=f"attachment://8bit.png")
            await ctx.send(embed=embed, file=avatar)

    @commands.command(name="pixelate")
    async def pixelate(self, ctx, distortion: int, member: discord.Member = None):

        if member:
            avatar_bytes = await member.avatar.replace(size=1024).read()
        else:
            avatar_bytes = await ctx.author.avatar.replace(size=1024).read()

        async with ctx.typing():

            avatar = await in_executor(
                AvatarMods.apply_effect,
                avatar_bytes,
                AvatarMods.pixelate,
                "8bit.png",
                distortion,
            )

            embed = discord.Embed(
                title="Pixelated avatar!",
                color=discord.Color.gold(),
            )
            embed.set_footer(
                text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar.url
            )
            embed.set_image(url=f"attachment://8bit.png")
            await ctx.send(embed=embed, file=avatar)


async def setup(bot):
    await bot.add_cog(Fun(bot))