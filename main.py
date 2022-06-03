import json
import discord
import random
from discord.ext import commands
import timestamp
from googleapiclient.discovery import build
import youtube_dl
import os
import websocket
import datetime
import asyncio
import requests
import socket
import rule34
import time
import xml.etree.ElementTree as et
import urllib.request as u
import urllib

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


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("command not found. Type in .help for all of the commands")

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
