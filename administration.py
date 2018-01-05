import discord, asyncio
from discord.ext import commands

class administration():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True , help= "deletes a large amount of messages",  aliases=["prune"])
    async def purge(self, ctx):
        xtx = ctx.message.content.split(" ")
        if ctx.message.author.permissions_in(ctx.message.channel).manage_messages == True: 
            if len(xtx) == 1:
                await self.bot.say("**Must Provide a Number**")
            else:
                await self.bot.purge_from(ctx.message.channel , limit = int(xtx[1]),  check=None)
                v = await self.bot.say("deleted **{}** messages".format(xtx[1]))
                await asyncio.sleep(3)
                await self.bot.delete_message(v)

        else: await self.bot.say("You don't have the **manage messages** permission!")
    @commands.command(pass_context = True)
    async def voicekick(self , ctx):
        id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
        member = ctx.message.server.get_member(id)
        if len(ctx.message.content.split(" ")) == 1:
            await self.bot.say("*must include a user to move*")
        else:
            try:
                await self.bot.move_member(member, ctx.message.server.afk_channel)
            except:
                await self.bot.say("must create an AFK channel")
    @commands.command(pass_context=True , help="kicks a certain user")
    async def kick(self , ctx):
        xtx = ctx.message.content.split(" ")
        if ctx.message.author.permissions_in(ctx.message.channel).kick_members == True:
            if len(xtx) == 1:
                await self.bot.say("**Must Provide a User**")
            else:
                await self.bot.say("Are you sure you want to kick this person? Type `yes or no`.")
                waitmsg = await self.bot.wait_for_message(15, channel=ctx.message.channel, author = ctx.message.author)
                if waitmsg.content.lower() == "no":
                    await self.bot.say("user was not kicked")
                if waitmsg.content.lower() is None:
                    await self.bot.say("user was not kicked")
                if waitmsg.content.lower() == "yes":
                    id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
                    member = ctx.message.server.get_member(id)
                    if(member == None):
                        return await self.bot.say("User not found!")
                    try:
                        await self.bot.kick(member)
                        await self.bot.say("**Kicked** " + member.name)
                    except:
                        return await self.bot.say("**I don't have enough permissions**!!") 
        else:
            await self.bot.say("**You don't have enough permissions to kick someone!**")
    
    @commands.command(pass_context=True, help= "bans a given user")
    async def ban(self , ctx):
        if ctx.message.author.permissions_in(ctx.message.channel).ban_members == True:
            xtx = ctx.message.content.split(" ") 
            if len(xtx) == 1:
                await self.bot.say("**Must Provide a User**")
            else:
                await self.bot.say("Are you sure you wanna ban this person? Type `yes or no`.")
                waitmsg = await self.bot.wait_for_message(15, channel=ctx.message.channel, author = ctx.message.author)
                if waitmsg.content.lower() == "no":
                    await self.bot.say("user was not banned")
                if waitmsg.content.lower() is None:
                    await self.bot.say("user was not banned")
                if waitmsg.content.lower() == "yes":
                    id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
                    member = ctx.message.server.get_member(id)
                    if(member == None):
                        return await self.bot.say("User not found!")
                    try:
                        await self.bot.ban(member , delete_message_days=1)
                        await self.bot.say(member.name + " *Got the* **BAN HAMMER**")
                    except:
                        return await self.bot.say("*I don't have permissions!!*") 
        else:
            await self.bot.say("*You don't have enough permissions to ban someone!*")

    @commands.command(pass_context = True , help = "mutes user mentioned")
    async def mute(self , ctx):
        xtx = ctx.message.content.split(" ")
        roles = ctx.message.server.roles
        muted_role = discord.utils.get(roles, name = "Muted")
        id = ctx.message.content.split(" ")[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
        member = ctx.message.server.get_member(id)
        if ctx.message.author.permissions_in(ctx.message.channel).manage_roles == True:
            try:
                if len(xtx) == 2:
                    muted = "muted " + xtx[1]
                    await self.bot.add_roles(member , muted_role)
                    await self.bot.say(muted)
                if len(xtx) == 4:
                    muted2 = "muted " + xtx[1] + " for " + xtx[2] + " " + xtx[3]
                    if xtx[3].lower() == "seconds":
                        await self.bot.add_roles(member , muted_role)
                        await self.bot.say(muted2)
                        await asyncio.sleep(int(xtx[2]))
                        await self.bot.remove_roles(member , muted_role)
                    if xtx[3].lower() == "minutes":
                        await self.bot.add_roles(member , muted_role)
                        await self.bot.say(muted2)
                        await asyncio.sleep(int(xtx[2]) * 60)
                        await self.bot.remove_roles(member , muted_role)
                    if xtx[3].lower() == "hours":
                        await self.bot.add_roles(member , muted_role)
                        await self.bot.say(muted2)
                        await asyncio.sleep(int(xtx[2]) * 3600)
                        await self.bot.remove_roles(member , muted_role)
            except discord.FORBIDDEN:
                await self.bot.say("*I dont have enough permissions!*")
        else: await self.bot.say("You must have the `manage_roles` permission")
    @commands.command(pass_context = True , help = "unmutes user mentioned")
    async def unmute(self , ctx , member:discord.Member):
        if len(ctx.message.content.split(" "))==1:
            await self.bot.say("Must provide a user")
        if ctx.message.author.permissions_in(ctx.message.channel).manage_roles == True:
            muted_role = discord.utils.get(ctx.message.server.roles, name = "Muted")
            await self.bot.remove_roles(member , muted_role)
            await self.bot.say("unmuted {}".format(member))

        else: await self.bot.say("You must have the `manage_roles` permission")

    @commands.command(pass_context =True)
    async def role(self, ctx):
        xtx = ctx.message.content.split(" ")
        author = ctx.message.author
        se = ctx.message.server
        tree = ctx.message.content[13:]
        if len(xtx) == 1:
            await self.bot.say("to use this command, you type ?role (add/remove/delete/create) (role name) such as `?role add Autobot`")
        else:
            if xtx[1] == "remove":
                if len(xtx) == 2:
                    await self.bot.say("must include a role to remove")
                else:
                    try:
                        role_name = ctx.message.content[13:].lower() 
                        for role in se.roles:
                            if role.name.lower() == role_name:
                                await self.bot.remove_roles(author , role)
                                variable = await self.bot.say("{0}, you removed the **{1}** role".format(author.display_name, role_name ))
                                await asyncio.sleep(5)
                                await self.bot.delete_message(variable)
                    except:
                        variable = await self.bot.say("*I dont have enough permissions!*")
                        await asyncio.sleep(6)
                        await self.bot.delete_message(variable)
            if xtx[1] == "add":
                if len(xtx) == 2:
                    await self.bot.say("must include a role to add")
                else:
                    try:
                        role_name = ctx.message.content[10:].lower()
                        for role in se.roles:
                            if role.name.lower() == role_name: 
                                await self.bot.add_roles(author , role)
                                variable = await self.bot.say("{0}, you received the **{1}** role".format(author.display_name, role_name))
                                await asyncio.sleep(5)
                                await self.bot.delete_message(variable)
                    except:
                        variable = await self.bot.say("*I dont have enough permissions!*")
                        await asyncio.sleep(6)
                        await self.bot.delete_message(variable)
            if xtx[1] == "create":
                if len(xtx) == 2:
                    await self.bot.say("must include a role to create")
                else: 
                    if author.permissions_in(ctx.message.channel).manage_roles == True:
                        role_name = ctx.message.content[13:].lower() 
                        for role in se.roles:
                            if role.name.lower() == role_name:
                                await self.bot.create_role(se , role_name)
                                await self.bot.say("created the {} role!".format(role_name))
                    else: return
            if xtx[1] == "delete":
                if len(xtx) == 2:
                    await self.bot.say("must include a role to delete")
                else: 
                    if author.permissions_in(ctx.message.channel).manage_server == True:
                        role_name = ctx.message.content[14:].lower() 
                        for role in se.roles:
                            if role.name.lower() == role_name:
                                await self.bot.delete_role(se , role_name)
                                await self.bot.say("created the {} role!".format(role_name))
                    else: return
            if xtx[1] == "list":
                xtx = ctx.message
                em = discord.Embed(title= "Server Roles", description="{}".format(', '.join(list(map(lambda x:x.name, ctx.message.server.roles)))), colour=ctx.message.author.colour)
                await self.bot.send_message(xtx.channel, embed=em)


def setup(bot):
    bot.add_cog(administration(bot))
