import discord
from discord import app_commands
from discord.ext import commands

class aram(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name = "aram",
    description = "Get champ information for ARAM games.")
    async def aram(self, interaction: discord.Interaction, champ: str) -> None:

        await interaction.response.send_message(
        f"Aquí están las runas para {champ}!"
        )

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(aram(bot))
