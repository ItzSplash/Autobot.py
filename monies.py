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
        file = "/home/splash/levels.json"
        with open(file, 'r') as f:
            datastore = json.load(f)
            qwerty = datastore["user"][ctx.message.author.id]["bank"]
            if qwerty > int(var[1]):
                if len(var)==2:
                    comp = random.randint(1,100)
                    if comp == 100:
                        variable1 = int(var[1]) * 3
                        em = discord.Embed(description="you rolled a **{0}**, you win! You recieve **{1}** credits!".format(comp , variable1), colour=ctx.message.author.colour)
                        await self.bot.send_message(ctx.message.channel, embed=em)
                        open_file_object = open("/home/splash/levels.json", 'r')
                        decoded_json = json.load(open_file_object)
                        output_file = "/home/splash/levels.json"
                        decoded_json["user"][ctx.message.author.id]["bank"] += int(variable1)
                        with open(output_file, 'w') as write_file_object:
                            write_file_object.write(json.dumps(decoded_json))
                    elif comp > 89:
                        variable1 = (int(var[1]) * 2)
                        em = discord.Embed(description="you rolled a **{0}**, you win! You recieve **{1}** credits!".format(comp , variable1), colour=ctx.message.author.colour)
                        await self.bot.send_message(ctx.message.channel, embed=em)
                        open_file_object = open("/home/splash/levels.json", 'r')
                        decoded_json = json.load(open_file_object)
                        output_file = "/home/splash/levels.json"
                        decoded_json["user"][ctx.message.author.id]["bank"] += int(variable1)
                        with open(output_file, 'w') as write_file_object:
                            write_file_object.write(json.dumps(decoded_json))
                    elif comp > 74:
                        variable1 = (int(var[1]) * 1.5)
                        em = discord.Embed(description="you rolled a **{0}**, you win! You recieve **{1}** credits!".format(comp , variable1), colour=ctx.message.author.colour)
                        await self.bot.send_message(ctx.message.channel, embed=em)
                        open_file_object = open("/home/splash/levels.json", 'r')
                        decoded_json = json.load(open_file_object)
                        output_file = "/home/splash/levels.json"
                        decoded_json["user"][ctx.message.author.id]["bank"] += int(variable1)
                        with open(output_file, 'w') as write_file_object:
                            write_file_object.write(json.dumps(decoded_json))
                    elif comp > 49:
                        em = discord.Embed(description="you rolled a **{0}**, you win! You recieve **{1}** credits!".format(comp , var[1]), colour=ctx.message.author.colour)
                        await self.bot.send_message(ctx.message.channel, embed=em)
                        open_file_object = open("/home/splash/levels.json", 'r')
                        decoded_json = json.load(open_file_object)
                        output_file = "/home/splash/levels.json"
                        decoded_json["user"][ctx.message.author.id]["bank"] += int(var[1])
                        with open(output_file, 'w') as write_file_object:
                            write_file_object.write(json.dumps(decoded_json))
                    else:
                        em = discord.Embed(description="you rolled a **{0}**, you lose. You lost **{1}** credits.".format(comp , var[1]), colour=ctx.message.author.colour)
                        await self.bot.send_message(ctx.message.channel, embed=em)
                        open_file_object = open("/home/splash/levels.json", 'r')
                        decoded_json = json.load(open_file_object)
                        output_file = "/home/splash/levels.json"
                        decoded_json["user"][ctx.message.author.id]["bank"] -= int(var[1])
                        with open(output_file, 'w') as write_file_object:
                            write_file_object.write(json.dumps(decoded_json))
                elif len(var)== 1:
                    await self.bot.say("u need an amount to bet `?spin (amount)`")
            else: 
                return
            
    @commands.command(pass_context = True)
    async def flip(self , ctx):
        headtail = ["t" , "h"]
        computer = random.choice(headtail)
        var = ctx.message.content.split(" ")
        if len(var) == 3:
            file = "/home/splash/levels.json"
            with open(file, 'r') as f:
                datastore = json.load(f)
                qwerty = datastore["user"][ctx.message.author.id]["bank"]
                if qwerty > int(var[2]):
                    if var[1].lower() == "t":
                        if computer == var[1].lower():
                            await self.bot.say("tails, you win")
                            open_file_object = open("/home/splash/levels.json", 'r')
                            decoded_json = json.load(open_file_object)
                            output_file = "/home/splash/levels.json"
                            decoded_json["user"][ctx.message.author.id]["bank"] += int(var[2])
                            with open(output_file, 'w') as write_file_object:
                                write_file_object.write(json.dumps(decoded_json))

                        else: 
                            await self.bot.say("heads, you lost")

                            open_file_object = open("/home/splash/levels.json", 'r')
                            decoded_json = json.load(open_file_object)
                            output_file = "/home/splash/levels.json"
                            decoded_json["user"][ctx.message.author.id]["bank"] -= int(var[2])
                            with open(output_file, 'w') as write_file_object:
                                write_file_object.write(json.dumps(decoded_json))

                    if var[1].lower() == "h":
                        if computer == var[1].lower():
                            await self.bot.say("heads, you win")

                            open_file_object = open("/home/splash/levels.json", 'r')
                            decoded_json = json.load(open_file_object)
                            output_file = "/home/splash/levels.json"
                            decoded_json["user"][ctx.message.author.id]["bank"] += int(var[2])
                            with open(output_file, 'w') as write_file_object:
                                write_file_object.write(json.dumps(decoded_json))

                        else: 
                            await self.bot.say("tails, you lost")

                            open_file_object = open("/home/splash/levels.json", 'r')
                            decoded_json = json.load(open_file_object)
                            output_file = "/home/splash/levels.json"
                            decoded_json["user"][ctx.message.author.id]["bank"] -= int(var[2])
                            with open(output_file, 'w') as write_file_object:
                                write_file_object.write(json.dumps(decoded_json))
        if len(var) == 2:
            await self.bot.say("must include an amount to bet")
        if len(var) == 1:
            await self.bot.say("?flip (h / t) (amount to bet)")
        if var[2] == "tails" or var[2] == "heads":
            await self.bot.say("user must use `h / t` for it to work")



def setup(bot):
    bot.add_cog(monies(bot))
