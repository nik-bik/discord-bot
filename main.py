import json
import discord
import random
from discord.ext import commands
import youtube_dl
import os
import datetime
import asyncio
import requests
import socket

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

#
@client.command()
async def iplookup(ctx, *, ipaddr: str = '9.9.9.9'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}?key=;3")
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'IP Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'IP Name', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.set_footer(text='\u200b')
            em.timestamp = datetime.datetime.utcnow()
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed = em)


#music#
@client.command()
async def play(ctx, url: str, name):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=name)

    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("iam out peace")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("no music play no pause")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("music play no pause")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop


# give role on react #
@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:

        with open("reactrole.json") as react_file:
            data = json.load(react_file)
            for x in data:
                if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x["role_id"])
                    await payload.member.add_roles(role)


# remove role on react #
@client.event
async def on_raw_reaction_remove(payload):
    with open("reactrole.json") as react_file:
        data = json.load(react_file)
        for x in data:
            if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
                role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x["role_id"])
                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


# react command #

@client.command()
@commands.has_role("Admin")
async def reactrole(ctx, emoji, role: discord.Role, *, message):
    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)
    with open("reactrole.json") as json_file:
        data = json.load(json_file)

        new_react_role = {
            "role_name": role.name,
            "role_id": role.id,
            "emoji": emoji,
            "message_id": msg.id
        }
        data.append(new_react_role)
    with open("reactrole.json", "w") as j:
        json.dump(data, j, indent=4)


# ping #
@client.command()
async def uwu(ctx):
    await ctx.send(f"uwu {round(client.latency * 1000)}ms")


@client.command()
async def web(ctx):
    await ctx.send("this is not a feature yet ;~;")


# funny 8ball thingy #
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["no uwu",
                 "yes uwu",
                 "maybe uwu",
                 "u can try uwu",
                 "iam sleepy ask that later =3=",
                 "me say yes uwu",
                 "me say no uwu",
                 "don't do that uwu",
                 "don't ask that >-<"]
    await ctx.send(random.choice(responses))


# funny pp size mesure #
@client.command(aliases=["size"])
async def pp(ctx, member: discord.Member, *, reason=None):
    responses = ["8D",
                 "8=D",
                 "8==D",
                 "8===D",
                 "8====D",
                 "8=====D",
                 "8======D",
                 "8=======D",
                 "8========D",
                 "8=========D",
                 "8==========D"
                 ]
    await ctx.send(f"{member.mention} {random.choice(responses)}")


# coin flip #
@client.command(aliases=["coin flip", "coin"])
async def coin_flip(ctx):
    responses = ["heads uwu",
                 "tails uwu"]
    await ctx.send(f"U got {random.choice(responses)}")


# clear command #
@client.command()
@commands.has_role("Admin")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# kick command #
@client.command()
@commands.has_permissions(kick_members=True)
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"kicked {member.mention}, he was a miene ;~;")


# ban command #
@client.command()
@commands.has_permissions(ban_members=True)
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member.mention}, he was a miene ;~; ")


# funny token thingy #
client.run(";3")

