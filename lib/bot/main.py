import discord
from discord.ext import commands

COGS = ["aram"]

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

        super().__init__(
        command_prefix = 'aery',
        intents = discord.Intents.all(),
        application_id = 989739264747139103
        )

    async def setup_hook(self):
        for cog in COGS:
            await self.load_extension(f"cogs.{cog}")
            print(f" {cog} cog loaded")

        print("setup complete")
        await bot.tree.sync()

    async def on_ready(self):
        print(f"{self.user} está conectada!")

with open('.env', 'r', encoding='utf-8') as f:
    token = f.read()

bot = MyBot()
bot.run(token)
