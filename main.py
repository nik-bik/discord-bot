import json
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("good morning u cutie")

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
    responses = ["small uwu",
                 "micro uwu",
                 "smaller then micro uwu",
                 "sowy its smoll uwu",
                 "normal size uwu",
                 "big 0-0",
                 "MASSIVE",
                 "NO CAP ITS SMALL UWU"]
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
    await ctx.send (f"kicked {member.mention}, he was a miene ;~;")


# ban command #
@client.command()
@commands.has_permissions(ban_members=True)
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member.mention}, he was a miene ;~; ")


# funny token thingy #
client.run("ODQ0MjMxOTYyMTEzMjEyNDE3.YKPaSA.1uCDhuafIsZ7Z1XPe0IImIBO_4s")
