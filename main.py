import discord, random, DiscordUtils, timestamp, youtube_dl, os, websocket, asyncio, requests, datetime, socket, rule34, time, xml.etree.ElementTree as et, urllib.request as u, urllib, json
from discord.ext import commands
from googleapiclient.discovery import build
from easy_pil import Editor, load_image_async, Font

from discord import File


client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


# start something msg idk why u ask me#
@client.event
async def on_ready():
    greeting = ["hewo",
                ";3",
                "iam back uwu",
                "welcome home",
                "just leave ur stuff here",
                "ON",
                "iam lazy bruh"]
    print(random.choice(greeting))
    await client.change_presence(activity=discord.Game(name='w-w-what'))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("command not found. Type in .help for all of the commands")
#logger#
@client.event
async def on_message(message):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    await client.process_commands(message)
    with open("logs.txt", "a") as text_file:
        print(f"<{st}> <{message.guild.name}> <{message.author}> <{message.id}>  {message.content}", file=text_file)

        
#welcome#
exec(open("thingys py idk/welcome.py").read())

#gifs#
exec(open("thingys py idk/gifs.py").read())

#meme#
exec(open("thingys py idk/meme.py").read())
        
#rule34#
exec(open("thingys py idk/rule34.py").read())
#search engine#
exec(open("thingys py idk/search engine.py").read())

#iplookup#
exec(open("thingys py idk/iplookup.py").read())

#music#
exec(open("thingys py idk/music.py").read())

# react command #
exec(open("thingys py idk/react command.py").read())

# ping #
exec(open("thingys py idk/ping.py").read())

#web#
exec(open("thingys py idk/web.py").read())

# funny 8ball thingy #
exec(open("thingys py idk/8ball.py").read())

# funny pp size mesure #
exec(open("thingys py idk/pp.py").read())

# coin flip #
exec(open("thingys py idk/coinflip.py").read())

#admin commands#
exec (open("thingys py idk/admin.py").read())

# funny token thingy #
client.run(";3")
