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
