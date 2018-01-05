import discord, asyncio
from discord.ext import commands
import json

class monies():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self , message):
        try:
            if message.author.bot:
                return
            else:
                open_file_object = open("/home/splash/levels.json", 'r')
                decoded_json = json.load(open_file_object)
                output_file = "/home/splash/levels.json"
                decoded_json["user"][message.author.id]["bank"] +=1
                with open(output_file, 'w') as write_file_object:
                    write_file_object.write(json.dumps(decoded_json))
        except KeyError:
            if message.author.bot:
                return
            else: 
                open_file_object = open("/home/splash/levels.json", 'r')
                decoded_json = json.load(open_file_object)
                output_file = "/home/splash/levels.json"
                decoded_json["user"][message.author.id] = {"bank":1}
                with open(output_file, 'w') as write_file_object:
                    write_file_object.write(json.dumps(decoded_json))


    @commands.command(pass_context =True)
    async def credits(self , ctx):
        xtx = ctx.message.content.split(" ")
        if len(xtx) == 1:
            file = "/home/splash/levels.json"
            with open(file, 'r') as f:
                datastore = json.load(f)
                await self.bot.say("{0}, You have **{1}** credits".format(ctx.message.author.display_name, datastore["user"][ctx.message.author.id]["bank"]))
        else: 
            file = "/home/splash/levels.json"
            with open(file, 'r') as f:
                datastore = json.load(f)
                id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
                member = ctx.message.server.get_member(id)
                await self.bot.say("{0}'s has **{1}** credits".format(member.display_name , datastore["user"][member.id]["bank"]))
    
    @commands.command(pass_context =True)
    async def ccgive(self , ctx):
        if ctx.message.author.id == "197063788560777216":
            var = ctx.message.content.split(" ")
            id = var[2].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            open_file_object = open("/home/splash/levels.json", 'r')
            decoded_json = json.load(open_file_object)
            output_file = "/home/splash/levels.json"
            decoded_json["user"][member.id]["bank"] += int(var[1])
            with open(output_file, 'w') as write_file_object:
                write_file_object.write(json.dumps(decoded_json))
                await self.bot.say("added {0} credits to {1}".format(var[1] , member.nick))
        else: return

    @commands.command(pass_context =True)
    async def ccremove(self , ctx):
        if ctx.message.author.id == "197063788560777216":
            var = ctx.message.content.split(" ")
            id = var[2].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            open_file_object = open("/home/splash/levels.json", 'r')
            decoded_json = json.load(open_file_object)
            output_file = "/home/splash/levels.json"
            decoded_json["user"][member.id]["bank"] -= int(var[1])
            with open(output_file, 'w') as write_file_object:
                write_file_object.write(json.dumps(decoded_json))
                await self.bot.say("removed {0} credits from {1}".format(var[1] , member.nick))
        else: return

    @commands.command(pass_context=True)
    async def spin(self , ctx):
        var = ctx.message.content.split(" ")
        file = "/home/splash/levels2.json"
        b = "bank"
        u = "user"
        ids = ctx.message.author.id
        colr = ctx.message.author.colour
        with open(file, 'r') as f:
            datastore = json.load(f)
            qwerty = datastore[u][ids][b]
            if qwerty >= int(var[1]):
                if len(var)==2:
                    comp = random.randint(1,100)
                    rolld = "you rolled a **{0}**, you win! You recieve **{1}** credits!"
                    ch = ctx.message.channel
                    
                    if comp == 100:
                        var1 = int(var[1]) * 3
                        em = discord.Embed(description=rolld.format(comp , var1), colour=colr)
                        await self.bot.send_message(ch, embed=em)
                        open1 = open(file, 'r')
                        jsoon = json.load(open1)
                        jsoon[u][ids][b] += int(var1)
                        with open(file, 'w') as write1:
                            write1.write(json.dumps(jsoon))
                    elif comp > 89:
                        var1 = (int(var[1]) * 2)
                        em = discord.Embed(description=rolld.format(comp , var1), colour=colr)
                        await self.bot.send_message(ch, embed=em)
                        open1 = open(file, 'r')
                        jsoon = json.load(open1)
                        jsoon[u][ids][b] += int(var1)
                        with open(file, 'w') as write1:
                            write1.write(json.dumps(jsoon))
                    elif comp > 74:
                        var1 = (int(var[1]) * 1.5)
                        em = discord.Embed(description=rolld.format(comp , var1), colour=colr)
                        await self.bot.send_message(ch, embed=em)
                        open1 = open(file, 'r')
                        jsoon = json.load(open1)
                        jsoon[u][ids][b] += int(var1)
                        with open(file, 'w') as write1:
                            write1.write(json.dumps(jsoon))
                    elif comp > 49:
                        var1 = int(var[1])
                        em = discord.Embed(description=rolld.format(comp , var1), colour=colr)
                        await self.bot.send_message(ch, embed=em)
                        open1 = open(file, 'r')
                        jsoon = json.load(open1)
                        jsoon[u][ids][b] += int(var[1])
                        with open(file, 'w') as write1:
                            write1.write(json.dumps(jsoon))
                    else:
                        var1 = int(var[1])
                        em = discord.Embed(description=rolld.format(comp , var1), colour=colr)
                        await self.bot.send_message(ch, embed=em)
                        open1 = open(file, 'r')
                        jsoon = json.load(open1)
                        jsoon[u][ids][b] -= int(var[1])
                        with open(file, 'w') as write1:
                            write1.write(json.dumps(jsoon))
                elif len(var)== 1:
                    await self.bot.say("you need an amount to bet `=spin (amount)`")
            else: 
                await self.bot.send_message(ch , "*You dont have enough credits!*")
            
    @commands.command(pass_context = True)
    async def flip(self , ctx):
        headtail = ["t" , "h"]
        computer = random.choice(headtail)
        var = ctx.message.content.split(" ")
        ids = ctx.message.author.id
        u = "user"
        b = "bank"
        if len(var) == 3:
            file = "/home/splash/levels2.json"
            with open(file, 'r') as f:
                datastore = json.load(f)
                qwerty = datastore[u][ids][b]
                if qwerty >= int(var[2]):
                    if var[1].lower() == "t":
                        if computer == var[1].lower():
                            await self.bot.say("Tails, you win!")
                            open1 = open(file, 'r')
                            decoded_json = json.load(open1)
                            decoded_json[u][ids][b] += int(var[2])
                            with open(file, 'w') as write1:
                                write1.write(json.dumps(decoded_json))

                        else: 
                            await self.bot.say("Heads, you lost!")
                            open1 = open(file, 'r')
                            decoded_json = json.load(open1)
                            decoded_json[u][ids][b] -= int(var[2])
                            with open(file, 'w') as write1:
                                write1.write(json.dumps(decoded_json))

                    if var[1].lower() == "h":
                        if computer == var[1].lower():
                            await self.bot.say("Heads, you win!")

                            open1 = open(file, 'r')
                            decoded_json = json.load(open1)
                            decoded_json[u][ids][b] += int(var[2])
                            with open(file, 'w') as write1:
                                write1.write(json.dumps(decoded_json))

                        else: 
                            await self.bot.say("Tails, you lost!")

                            open1 = open(file, 'r')
                            decoded_json = json.load(open1)
                            decoded_json[u][ids][b] -= int(var[2])
                            with open(file, 'w') as write1:
                                write1.write(json.dumps(decoded_json))
        if len(var) == 2:
            await self.bot.say("must include an amount to bet")
        if len(var) == 1:
            await self.bot.say("=flip (h / t) (amount to bet)")
        if var[2] == "tails" or var[2] == "heads":
            await self.bot.say("user must use `h / t` for it to work")




def setup(bot):
    bot.add_cog(monies(bot))
