import discord, asyncio
import datetime
from discord.ext import commands
import psutil
import os
import json

class information():
    def __init__(self, bot):
        self.bot = bot
	

    @commands.command(pass_context=True , help = "?nickname (name), changes nickname, ?nickname to go back to normal")
    async def nickname(self , ctx):
        try:
            await self.bot.change_nickname(ctx.message.author , ctx.message.content[10:])
            if len(ctx.message.content.split(" ")) == 1:
                await self.bot.say("you reset your nickname")
            else:
                await self.bot.send_message(ctx.message.channel ,"You changed ur nickname to **" + ctx.message.content[10:] + "**")
        except discord.FORBIDDEN:
            await self.bot.say("permissions are too low...")

    @commands.command(pass_context = True , help = "shows your / someone elses avatar")
    async def avatar(self , ctx):
        xtx = ctx.message.content.split(" ")
        if len(xtx) == 1:
            await self.bot.say(ctx.message.author.avatar_url.replace("?size=1024" , ""))
        else:
            id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            await self.bot.say(member.avatar_url.replace("?size=1024" , ""))

    @commands.command(pass_context = True)
    async def userid(self , ctx):
        xtx = ctx.message.content.split(" ")
        if len(xtx) == 1:
            await self.bot.say(ctx.message.author.mention + ", your userID is **" + ctx.message.author.id + "**")
        else:
            id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
            member = ctx.message.server.get_member(id)
            await self.bot.say("The person's userID is **" + member.id + "**")


    @commands.command(pass_context=True, help="Shows information about a user")
    async def user(self, ctx):
        if ctx.message.server.me.permissions_in(ctx.message.channel).embed_links is False:
            return await self.bot.send_message(ctx.message.channel, "No perms to create an embed!")
        if len(ctx.message.content.split(" ")) == 1:
            user = ctx.message.author
            embed = discord.Embed(colour=user.colour, title=user.name + "#" + user.discriminator)
            if user.game is not None:
                embed.description = str(user.game)
            embed.add_field(name="Created Account on", value=user.created_at.strftime("%d %b %Y %H:%M:%S\n" + str((datetime.datetime.now() - user.created_at).days) + " days ago."))
            embed.add_field(name="Joined Server on", value=user.joined_at.strftime("%d %b %Y %H:%M:%S\n") + str((datetime.datetime.now() - user.joined_at).days) + " days ago.")
            embed.add_field(name="Top Roles", value =", ".join(r.name for r in ctx.message.author.roles[1:4]))
            try:
                embed.add_field(name="Playing", value = user.game)
            except:
                return
            embed.add_field(name="Status", value = user.status)
            embed.add_field(name="Nickname", value = user.display_name)
            if user.avatar_url == "":
                embed.set_thumbnail(url=user.default_avatar_url)
            else:
                embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text="User ID: " + user.id)
            await self.bot.send_message(ctx.message.channel, content=" ", embed=embed)
        else:
            try:
                id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
                user = ctx.message.server.get_member(id)
                if user is None:
                    embed = discord.Embed(colour=0xe74c3c).add_field(name=u"\u2049 User not found... ", value="command: ``" + ctx.message.clean_content + "``")
                    return await self.bot.send_message(ctx.message.channel, content=" ", embed=embed)
                embed = discord.Embed(colour=user.colour, title=user.name + "#" + user.discriminator)
                embed.add_field(name="Created account on", value=user.created_at.strftime("%d %b %Y %H:%M:%S\n" + str((datetime.datetime.now() - user.created_at).days) + " days ago."))
                embed.add_field(name="Joined server on", value=user.joined_at.strftime("%d %b %Y %H:%M:%S\n") + str((datetime.datetime.now() - user.joined_at).days) + " days ago.")
                embed.add_field(name="Top Role", value = user.top_role)
                embed.add_field(name="Status", value = user.status)
                embed.add_field(name="Nickname", value = user.display_name)
                try:
                    embed.add_field(name="Playing ", value = user.game)
                except:
                    return
                if user.avatar_url == "":
                    embed.set_thumbnail(url=user.default_avatar_url)
                else:
                    embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text="User ID: " + user.id)
                await self.bot.send_message(destination=ctx.message.channel, content=" ", embed=embed)
            except Exception as e:
                embed = discord.Embed(colour=0xe74c3c).add_field(name=u"\u2049 Something went wrong... ", value="`" + str(e) +"`" )
                await self.bot.send_message(destination=ctx.message.channel, content=" ", embed=embed)
    @commands.command(pass_context=True, help="Shows information on the bot")
    async def info(self, ctx):
        me = ctx.message.server.me
        embed = discord.Embed(colour=me.colour, title=self.bot.user.name + "#" + self.bot.user.discriminator, description="bot website: http://itzsplash.me")
        mike_icon = "https://cdn.discordapp.com/avatars/386586108776939520/7ab01f24369ee3f370ebd7cb0bc976be.webp"
        embed.set_author(name="Created by Itz Splash#0012", url="http://itzsplash.me/invite", icon_url=mike_icon)
        embed.add_field(name="Created at", value=me.created_at.strftime("%d %b %Y %H:%M:%S\n" + str((datetime.datetime.now() - me.created_at).days) + " days ago."))
        embed.add_field(name="Member since", value=me.joined_at.strftime("%d %b %Y %H:%M:%S\n") + str((datetime.datetime.now() - me.joined_at).days) + " days ago.")
        pid = os.getpid()
        py = psutil.Process(pid)
        mem_info = py.memory_full_info()
        uss = round(mem_info[0]/1048576, 1)
        embed.set_thumbnail(url ="https://cdn.discordapp.com/avatars/387406522499727360/d163cf6cb1a79760a07c5d75f1188051.webp")
        embed.add_field(name="{} Guilds".format(len(self.bot.servers)), value="{} Users".format(len(list(self.bot.get_all_members()))), inline=True)
        embed.add_field(name="Usage", value="{0}MB / {1}% CPU ".format(uss, psutil.cpu_percent()))
        embed.add_field(name="Library", value="discord.py, version "+ discord.__version__ + "\n python version 3.5.2")
        embed.add_field(name="Invite Link" , value = "http://itzsplash.me/invite")
        await self.bot.send_message(ctx.message.channel, " ", embed=embed)

    @commands.command(pass_context = True)
    async def server(self, ctx):
        serv = ctx.message.server
        me = serv.me
        embed = discord.Embed(colour= ctx.message.author.color)
        embed.set_author(name=serv.name, icon_url=serv.icon_url)
        embed.add_field(name = "Server Owner",value = serv.owner)
        embed.add_field(name= "Created at", value = serv.created_at.strftime("%d %b %Y %H:%M:%S\n" + str((datetime.datetime.now() - serv.created_at).days) + " days ago."))
        embed.add_field(name = "Server ID" , value = serv.id)
        embed.add_field(name = "Members" , value = "{0}".format(serv.member_count))
        embed.add_field(name = "Channels", value= "{0}".format(len(serv.channels)))
        embed.add_field(name = "Region" , value = serv.region)
        embed.set_footer(text="type ?role list to see server roles")
        try:
            embed.set_thumbnail(url = serv.icon_url)
        except:
            return
        await self.bot.send_message(ctx.message.channel, " ", embed=embed)
        
    @commands.command(pass_context = True, help = "creates an invite for one use, for 24 hours")
    async def serverinvite(self , ctx):
        try: 
            serverinvite = await self.bot.create_invite(ctx.message.server , max_age = 86400 , max_uses = 1)
            await self.bot.send_typing(ctx.message.channel)
            await asyncio.sleep(5)
            await self.bot.say(serverinvite)
        except discord.Forbidden:
            await self.bot.say("i dont have the `create instant invite` permission!")

    @commands.command(pass_context=True)
    async def remindme(self, ctx):
        xtx = ctx.message.content.split(" ")
        channel = ctx.message.channel
        author = ctx.message.author
        mention = ctx.message.author.mention
        if len(xtx) > 5: 
            to = ctx.message.content.split("to ", 1)[1]
            if xtx[3] == "seconds":
                await self.bot.send_message(channel , "Ok, ill remind you to **" + to +  "** in **" + xtx[2] + "** seconds!")
                await asyncio.sleep(int(xtx[2]))
                await self.bot.send_message(author , mention + ", " + to)
            if xtx[3] == "minutes" or xtx[3] == "minute":
                await self.bot.send_message(channel , "Ok, ill remind you to **" + to +  "** in **" + xtx[2] + "** minutes!")
                await asyncio.sleep(int(xtx[2]) * 60)
                await self.bot.send_message(author , mention + ", " + to)
            if xtx[3] == "hours" or xtx[3] == "hour":
                await self.bot.send_message(channel , "Ok, ill remind you to **" + to +  "** in **" + xtx[2] + "** hours!")
                await asyncio.sleep(int(xtx[2]) * 3600)
                await self.bot.send_message(author , mention + ", " + to)
        else: await self.bot.say("format of ?remindme is `?remindme in (length) (seconds/minutes/hours) to (info)`")

        
    @commands.command()
    async def invite(self):
        return await self.bot.say('You can invite my bot to your server with this link: <http://itzsplash.me/invite>')

    
    @commands.command(pass_context = True, aliases = ["tag" , 'tags'], help = "creates commands from discord, type \"=t help\"")
    async def t(self, ctx):
        xtx = ctx.message.content.split(" ")
        ser = ctx.message.server.id
        file = "/home/splash/tags2.json"
        output_file = "/home/splash/tags2.json"
        if len(xtx) == 1:
            await self.bot.say("proper use is  `=t (tag)`, to see server tags, type `=t list` ")
        elif len(xtx) == 3:
            await self.bot.say("you must include something after the tag")
        elif xtx[1] == "help":
            await self.bot.say("`=t create` to create a tag\n`=t edit` to edit a command\n`=t list` to show the server tags\n`=t delete` to delete a tag")
        elif xtx[1] == "create":
            open_file_object = open("/home/splash/tags2.json", 'r')
            decoded_json = json.load(open_file_object)
            decoded_json[ser][xtx[2]] = xtx[3:]
            jsoon = json.dumps(decoded_json)
            with open(output_file, 'w') as write_file_object:
                write_file_object.write(jsoon)
            await self.bot.say("created the {} tag".format(xtx[2]))
        elif xtx[1] == "delete":
            return

            
        elif xtx[1] == "edit":
            open_file_object = open("/home/splash/tags2.json", 'r')
            decoded_json = json.load(open_file_object)
            decoded_json[ser][xtx[2]] = xtx[3:]
            jsoon = json.dumps(decoded_json)
            with open(output_file, 'w') as write_file_object:
                write_file_object.write(json.dumps(decoded_json))
            await self.bot.say("edited the {} tag".format(xtx[1]))
        elif xtx[1] == "list":
            try:
                with open(file, 'r') as f:
                    datastore = json.load(f)
                    await self.bot.say("the tags for this server are; `{}`".format(" ".join(datastore[ser].keys())))
            except KeyError:
                return
            
        else: 
            try:
                with open(file, 'r') as f:
                    datastore = json.load(f) 
                    await self.bot.say(" ".join(datastore[ser][xtx[1]]))
            except KeyError:
                return
		
def setup(bot):
    bot.add_cog(information(bot))
