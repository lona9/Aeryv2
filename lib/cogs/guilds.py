import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import Context
from ..db import db
import pendulum
import datetime
from datetime import datetime

class guilds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name = "guilds",
    description = "Number of guilds.")
    async def guilds(self, ctx: commands.Context) -> None:

        guilds = len(self.bot.guilds)

        await ctx.send(f"aery es parte de **{len(self.bot.guilds)}** servers.")
        

    @app_commands.command(name="language",
    description = "Elige el idioma de Aery / Escolha o idioma do Aery / Choose Aery's language.")
    @app_commands.choices(language = [
    Choice(name="Español", value="SP"),
    Choice(name="Portugues", value="PT"),
    Choice(name="English", value="EN")]
    )
    async def language(self, interaction: discord.Interaction, language: str) -> None:

        ctx = await Context.from_interaction(interaction)

        try:

            guild_id = ctx.guild.id
            tz = pendulum.timezone('America/La_Paz')
            event_date = datetime.now(tz)

            db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command, Arguments) VALUES (?, ?, ?, ?, ?)",
            event_date, guild_id, ctx.guild.name, 'language', language)

            db.execute("UPDATE languages SET GuildLang = ? WHERE GuildID = ?", language, ctx.guild.id)

            db.commit()

            if language == 'SP':
                await ctx.send(f"Aery ahora está en español.")

            elif language == 'PT':

                await ctx.send(f"Aery esta agora em portugues.")

            elif language == 'EN':

                await ctx.send(f"Aery is now in english.")

            else:
                await ctx.send(f"Debes escoger una opción válida / Você deve escolher uma opção válida / You must choose a valid option.")

        except:
            await ctx.send("Este comando solo puede ocuparse dentro de un servidor / Este comando só pode ser usado em um servidor / This command can only be used in a server.")


    @Cog.listener()
    async def on_guild_join(self, guild):
        self.logs = self.bot.get_channel(991742125471432776)

        eventmsg = f'aery se unió a {guild.name} ({guild.member_count} miembros)'

        await self.logs.send(eventmsg)

        db.execute("INSERT OR IGNORE INTO languages (GuildID, GuildName, GuildSize) VALUES (?, ?, ?)",
        guild.id, guild.name, guild.member_count)
        db.commit()

        tz = pendulum.timezone('America/La_Paz')
        event_date = datetime.now(tz)

        command = 'guild_join'

        db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command) VALUES (?, ?, ?, ?)",
        event_date, guild.id, guild.name, command)
        db.commit()

    @Cog.listener()
    async def on_guild_remove(self, guild):
        self.logs = self.bot.get_channel(991742125471432776)

        eventmsg = f'aery fue expulsada de {guild.name} ({guild.member_count} miembros)'

        await self.logs.send(eventmsg)

        db.execute("DELETE FROM languages WHERE GuildID = ?", guild.id)
        db.commit()

        tz = pendulum.timezone('America/La_Paz')
        event_date = datetime.now(tz)

        command = 'guild_remove'

        db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command) VALUES (?, ?, ?, ?)",
        event_date, guild.id, guild.name, command)
        db.commit()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(guilds(bot))
