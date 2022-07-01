import discord
from discord.ext import commands
from ..db import db
from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

COGS = ["builds", "guilds"]

class Ready(object):
  def __init__(self):
    for cog in COGS:
      setattr(self, cog, False)

  def ready_up(self, cog):
    setattr(self, cog, True)
    print(f" {cog} cog ready")

  def all_ready(self):
    return all([getattr(self, cog) for cog in COGS])

class MyBot(commands.Bot):

    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        db.autosave(self.scheduler)

        self.ready = False

        super().__init__(
        command_prefix = 'aery ',
        intents = discord.Intents.all(),
        application_id = 989739264747139103
        )

    async def setup_hook(self):
        for cog in COGS:
            await self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog loaded")

        print("setup complete")
        await bot.tree.sync()

    def update_db(self):
        db.multiexec("INSERT OR IGNORE INTO guildinfo (GuildID) VALUES (?)",
    					 ((guild.id,) for guild in self.guilds))

        for guild in self.guilds:
            db.execute("UPDATE guildinfo SET GuildName = ?, GuildSize = ? WHERE GuildID = ?",
            guild.name, guild.member_count, guild.id)

        db.commit()

        to_remove = []
        stored_guilds = db.column("SELECT GuildID FROM guildinfo")
        for id_ in stored_guilds:
          if not self.guilds:
            to_remove.append(id_)

        db.multiexec("DELETE FROM guildinfo WHERE GuildID = ?",
    					 ((id_,) for id_ in to_remove))

        db.commit()

    async def on_ready(self):
        if not self.ready:

            log_channel = self.get_channel(991742125471432776)
            await log_channel.send('Estoy lista, estoy lista, estoy lista!')

            self.scheduler.start()
            self.update_db()

            self.ready = True

            game = discord.Game("/help or aery help")
            await self.change_presence(status=discord.Status.online, activity=game)
        else:
            print("aery reconnected")
bot = MyBot()
