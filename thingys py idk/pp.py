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
                 "8==========D",
                 "8===========D",
                 "8============D",
                 "8==============D",
                 "8===============D",
                 "8=================D",
                 "8===================D",
                 "8====================D",
                 "8=====================D",
                 "8=======================D",
                 "8=========================D",
                 "8===============================================================================D",
                 "(i)"
                 ]
    pp = discord.Embed(title=f"PP Size of {member.name}#{member.discriminator}")
    pp.add_field(name="Your PP size is ", value=random.choice(responses))
    await ctx.send(embed=pp)
