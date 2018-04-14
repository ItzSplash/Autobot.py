import discord, asyncio
from discord.ext import commands
import random
import json
from rls.rocket import RocketLeague
import requests
import math
from pypubg import core

google_jky= "key"
ranks = {'0': "Unranked", '1': "Bronze I", '2': "Bronze II", '3': "Bronze III", '4': "Silver I", '5': "Silver II",
         '6': "Silver III", '7': "Gold I", '8': "Gold II", '9': "Gold III", '10': "Diamond I", '11': "Diamond II",
         '12': 'Diamond III', '13': 'Platinum I', '14': 'Platinum II', '15': 'Platinum III', '16': 'Champion I',
         '17': 'Champion II', '18': 'Champion III', '19': 'Grand Champion'}
class api():
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(pass_context = True)
    async def rlrank(self , ctx):
        rocket = RocketLeague(api_key='Key')
        ch = ctx.message.channel
        xtx = ctx.message.content.split(" ")
        if len(xtx) == 1: 
            await self.bot.send_message(ch , "must include a platform and username `?rlrank xbox Itz Splashh")
        if len(xtx)== 2:
            await self.bot.send_message(ch, "must include platform and username")
        else:
            if xtx[1].lower() == "pc":
                key = "key"
                r = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + key + "&vanityurl=" + xtx[2])
                reqq = json.loads(r.text)
                platform = 1
                ids = reqq["response"]["steamid"]
            if xtx[1].lower() == "xbox":
                platform = 3
                ids = '%20'.join(xtx[2:])
            if xtx[1].lower() == "ps4":
                platform = 1
                ids = xtx[2:]
            await self.bot.send_typing(ch)
            try:
                stats = rocket.players.player(id=ids, platform=platform)
            except:
                return await self.bot.send_message(ch, "*could not find user!*")

            emb = discord.Embed(colour=ctx.message.author.colour, title= "{}'s stats".format(ids))
            emb.set_thumbnail(url=stats.json()['avatar'])

            solorank = ranks[str(stats.json()["rankedSeasons"]["7"]["10"]["tier"])]
            solo_division = stats.json()["rankedSeasons"]["7"]["10"]["division"]
            solo_points = stats.json()["rankedSeasons"]["7"]["10"]["rankPoints"]
            singles = "{0} tier {1} ({2})".format(solorank, solo_division + 1,solo_points)

            doublerank = ranks[str(stats.json()["rankedSeasons"]["7"]["11"]["tier"])]
            double_division = stats.json()["rankedSeasons"]["7"]["11"]["division"]
            double_points = stats.json()["rankedSeasons"]["7"]["11"]["rankPoints"]
            doubles = "{0} tier {1} ({2})".format(doublerank, double_division + 1, double_points)

            threes = ranks[str(stats.json()["rankedSeasons"]["7"]["12"]["tier"])]
            threes_division = stats.json()["rankedSeasons"]["7"]["12"]["division"]
            threes_points = stats.json()["rankedSeasons"]["7"]["12"]["rankPoints"]
            solostandard = "{0} tier {1} ({2})".format(threes, threes_division + 1, threes_points)

            standardrank = ranks[str(stats.json()["rankedSeasons"]["7"]["13"]["tier"])]
            standard_division = stats.json()["rankedSeasons"]["7"]["13"]["division"]
            standard_points = stats.json()["rankedSeasons"]["7"]["13"]["rankPoints"]
            standard = "{0} tier {1} ({2})".format(standardrank, standard_division + 1, standard_points)

            the_string = "1s- {}\n2s- {}\nsolo 3s- {}\n3s- {}"
            emb.add_field(name="Ranks:",value= the_string.format(singles, doubles, solostandard,standard))

            statss = "**{}** shots \n**{}** assists\n**{}** goals\n**{}** saves\n**{}** wins\n**{}** MVPs"
            shots = stats.json()["stats"]["shots"]
            assists = stats.json()["stats"]["assists"]
            goals = stats.json()["stats"]["goals"]
            saves = stats.json()["stats"]["saves"]
            wins = stats.json()["stats"]["wins"]
            mvp = stats.json()["stats"]["mvps"]
            emb.add_field(name="Stats:", value=statss.format(shots, assists, goals, saves, wins, mvp))
            try:
                await self.bot.send_message(ch, "", embed= emb)
            except:
                await self.bot.send_message(ch, "*could not find user!*")
    @commands.command(pass_context = True)
    async def osu(self, ctx):
        xtx = ctx.message.content.split(" ")
        ch = ctx.message.channel
        if len(xtx) == 1:
            await self.bot.send_message(ch, "must include a username")
        else:
            key = "75e98d0850e3ccab3f44948406e36dde624fdd09"
            r = requests.get("https://osu.ppy.sh/api/get_user?k="key"&u={}".format(" ".join(ctx.message.content.split(" ")[1:])))
            reqq = json.loads(r.text)[0]
            emb = discord.Embed(description=None, colour=ctx.message.author.colour, title=reqq["username"])
            emb.add_field(name= "Total Score", value= str(reqq['total_score']))
            emb.set_thumbnail(url="https://a.ppy.sh/{}".format(reqq["user_id"]))
            emb.add_field(name="Level", value=math.floor(float(reqq['level'])))
            emb.add_field(name="Accuracy", value="{}%".format(round(float(reqq['accuracy']), 2)))
            emb.set_footer(text= "User id - {}".format(reqq["user_id"]))
            emb.add_field(name= "Play count", value=reqq["playcount"])
            emb.add_field(name= "Rank", value="Global- {0}\n{3} :flag_{1}:- {2}".format(reqq['pp_rank'], reqq['country'].lower(), reqq["pp_country_rank"], reqq["country"]))
            emb.add_field(name="PP", value="{}".format(round(float(reqq["pp_raw"]), 2)))
            await self.bot.send_message(ch, "", embed=emb)
    @commands.command(pass_context = True)
    async def pubgstats(self , ctx):
        key = "key"
        r = requests.get("https://api.pubgtracker.com/v2/profile/pc/VissGames?region=na&season=2018-01", headers={"TRN-Api-Key": key})
        reqq = json.loads(r.text)
        if reqq["error"]:
            await self.bot.say(reqq["error"])
        else:
            await self.bot.say(reqq)
    @commands.command(pass_context =  True)
    async def fortnite(self, ctx):
        ch = ctx.message.channel
        key = "key"
        xtx = ctx.message.content.split(" ")
        platform = None
        gamertag = None
        color = None
        if len(xtx) == 1:
            return await self.bot.send_message(ch, "must include platform then gamertag")
        elif len(xtx) == 2:
            return await self.bot.send_message(ch, "must include platform then gamertag")
        else:
            if xtx[1].lower() == "xbox":
                platform = "xbl"
                gamertag = "%20".join(xtx[2:])
                color = 0x107c10
            elif xtx[1].lower() == "pc":
                platform = "pc"
                gamertag = xtx[2]
                color = 0x003791
                color = 0x696969
            elif xtx[1].lower() == "ps4":
                platform = "psn"
                gamertag = xtx[2]
                color = 0x003791
            r = requests.get("https://api.fortnitetracker.com/v1/profile/{0}/{1}".format(platform, gamertag), headers={"TRN-Api-Key": key})
            fortnite = json.loads(r.text)
            try:
                emb = discord.Embed(color= color, title= "{}'s Fortnite stats".format(fortnite["epicUserHandle"]))
            except KeyError:
                return await self.bot.send_message(ch, "*Cannot find user!*")
            try:
                solo = fortnite["stats"]["p2"]["top1"]["value"]
                duo = fortnite["stats"]["p10"]["top1"]["value"]
                squad = fortnite["stats"]["p9"]["top1"]["value"]
                total = fortnite["lifeTimeStats"][8]["value"]
                emb.add_field(name="Wins:", value= "Solos - {}\nDuos - {}\nSquads - {}\nTotal - {}".format(solo, duo, squad, total))
            except Exception as e:
                return await self.bot.send_message(ch, "*you havent played all gamemodes*")
            
            winperc = fortnite["lifeTimeStats"][9]["value"]
            kdratio = fortnite["lifeTimeStats"][11]["value"]
            kills =fortnite["lifeTimeStats"][10]["value"]
            matches = fortnite["lifeTimeStats"][7]["value"]
            emb.add_field(name= "Stats", value= "{} Win%\n{} Kills\n{} K/D ratio\n{} matches played".format(winperc, kills, kdratio,matches))
            return await self.bot.send_message(ch, "", embed= emb)
'''
    @commands.command(pass_context = True)
    async def image(self,ctx):
        client_id= "client_id token"
        client_secret= "client_token token"
        r = requests.get("	https://api.imgur.com/3/image/{id}")
        reqq = json.loads(r.text)
        print(reqq)
'''

    
    
def setup(bot):
    bot.add_cog(api(bot))
