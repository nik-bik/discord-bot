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
