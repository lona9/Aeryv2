import discord
from discord import app_commands
from discord.ext import commands
from ..db import db
import pendulum
import datetime
from datetime import datetime
from discord import Embed

class info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot(help_command=None) = bot
        self.bot.remove_command("help")

    @commands.hybrid_command(name = "help",
    description = "Bot general information.")
    async def ayuda(self, ctx: commands.Context) -> None:

        date = "31/07/2022"

        parche = "12.14"

        try:
            language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

            language = str(language[0])

        except:
            language = "SP"

        if language == 'EN':

            embed = Embed(title="Aery Information")

            fields = [("\u200B", "Type `/commands` to see what Aerybot can do. Type `/language` inside a server to change its language.", False),

            ("\u200B", f"**Aerybot** wants to make it easier and faster to get builds and runes to play League of Legends. It's updated once a week, and all information is obtained from the most popular, with higher win rate builds according to League of Graphs.\n\nThis bot was updated on **{date}**.\n\nLos datos fueron obtenidos de League of Graphs, for All Regions, Platinum+, **patch {parche}**.\n\nIf you want to invite this bot to another server, you can use [this link.](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)\n\nIf you liked this bot, consider buying the creator a [kofi.](https://www.ko-fi.com/lona9)", False)]

            for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
            embed.set_footer(text="If you have any issues, or need more help, message lona#4817")

            await ctx.send(embed=embed)

        elif language == 'PT':

            embed = Embed(title="Informação de Aery")

            fields = [("\u200B", "`ATENÇÃO`: **O Aerybot agora funciona apenas com comandos de barra, devido às alterações do Discord para bot development.**\nEscreva `/commands` para ver o que pode fazer Aerybot. Escreva `/language*`dentro de um servidor para mudar o idioma.", False),
            ("\u200B", f"**Aerybot** quer fazer mais fácil e rápida a busca de builds e runas para jogar League of Legends. Se atualiza uma vez por semana, e toda a informação é obtida das runas e builds mais populares e com melhor winrate de acordo com League of Graphs.\n\nEsse bot foi atualizado pela última vez no **{date}**.\n\nOs dados e builds foram obtidos de League of Graphs, para Todas as regiões, Platino+, **parche {parche}**.\n\nSe você quiser convidar o bot para outro server, pode fazê-lo com [esse link.](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)\n\nSe você curtiu esse bot, considere comprar um [kofi](https://www.ko-fi.com/lona9) para a criadora.", False)]

            for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
            embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

            await ctx.send(embed=embed)

        else:

            embed = Embed(title="Información de Aery")

            fields = [("\u200B", "`ATENCIÓN`: **Aerybot ahora solo funciona con slash commands, debido a los cambios de Discord para desarrollar bots.**\nEscribe `/commands` para ver qué puede hacer Aerybot. Escribe `/language` dentro de un servidor para cambiar el idioma. / Escreva `/language`dentro de um servidor para mudar o idioma. / Type `/language` inside a server to change its language.", False),
            ("\u200B", f"**Aerybot** quiere hacer más fácil y rápida la búsqueda de builds y runas para jugar League of Legends. Se actualiza una vez por semana, y toda la información es obtenida de las runas y builds más populares y con mejor winrate de acuerdo a League of Graphs.\n\nEste bot fue actualizado por ultima vez el **{date}**.\n\nLos datos y builds fueron obtenidos de League of Graphs, para Todas las regiones, Platino+, **parche {parche}**.\n\nSi quieres invitar a este bot a otro server, puedes hacerlo con [este link.](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)\n\nSi te gustó este bot, considera comprar un [kofi](https://www.ko-fi.com/lona9) a la creadora.", False)]

            for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
            embed.set_footer(text="Si presento problemas o necesitas más ayuda, envía un mensaje a lona#4817")

            await ctx.send(embed=embed)

        try:
            guild_id = ctx.guild.id
            guild_name = ctx.guild.name

        except:
            guild_id = 'DM'
            guild_name = 'DM'

        finally:
            tz = pendulum.timezone('America/La_Paz')
            event_date = datetime.now(tz)

            db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command) VALUES (?, ?, ?, ?)",
            event_date, guild_id, guild_name, 'help')
            db.commit()

            self.logs = self.bot.get_channel(991742125471432776)
            await self.logs.send(f"aery help, guild: {guild_name}")


    @commands.hybrid_command(name = "commands",
    description = "List of commands.")
    async def commandlist(self, ctx: commands.Context) -> None:
        try:
            language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

            language = str(language[0])

        except:
            language = "SP"

        if language == 'EN':
            embed = Embed(title="Command List")

            fields = [("\u200B", "These are the available commands you can use:", False),
            ("\u200B", ":small_blue_diamond: `/aram <champ`: Type command + name of the camp to see its stats and builds for ARAM games (e.g: `/aram ashe`).\n:small_blue_diamond: `/normal <champ>`: Type command + name of the champ to see its stats and builds for Normal games (e.g: `/normal ashe`). \nIf the champion has more than one position, you can type the position after the name to see specific builds. Use abbreviated position names (mid, top, adc, supp, jg). E.g: `/normal ekko jg`. If you use the command without a position argument, it'll show the average build considering all positions.", False),
            ("\u200B", ":small_blue_diamond: `/language`: Change the language of Aery to spanish/portuguese/english. (Only works inside servers, not DMs).\n:small_blue_diamond: `/help`: General information of the bot.\n:small_blue_diamond: `/invite`: Sends the link to invite Aery to other servers.", False),
            ("\u200B", "Commands must be written in lower case. Names of champions can be written in any case, with or without spaces or special characters. Each champ has a set of accepted names, including their most common abbreviations.", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
            embed.set_footer(text="If you have any issues, or need more help, message lona#4817")

            await ctx.send(embed=embed)

        elif language == 'PT':
            embed = Embed(title="Lista de comandos")

            fields = [("\u200B", "Esses são os comandos que você pode usar e suas funções:", False),
            ("\u200B", ":small_blue_diamond: `/aram <champ>`: Escrever comando + nome do champ para ver suas stats e builds para partidas ARAM (ej: /aram ashe`).\n:small_blue_diamond: `/normal <champ>`: Escrever comando + nome do champ para ver suas stats e builds para partidas normais (ej: `/normal ashe`).\nSe o champ tiver mais de uma posição, você pode escrever a posição depois do nome para ver as stats específicas. Usar os nomes abreviados (mid, top, adc, supp, jg). Por exemplo, escrever: `/normal ekko jg`. O comando sem posição no final vai mostrar a informação média para o champ considerando todas as posições.", False),
            ("\u200B", ":small_blue_diamond: `/language`: Usa esse comando para mudar a língua do bot a português/espanhol/inglês (Apenas dentro de um servidor, sem DM).\n:small_blue_diamond: `/help`: Informação geral do bot.\n:small_blue_diamond: `/invite`: Envia o link para convidar a Aery a outros servers.", False),
            ("\u200B", "Comandos devem ser escritos com letras minúsculas. Os nomes dos champs se podem escrever com ou sem maiúsculas, com ou sem espaços, e com ou sem caráteres especiais. Cada champ tem um set de nomes aceitos, que inclui as abreviações mais comuns.", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
            embed.set_footer(text="Se eu apresentar problemas ou você precisa de mais ajuda, envie uma mensagem a lona#4817")

            await ctx.send(embed=embed)

        else:
            embed = Embed(title="Lista de comandos")

            fields = [("\u200B", "Estos son los comandos que puedes utilizar y sus funciones:", False),
            ("\u200B", ":small_blue_diamond: `/aram <champ>`: Escribir comando + nombre del champ para ver sus stats y builds para partidas ARAM (ej: `/aram ashe`).\n:small_blue_diamond: `/normal <champ>`: Escribir comando + nombre del champ para ver sus stats y builds para partidas normales (ej: `/normal ashe`). \nSi el champ tiene más de una posición, puedes escribir la posición después del nombre para ver las stats específicas. Usar los nombres abreviados (mid, top, adc, supp, jg). Por ejemplo, escribir: `/normal ekko jg`. El comando sin posición al final mostrará la información promedio para el champ considerando todas las posiciones.", False),
            ("\u200B", ":small_blue_diamond: `/language`: Cambia el idioma de Aery a español/portugués/inglés (solo dentro de un server, no en DM).\n:small_blue_diamond: `/help`: Información general del bot.\n:small_blue_diamond: `/invite`:  Envía el link para invitar a Aery a otros servers.", False),
            ("\u200B", "Comandos deben ser escritos en minúsculas. Los nombres de champs se pueden con o sin mayúsculas, con o sin espacios, y con o sin caracteres especiales. Cada champ tiene un set de nombres aceptados, que incluye las abreviaciones más comunes.", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            embed.set_author(name='Aerybot', icon_url="https://cdn.discordapp.com/attachments/827220123299086447/827222701349404771/Summon_Aery_rune.png")
            embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a lona#4817")

            await ctx.send(embed=embed)

        try:
            guild_id = ctx.guild.id
            guild_name = ctx.guild.name

        except:
            guild_id = 'DM'
            guild_name = 'DM'

        finally:
            tz = pendulum.timezone('America/La_Paz')
            event_date = datetime.now(tz)

            db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command) VALUES (?, ?, ?, ?)",
            event_date, guild_id, guild_name, 'commands')
            db.commit()

            self.logs = self.bot.get_channel(991742125471432776)
            await self.logs.send(f"aery commands, guild: {guild_name}")

    @commands.hybrid_command(name = "invite",
    description = "Get an invite link.")
    async def invite(self, ctx: commands.Context) -> None:
        try:
            language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

            language = str(language[0])

        except:
            language = "SP"


        if language == 'EN':
            await ctx.send("You can invite Aery to other servers using [this link.](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)")

        elif language == 'PT':
            await ctx.send("Você pode convidar Aery para outros servidores com o [seguinte link.](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)")

        else:
            await ctx.send("Puedes invitar a Aery a otros servers con el [siguiente link.](https://discord.com/api/oauth2/authorize?client_id=804475973579833374&permissions=8&scope=bot%20applications.commands)")

        try:
            guild_id = ctx.guild.id
            guild_name = ctx.guild.name

        except:
            guild_id = 'DM'
            guild_name = 'DM'

        finally:
            tz = pendulum.timezone('America/La_Paz')
            event_date = datetime.now(tz)

            db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command) VALUES (?, ?, ?, ?)",
            event_date, guild_id, guild_name, 'invite')
            db.commit()

            self.logs = self.bot.get_channel(991742125471432776)
            await self.logs.send(f"aery invite, guild: {guild_name}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(info(bot))
