import discord
from discord import app_commands
from discord.ext import commands
from ..db import db

class builds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name = "aram",
    description = "Get champ information for ARAM games.")
    async def aram(self, ctx: commands.Context, champ: str) -> None:

        if champ != 'ashe':
            await ctx.send(
            f"Aquí están las runas para {champ}!"
            )
        else:
            await ctx.send("Revisa lo que escribiste!")

            self.testchannel = self.bot.get_channel(827220123299086447)

        await ctx.send(language)


    @app_commands.command(name = "normal",
    description= "Get champ information for Normal games.")
    async def normal(self, interaction: discord.Interaction, champ:str) -> None:
        await interaction.response.send_message(f"Aquí estás las runas para {champ} (NORMAL)")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(builds(bot))
