@client.command()
async def uwu(ctx):
    await ctx.send(f"uwu {round(client.latency * 1000)}ms")