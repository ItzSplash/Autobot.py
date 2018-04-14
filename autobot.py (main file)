import os
import time
import json
import string
import discord
import random
import asyncio
import operator
from discord.ext import commands

startup_extensions = ["fun", "administration" , "information", "trivia", "api"]
bot =commands.Bot(command_prefix ="?")


@bot.event
async def on_ready():
    print("bot is Online!, running version " + discord.__version__ + " of Discord.py")
    await asyncio.sleep(10)
    bot.remove_command("help")
    await bot.change_presence(game=discord.Game(name="Type ?help", type=0))


@bot.command(pass_context=True , help= 'to test if the bot is online')
async def ping(ctx):
    before = time.monotonic()
    await(await bot.ws.ping())
    after = time.monotonic()
    ping = str(round((after - before) * 1000))
    await bot.say("Pong! :ping_pong: {0}ms".format(ping))


'''
@bot.command(pass_context=True, )
async def summon(ctx):
    await bot.join_voice_channel(ctx.message.author.voice_channel)


    voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
    player = await voice.create_ytdl_player(ctx.message.content.split(" ")[1])
    player.start()
'''
@bot.command(pass_context = True )
async def dmmeboi(ctx):
    await bot.send_message(ctx.message.author , "hey uwu" )
@bot.command()
async def play():
    return
@bot.command(pass_context=True, hidden=True, help="Loads an extension")
async def load(ctx, extension_name : str):
    ext = extension_name.lower()
    if ctx.message.author.id == "197063788560777216": 
        try:
            bot.load_extension(ext)
        except (AttributeError, ImportError) as e:
            return await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        except:
            return await bot.say("Extension {} not found".format(ext))
        await bot.say("{} loaded.".format(ext))
    else: return

@bot.command(pass_context=True, help="Unload an extension")
async def unload(ctx, extension_name : str):
    if ctx.message.author.id == "197063788560777216": 
        bot.unload_extension(extension_name.lower())
        await bot.say("{} unloaded.".format(extension_name.lower()))

@bot.command(pass_context = True, aliases = ["eval"], hidden = True)
async def gggggggggg(ctx):
    return

@bot.event
async def on_server_join(server):
    await bot.send_message(bot.get_channel("380129924708827137"), "Rikka joined the " + server.name +  " server")
    try:
        await bot.send_message(bot.get_channel(server.id), "Thank you for inviting me to your server! I have a ton of commands for you to use! if you want a new command added, or there is an error with the bot, please message the bot owner at `Itz Splash#0012`. To start, type `?help`")
    except:
        return
@bot.event
async def on_message(message):
    chan = message.channel
    con = message.content
    if con.startswith("<@387406522499727360>"):
        await bot.send_message(chan,"hey whats up")
        waitmsg = await bot.wait_for_message(15, channel=message.channel, author = message.author)
        if waitmsg.content == "nothing much" or waitmsg.content == "nm":
            await bot.send_message(message.channel, "thats good, i'm doing well also")
        
    elif con.lower().startswith("?eval") and message.author.id == "197063788560777216":
        try:
            before = time.monotonic()
            await(await bot.ws.ping())
            after = time.monotonic()
            ping = str(round((after - before) * 1000))
            split = "================================"
            await bot.send_message(chan , "evaluating...")
            await asyncio.sleep(1)
            await bot.send_message(chan,content="```py\nInput: {0}\n{1}\n".format(message.content[6:] , split) + "Output: " + str(eval(message.content[6:])) + "````type:" + str(eval.__name__) + "  eval time: {}ms".format(ping) +"`")
        except Exception as e:
            await bot.send_message(chan, "```py\n" + repr(e) + "```")

    if con.lower().startswith("?help"):
        if message.author.bot: return
        else:
            em = discord.Embed(description=None, colour=message.author.colour)
            em.add_field(name= "Administration:", value= "voicekick, role, purge, ban, unban, kick, mute, unmute")
            em.add_field(name= "Fun:", value= "choose, fancy, calculator, roll, suicide, mal, rps, illegal, rem, rolldice, 8ball, say")
            em.add_field(name= "Information:", value= "discrim, user, server, info, avatar, userid, remindme, serverinvite, nickname, invite")
            #em.add_field(name= "Gambling:", value= "credits, flip, spin")
            em.add_field(name= "Games:", value="osu, rlrank, fortnite")
            em.set_footer(text="any errors or suggestions, message Itz Splash#0012")
            await bot.send_message(message.channel, embed=em)
    await bot.process_commands(message)
    bot.remove_command("help")

  
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension.lower())
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension.lower(), exc))



bot.run("token")
