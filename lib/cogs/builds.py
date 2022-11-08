import discord
from discord import app_commands
from discord.ext import commands
from ..db import db
import pendulum
import datetime
from datetime import datetime
import os
from discord import Embed

class builds(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name = "aram",
    description = "Get champ information for ARAM games.")
    async def aram(self, ctx: commands.Context, champ: str) -> None:

        try:
            language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

            language = str(language[0])

        except:
            language = "SP"

        if champ == ():
            if language == 'EN':
                await ctx.send('¡You must type a champ name after `/aram`!')
            elif language == 'PT':
                await ctx.send('Você deve escrever o nome de um champ após `/aram`!')
            else:
                await ctx.send('¡Debes escribir el nombre de un champ después de `/aram`!')

        else:
            charsearch = "".join(champ).lower().replace("'", "").replace(".", "")

            champions = {"aatrox": ["aatrox"],
                  "ahri": ["ahri"],
                  "akali": ["akali"],
                  "akshan": ["akshan"],
                  "alistar": ["alistar"],
                  "amumu": ["amumu"],
                  "anivia": ["anivia"],
                  "annie": ["annie"],
                  "aphelios": ["aphelios"],
                  "ashe": ["ashe"],
                  "aurelionsol": ["aurelion", "sol", "aurelionsol"],
                  "azir": ["azir"],
                  "bard": ["bard", "bardo"],
                  "belveth": ["belveth", "bel"],
                  "blitzcrank": ["blitz", "blitzcrank"],
                  "brand": ["brand"],
                  "braum": ["braum"],
                  "caitlyn": ["cait", "caitlyn"],
                  "camille": ["camille"],
                  "cassiopeia": ["cassiopeia", "cassio", "cassi"],
                  "chogath": ["chogath", "cho"],
                  "corki": ["corki"],
                  "darius": ["darius"],
                  "diana": ["diana"],
                  "drmundo": ["drmundo", "mundo", "dr"],
                  "draven": ["draven"],
                  "ekko": ["ekko"],
                  "elise": ["elise"],
                  "evelynn": ["evelynn", "eve"],
                  "ezreal": ["ez", "ezreal"],
                  "fiddlesticks": ["fiddlesticks", "fiddle"],
                  "fiora": ["fiora"],
                  "fizz": ["fizz"],
                  "galio": ["galio"],
                  "gangplank": ["gangplank", "gang"],
                  "garen": ["garen"],
                  "gnar": ["gnar"],
                  "gragas": ["gragas"],
                  "graves": ["graves"],
                  "gwen": ["gwen"],
                  "hecarim": ["hecarim", "hec", "heca"],
                  "heimerdinger": ["heimerdinger", "heim", "heimer"],
                  "illaoi": ["illaoi"],
                  "irelia": ["irelia"],
                  "ivern": ["ivern"],
                  "janna": ["janna"],
                  "jarvaniv": ["jarvaniv", "jarvan"],
                  "jax": ["jax"],
                  "jayce": ["jayce"],
                  "jhin": ["jhin", "jihn", "jin"],
                  "jinx": ["jinx"],
                  "kaisa": ["kaisa"],
                  "kalista": ["kalista"],
                  "karma": ["karma"],
                  "karthus": ["karthus"],
                  "kassadin": ["kassadin", "kass"],
                  "katarina": ["katarina", "kat", "kata"],
                  "kayle": ["kayle"],
                  "kayn": ["kayn"],
                  "kennen": ["kennen"],
                  "khazix": ["k6", "khazix"],
                  "kindred": ["kindred", "kind"],
                  "kled": ["kled"],
                  "kogmaw": ["kogmaw", "kog", "maw"],
                  "ksante": ["ksante"],
                  "leblanc": ["leblanc"],
                  "leesin": ["leesin", "lee", "sin"],
                  "leona": ["leona"],
                  "lillia": ["lillia"],
                  "lissandra": ["liss", "lissandra"],
                  "lucian": ["lucian"],
                  "lulu": ["lulu"],
                  "lux": ["lux"],
                  "malphite": ["malphite", "malph"],
                  "malzahar": ["malzahar"],
                  "maokai": ["maokai"],
                  "masteryi": ["masteryi", "maestroyi", "yi"],
                  "missfortune": ["missfortune", "mf", "miss"],
                  "mordekaiser": ["mordekaiser", "morde"],
                  "morgana": ["morgana", "morg"],
                  "nami": ["nami"],
                  "nasus": ["nasus"],
                  "nautilus": ["nautilus", "nauti"],
                  "neeko": ["neeko"],
                  "nidalee": ["nidalee", "nida"],
                  "nilah": ["nilah"],
                  "nocturne": ["nocturne", "noct"],
                  "nunu": ["nunu", "nunuywillump"],
                  "olaf": ["olaf"],
                  "orianna": ["orianna"],
                  "ornn": ["ornn"],
                  "pantheon": ["pantheon", "pant", "panth"],
                  "poppy": ["poppy"],
                  "pyke": ["pyke", "paik"],
                  "qiyana": ["qiyana"],
                  "quinn": ["quinn"],
                  "rakan": ["rakan"],
                  "rammus": ["rammus"],
                  "reksai": ["reksai", "rek"],
                  "rell": ["rell"],
                  "renata": ["renata", "renataglasc"],
                  "renekton": ["renekton", "renek"],
                  "rengar": ["rengar"],
                  "riven": ["riven"],
                  "rumble": ["rumble"],
                  "ryze": ["ryze"],
                  "samira": ["samira"],
                  "sejuani": ["sejuani"],
                  "senna": ["senna"],
                  "seraphine": ["seraphine", "sera", "seraph"],
                  "sett": ["sett"],
                  "shaco": ["shaco"],
                  "shen": ["shen"],
                  "shyvana": ["shyvana", "shyvanna", "shyv"],
                  "singed": ["singed"],
                  "sion": ["sion"],
                  "sivir": ["sivir"],
                  "skarner": ["skarner"],
                  "sona": ["sona"],
                  "soraka": ["soraka", "raka"],
                  "swain": ["swain"],
                  "sylas": ["sylas"],
                  "syndra": ["syndra"],
                  "tahmkench": ["tahmkench", "tahm", "kench"],
                  "taliyah": ["taliyah"],
                  "talon": ["talon"],
                  "taric": ["taric"],
                  "teemo": ["teemo"],
                  "thresh": ["thresh"],
                  "tristana": ["tristana", "trist"],
                  "trundle": ["trundle"],
                  "tryndamere": ["tryndamere", "trynd"],
                  "twistedfate": ["twistedfate", "tf", "twisted"],
                  "twitch": ["twitch"],
                  "udyr": ["udyr"],
                  "urgot": ["urgot"],
                  "varus": ["varus"],
                  "vayne": ["vayne"],
                  "veigar": ["veigar", "veig", "vergas"],
                  "velkoz": ["velkoz", "vel"],
                  "vex": ["vex"],
                  "vi": ["vi"],
                  "viego": ["viego"],
                  "viktor": ["viktor"],
                  "vladimir": ["vladimir", "vlad", "vladi"],
                  "volibear": ["volibear", "voli"],
                  "warwick": ["warwick", "ww"],
                  "monkeyking": ["wukong"],
                  "xayah": ["xayah"],
                  "xerath": ["xerath"],
                  "xinzhao": ["xin", "xinzhao"],
                  "yasuo": ["yasuo"],
                  "yone": ["yone"],
                  "yorick": ["yorick"],
                  "yuumi": ["yuumi"],
                  "zac": ["zac"],
                  "zed": ["zed"],
                  "zeri": ["zeri"],
                  "ziggs": ["ziggs"],
                  "zilean": ["zilean"],
                  "zoe": ["zoe"],
                  "zyra": ["zyra"]}

            def filename(x):
                if language == "EN":
                    arampath = '/root/aery/data/aram/en/'
                    extension = '.txt'
                    file = arampath + x + extension

                elif language == "PT":
                    arampath = '/root/aery/data/aram/pt/'
                    extension = '.txt'
                    file = arampath + x + extension

                else:
                    arampath = '/root/aery/data/aram/sp/'
                    extension = '.txt'
                    file = arampath + x + extension

                return file

            counter = 0

            for key, value in champions.items():
                if charsearch in value:
                    path = filename(key)

                    counter += 1
                    with open(path, encoding="latin-1") as f:
                        text = f.read()
                        await ctx.send(text)

                    try:
                        guild_id = ctx.guild.id
                        guild_name = ctx.guild.name

                    except:
                        guild_id = 'DM'
                        guild_name = 'DM'

                    finally:
                        tz = pendulum.timezone('America/La_Paz')
                        event_date = datetime.now(tz)

                        db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command, Arguments) VALUES (?, ?, ?, ?, ?)",
                        event_date, guild_id, guild_name, 'aram', champ)
                        db.commit()

                        self.logs = self.bot.get_channel(991742125471432776)
                        await self.logs.send(f"aery aram {champ}, guild: {guild_name}")

            if counter == 0:
                if language == "EN":
                    await ctx.send("There's not information for that champ! Did you type the name correctly?")
                elif language == "PT":
                    await ctx.send("Não há informações para esse champ. Você soletrou o nome corretamente?")
                else:
                    await ctx.send("¡No existe información para este champ! ¿Escribiste bien el nombre?")


    @commands.hybrid_command(name = "normal",
    description = "Get champ information for Normal games.")
    async def normal(self, ctx: commands.Context, champ: str) -> None:

        try:
            language = db.record("SELECT GuildLang FROM languages WHERE GuildID = ?", ctx.guild.id)

            language = str(language[0])

        except:
            language = "SP"

        if champ == ():
            if language == 'EN':
                await ctx.send('¡You must type a champ name after `/normal`!')
            elif language == 'PT':
                await ctx.send('Você deve escrever o nome de um champ após `/normal`!')
            else:
                await ctx.send('¡Debes escribir el nombre de un champ después de `/normal`!')

        else:
            charsearch = champ.lower().replace("'", "").replace(".", "").replace(" ", "")

            champions = {"aatrox": ["aatrox"],
                  "ahri": ["ahri"],
                  "akali": ["akali"],
                  "akalimiddle": ["akalimid"],
                  "akalitop": ["akalitop"],
                  "akshan": ["akshan"],
                  "akshanmiddle": ["akshanmid"],
                  "akshanadc": ["akshanadc"],
                  "alistar": ["alistar"],
                  "amumu": ["amumu"],
                  "anivia": ["anivia"],
                  "annie": ["annie"],
                  "aphelios": ["aphelios"],
                  "ashe": ["ashe"],
                  "aurelionsol": ["aurelion", "sol", "aurelionsol"],
                  "azir": ["azir"],
                  "bard": ["bard", "bardo"],
                  "belveth": ["belveth", "bel"],
                  "blitzcrank": ["blitz", "blitzcrank"],
                  "brand": ["brand"],
                  "braum": ["braum"],
                  "caitlyn": ["cait", "caitlyn"],
                  "camille": ["camille"],
                  "cassiopeia": ["cassiopeia", "cassio", "cassi"],
                  "chogath": ["chogath", "cho"],
                  "corki": ["corki"],
                  "darius": ["darius"],
                  "diana": ["diana"],
                  "dianamiddle": ["dianamid"],
                  "dianajungle": ["dianajg"],
                  "drmundo": ["drmundo", "mundo"],
                  "drmundojungle": ["drmundojg", "mundojg"],
                  "drmundotop": ["mundotop", "drmundotop"],
                  "draven": ["draven"],
                  "ekko": ["ekko"],
                  "ekkojungle": ["ekkojg"],
                  "ekkomiddle": ["ekkomid"],
                  "elise": ["elise"],
                  "evelynn": ["evelynn", "eve"],
                  "ezreal": ["ez", "ezreal"],
                  "fiddlesticks": ["fiddlesticks", "fiddle"],
                  "fiora": ["fiora"],
                  "fizz": ["fizz"],
                  "galio": ["galio"],
                  "galiomiddle": ["galiomid"],
                  "gangplank": ["gangplank", "gang"],
                  "garen": ["garen"],
                  "gnar": ["gnar"],
                  "gragas": ["gragas"],
                  "gragasjungle": ["gragasjg"],
                  "gragastop": ["gragastop"],
                  "gragassupport": ["gragassupp"],
                  "graves": ["graves"],
                  "gwen": ["gwen"],
                  "hecarim": ["hecarim", "hec", "heca"],
                  "heimerdingermiddle": ["heimerdingermid", "heimmid", "heimermid"],
                  "heimerdingertop": ["heimerdingertop", "heimtop", "heimertop"],
                  "heimerdinger": ["heimerdinger", "heim", "heimer"],
                  "illaoi": ["illaoi"],
                  "irelia": ["irelia"],
                  "ireliatop": ["ireliatop"],
                  "ireliamiddle": ["ireliamid"],
                  "ivern": ["ivern"],
                  "janna": ["janna"],
                  "jarvaniv": ["jarvaniv", "jarvan"],
                  "jax": ["jax"],
                  "jayce": ["jayce"],
                  "jhin": ["jhin", "jihn", "jin"],
                  "jinx": ["jinx"],
                  "kaisa": ["kaisa"],
                  "kalista": ["kalista"],
                  "karma": ["karma"],
                  "karthus": ["karthus"],
                  "kassadin": ["kassadin", "kass"],
                  "katarina": ["katarina", "kat", "kata"],
                  "kayle": ["kayle"],
                  "kayn": ["kayn"],
                  "kennen": ["kennen"],
                  "khazix": ["k6", "khazix"],
                  "kindred": ["kindred", "kind"],
                  "kled": ["kled"],
                  "kogmaw": ["kogmaw", "kog", "maw"],
                  "ksante": ["ksante"],
                  "leblanc": ["leblanc"],
                  "leesin": ["leesin", "lee", "sin"],
                  "leesintop": ["leesintop", "leetop", "sintop"],
                  "leesinjungle": ["leesinjg", "leejg", "sinjg"],
                  "leona": ["leona"],
                  "lillia": ["lillia"],
                  "lissandra": ["liss", "lissandra"],
                  "lucian": ["lucian"],
                  "lucianadc": ["lucianadc"],
                  "lucianmiddle": ["lucianmiddle"],
                  "lulu": ["lulu"],
                  "lux": ["lux"],
                  "luxmiddle": ["luxmid"],
                  "luxsupport": ["luxsupp"],
                  "malphite": ["malphite", "malph"],
                  "malzahar": ["malzahar"],
                  "maokai": ["maokai"],
                  "maokaisupport": ["maokaisupp"],
                  "maokaitop": ["maokaitop"],
                  "masteryi": ["masteryi", "maestroyi", "yi"],
                  "missfortune": ["missfortune", "mf", "miss"],
                  "mordekaiser": ["mordekaiser", "morde"],
                  "morgana": ["morgana", "morg"],
                  "morganajungle": ["morganajg", "morgjg"],
                  "morganasupport": ["morganasupp", "morgsupp"],
                  "nami": ["nami"],
                  "nasus": ["nasus"],
                  "nautilus": ["nautilus", "nauti"],
                  "neeko": ["neeko"],
                  "neekomiddle": ["neekomid"],
                  "neekosupport": ["neekosupp"],
                  "nidalee": ["nidalee", "nida"],
                  "nilah": ["nilah"],
                  "nocturne": ["nocturne", "noct"],
                  "nunu": ["nunu", "nunuywillump"],
                  "olaf": ["olaf"],
                  "orianna": ["orianna"],
                  "ornn": ["ornn"],
                  "pantheon": ["pantheon", "pant", "panth"],
                  "pantheonmiddle": ["pantheonmid", "pantmid", "panthmid"],
                  "pantheonsupport": ["pantheonsupp", "pantsupp", "panthsupp"],
                  "poppy": ["poppy"],
                  "poppyjungle": ["poppyjg"],
                  "poppytop": ["poppytop"],
                  "pyke": ["pyke", "paik"],
                  "qiyana": ["qiyana"],
                  "quinn": ["quinn"],
                  "rakan": ["rakan"],
                  "rammus": ["rammus"],
                  "reksai": ["reksai", "rek"],
                  "rell": ["rell"],
                  "renata": ["renata", "renataglasc"],
                  "renekton": ["renekton", "renek"],
                  "rengar": ["rengar"],
                  "rengarjungle": ["rengarjg"],
                  "rengartop": ["rengartop"],
                  "riven": ["riven"],
                  "rumble": ["rumble"],
                  "rumblejungle": ["rumblejg"],
                  "rumblemiddle": ["rumblemid"],
                  "rumbletop": ["rumbletop"],
                  "ryze": ["ryze"],
                  "ryzemiddle": ["ryzemid"],
                  "ryzetop": ["ryzetop"],
                  "samira": ["samira"],
                  "sejuani": ["sejuani"],
                  "senna": ["senna"],
                  "seraphine": ["seraphine", "sera", "seraph"],
                  "sett": ["sett"],
                  "setttop": ["setttop"],
                  "settsupport": ["settsupp"],
                  "shaco": ["shaco"],
                  "shacojungle": ["shacojg"],
                  "shacosupport": ["shacosupport"],
                  "shen": ["shen"],
                  "shyvana": ["shyvana", "shyvanna"],
                  "singed": ["singed"],
                  "sion": ["sion"],
                  "sivir": ["sivir"],
                  "skarner": ["skarner"],
                  "sona": ["sona"],
                  "soraka": ["soraka", "raka"],
                  "swain": ["swain"],
                  "swainadc": ["swainadc"],
                  "swainsupport": ["swainsupp"],
                  "sylas": ["sylas"],
                  "sylasmiddle": ["sylasmid"],
                  "sylastop": ["sylastop"],
                  "syndra": ["syndra"],
                  "tahmkench": ["tahmkench", "tahm", "kench"],
                  "tahmkenchadc": ["tahmkenchadc", "tahmadc", "kenchadc"],
                  "tahmkenchtop": ["tahmkenchtop", "tahmtop", "kenchtop"],
                  "tahmkenchsupport": ["tahmkenchsupp", "tahmsupp", "kenchsupp"],
                  "taliyah": ["taliyah"],
                  "talon": ["talon"],
                  "taric": ["taric"],
                  "teemo": ["teemo"],
                  "thresh": ["thresh"],
                  "tristana": ["tristana", "trist"],
                  "trundle": ["trundle"],
                  "trundlejungle": ["trundlejg"],
                  "trundletop": ["trundletop"],
                  "tryndamere": ["tryndamere", "trynd"],
                  "twistedfate": ["twistedfate", "tf"],
                  "twitch": ["twitch"],
                  "udyr": ["udyr"],
                  "urgot": ["urgot"],
                  "varus": ["varus"],
                  "vayne": ["vayne"],
                  "veigar": ["veigar", "veig", "vergas"],
                  "velkoz": ["velkoz", "vel"],
                  "velkozmiddle": ["velkozmid", "velmid"],
                  "velkozsupport": ["velkozsupp", "velsupp"],
                  "vex": ["vex"],
                  "vi": ["vi"],
                  "viego": ["viego"],
                  "viegojungle": ["viegojg"],
                  "viegomiddle": ["viegomid"],
                  "viktor": ["viktor"],
                  "vladimir": ["vladimir", "vlad"],
                  "vladimirmiddle": ["vladimirmid", "vladmid"],
                  "vladimirtop": ["vladimirtop", "vladtop"],
                  "volibear": ["volibear", "voli"],
                  "volibearjungle": ["volibearjg", "volijg"],
                  "volibeartop": ["volibeartop", "volitop"],
                  "warwick": ["warwick", "ww"],
                  "warwickjungle": ["warwickjg", "wwjg"],
                  "warwicktop": ["warwicktop", "wwtop"],
                  "monkeyking": ["wukong"],
                  "xayah": ["xayah"],
                  "xerath": ["xerath"],
                  "xerathsupport": ["xerathsupp"],
                  "xerathmiddle": ["xerathmid"],
                  "xinzhao": ["xin", "xinzhao"],
                  "yasuo": ["yasuo"],
                  "yone": ["yone"],
                  "yorick": ["yorick"],
                  "yuumi": ["yuumi"],
                  "zac": ["zac"],
                  "zed": ["zed"],
                  "zeri": ["zeri"],
                  "ziggs": ["ziggs"],
                  "ziggsmiddle": ["ziggsmid"],
                  "ziggsadc": ["ziggsadc"],
                  "zilean": ["zilean"],
                  "zoe": ["zoe"],
                  "zyra": ["zyra"]}

            def filename(x):
                if language == "EN":
                    path = '/root/aery/data/normal/en/'
                    extension = '.txt'
                    file = path + x + extension

                elif language == "PT":
                    path = '/root/aery/data/normal/pt/'
                    extension = '.txt'
                    file = path + x + extension

                else:
                    path = '/root/aery/data/normal/sp/'
                    extension = '.txt'
                    file = path + x + extension

                return file

            counter = 0

            for key, value in champions.items():
                if charsearch in value:
                    path = filename(key)

                    counter += 1
                    with open(path, encoding="latin-1") as f:
                        text = f.read()
                        await ctx.send(text)

                    try:
                        guild_id = ctx.guild.id
                        guild_name = ctx.guild.name

                    except:
                        guild_id = 'DM'
                        guild_name = 'DM'

                    finally:
                        tz = pendulum.timezone('America/La_Paz')
                        event_date = datetime.now(tz)

                        db.execute("INSERT INTO logs (EventDate, GuildID, GuildName, Command, Arguments) VALUES (?, ?, ?, ?, ?)",
                        event_date, guild_id, guild_name, 'normal', champ)
                        db.commit()

                        self.logs = self.bot.get_channel(991742125471432776)
                        await self.logs.send(f"aery normal {champ}, guild: {guild_name}")

            if counter == 0:
                if language == "EN":
                    await ctx.send("There's not information for that champ! Did you type the name correctly?")
                elif language == "PT":
                    await ctx.send("Não há informações para esse champ. Você soletrou o nome corretamente?")
                else:
                    await ctx.send("¡No existe información para este champ! ¿Escribiste bien el nombre?")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(builds(bot))
