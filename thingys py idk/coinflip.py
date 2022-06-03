@client.command(aliases=["coin flip", "coin"])
async def coin_flip(ctx):
    responses = ["heads uwu",
                 "tails uwu"]
    await ctx.send(f"U got {random.choice(responses)}")
