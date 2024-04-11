import os
import traceback
import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            intents=intents,
            command_prefix="!",
            case_insensitive=True,
            owner_id=534820059965685770,
        )

    async def load_extensions(self) -> None:
        print("Loading extensions...")
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cog = filename[:-3]
                try:
                    await self.load_extension(f"cogs.{cog}")
                except Exception as e:
                    traceback.print_exc()

    async def setup_hook(self) -> None:
        await self.load_extensions()

    async def on_ready(self) -> None:
        print("Bot Online!", f"Username: {self.user.name}\nUser ID: {self.user.id}")