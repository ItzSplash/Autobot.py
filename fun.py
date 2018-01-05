import discord, asyncio
from discord.ext import commands
import random

randomcolors = ['a' , 'b' , "c" , "d" , "e" , "f" , "g" , "1" , "2", "3" , "4" , "5" , "6" , '7' , '8' , '9' , '0']
Rem_photos = ['http://i.imgur.com/bl9iQsu.jpg' , 'http://i.imgur.com/Nsc5SlA.jpg' , 
    'http://i.imgur.com/APSU7Bw.jpg' , 'http://i.imgur.com/7wK9PZh.jpg' , 'http://i.imgur.com/EnPQosj.png' ,
    'http://i.imgur.com/0gr4nkC.jpg' , 'http://i.imgur.com/COqbGN9.jpg' , 'http://i.imgur.com/ASP7BI1.jpg' , 
    'http://i.imgur.com/dXF1RRG.jpg' , 'http://i.imgur.com/4fOgBsr.jpg' , 'http://i.imgur.com/burcdcN.jpg' ,
    'http://i.imgur.com/TCCnd8b.jpg' , 'http://i.imgur.com/e6gHCPF.jpg' , 'http://i.imgur.com/bpzTsE2.jpg' ,
    'http://i.imgur.com/DQJPS8x.jpg' , 'http://i.imgur.com/f7w4RDE.jpg' , 'http://i.imgur.com/yGMqPom.png' ,
    'http://i.imgur.com/IIG4tpO.jpg' , 'http://i.imgur.com/JQ9U6ix.jpg' , 'http://i.imgur.com/xQU78GY.jpg' ,
    'http://i.imgur.com/jvmBTXB.jpg' , 'http://i.imgur.com/SUyaU9L.jpg' , 'http://i.imgur.com/gr695hc.jpg' ,
    'http://i.imgur.com/BVno6l6.png' , 'http://i.imgur.com/Ffn0dyK.jpg' , 'http://i.imgur.com/Gznz3n0.jpg' 
    'http://i.imgur.com/WBawS2J.jpg', 'http://i.imgur.com/Mv7fcC9.jpg', 'http://i.imgur.com/kt9YnWG.jpg',
    'http://i.imgur.com/iOzFqgh.jpg', 'http://i.imgur.com/hNnO8OX.jpg', 'http://i.imgur.com/YBygo97.jpg',
    'http://i.imgur.com/9Iaakhw.jpg', 'http://i.imgur.com/QT1BC8W.jpg', 'http://i.imgur.com/1H7k5m8.jpg',
    'http://i.imgur.com/639OCxG.jpg', 'http://i.imgur.com/lz2IXrg.jpg', 'http://i.imgur.com/ZQ6tVyv.png',
    'http://i.imgur.com/WZjkDU8.jpg', 'http://i.imgur.com/4GIw1ne.jpg', 'http://i.imgur.com/IoeK3aM.jpg' ,
    'http://i.imgur.com/HDUeD1F.png', 'http://i.imgur.com/azszJ2B.png' ]
eight = [" It is certain", "It is decidedly so", "Without a doubt",
                        "Yes definitely", " You may rely on it", " As I see it yes",
                        " Most likely", " Outlook good", " Yes",
                        " Signs point to yes", " Reply hazy try again",
                        "Ask again later", " Better not tell you now",
                        "Cannot predict now", "Concentrate and ask again",
                        "Don't count on it", "My reply is no",
                        "My sources say no", "Outlook not so good",
                        "Very doubtful"]

dictttt = {"A":"𝓐", "B":"𝓑", "C":"𝓒", "D":"𝓓", "E":"𝓔", "F":'𝓕', 'G':'𝓖', 'H':'𝓗', 
'I':'𝓘', 'J':'𝓙','K':'𝓚', 'L':'𝓛', 'M':'𝓜', 'N':'𝓝', 'O':'𝓞', 'P':'𝓟', 'Q':'𝓠', 
'R':'𝓡', 'S':'𝓢', 'T':'𝓣', 'U':'𝓤','V':'𝓥', 'W':'𝓦', 'X':'𝓧', 'Y':'𝓨','Z':'𝒵',
'a':'𝓪', 'b':'𝓫', 'c':'𝓬', 'd':'𝓭','e':'𝓮', 'f':'𝓯', 'g':'𝓰', 'h':'𝓱', 'i':'𝓲', 
'j':'𝓳', 'k':'𝓴', 'l':'𝓵','m':'𝓶', 'n':'𝓷','o':'𝓸','p':'𝓹', 'q':'𝓺', 'r':'𝓻', 's':'𝓼',
't':'𝓽', 'u':'𝓾', 'v':'𝒱', 'w':'𝔀', 'x':'𝔁', 'y':'𝔂', 'z':'𝒵', " ":" ", "'":"'" , "\n":"\n", ".":".", "?": "?"}
class fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True , help = "?say (text) bot says what u typed")
    async def say(self , ctx):
        cont = ctx.message.content
        if len(cont.split(" "))== 1:
            await self.bot.say("must include text")
        else:
            await self.bot.say(ctx.message.content[5:])
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context = True, aliases = ["calc"])
    async def calculator(self, ctx):
        xtx = ctx.message.content.split(" ")
        mess = ctx.message.channel
        if len(xtx) == 1:
            await self.bot.send_message(mess , "must provide integers")
        elif len(xtx) == 2:
            await self.bot.send_message(mess, int(xtx[1]))
        else: 
            l = int(xtx[1])
            r = int(xtx[3])
            if xtx[2] == "+":
                await self.bot.send_message(mess , l + r)
            elif xtx[2] == "-":
                if right > left:
                    await self.bot.say("**cannot do negative numbers**")
                else: await self.bot.send_message(mess , l - r)
            elif xtx[2] == "*":
                await self.bot.send_message(mess , l * r)
            elif xtx[2] == "/":
                await self.bot.send_message(mess , l / r)
            elif xtx[2] == "%":
                await self.bot.send_message(mess , l % r)
            elif len(xtx) == 1:
                await self.bot.send_message(mess , "must provide integers")
            elif len(xtx) == 2:
                await self.bot.send_message(mess, int(xtx[1]))

    @commands.command(pass_context=True)
    async def suicide(self , ctx):
        await self.bot.send_file(ctx.message.channel , "suicide.png")     

    @commands.command(pass_context=True , help = "types lenny and deletes your message" , hidden = True)
    async def lenny(self , ctx):
        await self.bot.say("( ͡° ͜ʖ ͡°)")
        await self.bot.delete_message(ctx.message)
    @commands.command(pass_context=True , help = "trump makes it illegal")
    async def illegal(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("you must include an argument such as `?illegal <text>`")
        else:
            await self.bot.say("https://storage.googleapis.com/is-now-illegal.appspot.com/gifs/" + ctx.message.content[9:].upper().replace(" ", "%20") + ".gif")


    @commands.command(pass_context=True, help= 'picks a random number between 1 and a given number')
    async def roll(self , ctx):
        var = ctx.message.content.split(" ")
        xtx = ctx.message.author.name
        if len(var)==1:
            await self.bot.say("**{0}**, you rolled a **{1}**!".format(xtx , str(random.randint(1,100))))
        elif len(var)>=2:
            if var[1].isdigit()==False:
                return await self.bot.say('**only positive integers may be used**')
            await self.bot.say("**{0}**, you rolled a **{1}**!".format(xtx , str(random.randint(1,int(var[1])))))

    @commands.command(pass_context =True,help ="shows your MAL list, type ?mal (mal username)")
    async def mal(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("must include a MyAnimeList username")
        else:
            await self.bot.say("https://myanimelist.net/animelist/" + ctx.message.content[5:])


    @commands.command(pass_context = True ,hidden=True , help = "rock paper scissors")
    async def rps(self , ctx):
        scissors = 3
        paper = 5
        rock = 7
        whoops =  [scissors , paper , rock]
        rps = random.choice(whoops)
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("you have to type it like `?rps (r/p/s)`")
        else:
            xtx = ctx.message.content.split(" ")[1].lower()
            if xtx == "rock" or xtx ==  "r":
                if int(rps + rock) == 14:
                    await self.bot.say("**Rock!**, It's a Tie")
                if int(rps + rock) == 12:
                    await self.bot.say("**Paper!**, I won!")
                if int(rps + rock) == 10:
                    await self.bot.say("**Scissors!**, You beat me!")
            if xtx == "paper" or xtx == "p":
                if int(rps + paper) == 10:
                    await self.bot.say("**Paper!**, It's a Tie!")
                if int(rps + paper) == 12:
                    await self.bot.say("**Scissors!**, I won!")
                if int(rps + paper) == 8:
                    await self.bot.say("**Rock!**, You beat me!")
            if xtx == "scissors" or xtx == "s":
                if int(rps + scissors) == 6:
                    await self.bot.say("**Scissors!**, It's a Tie!")
                if int(rps + scissors) == 10:
                    await self.bot.say("**Rock!**, I won!")
                if int(rps + scissors) == 8:
                    await self.bot.say("**Paper!**, You beat me!")

    @commands.command(pass_context = True, hidden = True)
    async def embed(self , ctx):
        xtx = ctx.message
        em = discord.Embed(title= None, description=xtx.content[7:], colour=0xDEADBF)
        em.set_author(name=xtx.author.name, icon_url=xtx.author.avatar_url)
        await self.bot.send_message(xtx.channel, embed=em)
        await self.bot.delete_message(xtx)
        
    @commands.command(pass_context=True)
    async def randomcolor(self , ctx):
        randcolor = random.randint(0, 16777215)
        emb = discord.Embed(title= None, description=str(randcolor), colour=randcolor)
        msg = await self.bot.send_message(ctx.message.channel ,  embed = emb)
        await self.bot.add_reaction(msg , "\U000023ed")
        @self.bot.event
        async def on_reaction_add(reaction , user):
            if reaction.emoji == "⏭":
                randcolor = random.randint(0, 16777215)
                em = discord.Embed(title= None, description=str(randcolor), colour=randcolor)
                await self.bot.edit_message(msg, new_content=None, embed=em)
                await self.bot.remove_reaction(msg, "\U000023ed", ctx.message.author)

    @commands.command(pass_context=True)
    async def fancy(self, ctx):
        if len(ctx.message.content.split(" "))== 1:
            await self.bot.send_message(ctx.message.channel, "must include args, such as `?fancy <text>`")
        else:
            list1 = ctx.message.content[7:]
            other_list = []
            for i in list1:
                other_list.append(dictttt[i])
            await self.bot.say(''.join(other_list))
            await self.bot.delete_message(ctx.message)


    @commands.command(pass_context = True, hidden = True)
    async def big(self , ctx):
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("must include text")
        else: 
            list1 = ctx.message.content[5:].lower().replace(" ","")
            other_list = []
            for i in list1:
                other_list.append(":regional_indicator_" + i + ":")
            await self.bot.say(''.join(other_list))
            await self.bot.delete_message(ctx.message)

    
    @commands.command(pass_context = True)
    async def rule34(self, ctx):
        if "nsfw" in ctx.message.channel.name:
            await self.bot.say("kek, there is no nsfw command yet")
        else: 
            v = await self.bot.say("channel name must contain \"nsfw\" in it")
            await asyncio.sleep(3)
            await self.bot.delete_message(v)


    @commands.command(pass_context=True, aliases = ["8ball"])
    async def eii(self , ctx):
        await self.bot.say("**{0}**, your prediction :8ball:, **{1}**".format(ctx.message.author.name,random.choice(eight)))

    @commands.command(pass_context=True, help= 'shows a random pick of Rem from Re:zero')
    async def rem(self):
        await self.bot.say(random.choice(Rem_photos))
    @commands.command(pass_context=True, help= 'rolls a dice')
    async def rolldice(self , ctx):
        await self.bot.say("**{0}** , your roll is **{1}**".format(ctx.message.author.name, random.randint(1,6)))
def setup(bot):
    bot.add_cog(fun(bot))
