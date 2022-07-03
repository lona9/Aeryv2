import discord
from discord import app_commands
from discord.ext import commands
from ..db import db
import pendulum
import datetime
from datetime import datetime

class builds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name = "aram",
    description = "Get champ information for ARAM games.")
    async def aram(self, ctx: commands.Context, champ: str) -> None:

        if champ != 'ashe':
            await ctx.send(f"english english {champ}!")

            tz = pendulum.timezone('America/La_Paz')
            event_date = datetime.now(tz)

            try:
                guild_id = ctx.guild.id
            except:
                guild_id = 'DM'
            finally:
                db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command, Arguments) VALUES (?, ?, ?, ?, ?)",
                event_date, guild_id, ctx.guild.name, 'aram', champ)
                db.commit()

        else:
            await ctx.send("Revisa lo que escribiste!")


    @app_commands.command(name = "normal",
    description= "Get champ information for Normal games.")
    async def normal(self, interaction: discord.Interaction, champ:str) -> None:
        await interaction.response.send_message(f"Here are {champ}'s builds (NORMAL)")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(builds(bot))
