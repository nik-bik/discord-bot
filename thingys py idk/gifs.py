kick_gifs = ["https://c.tenor.com/EcdG5oq7MHYAAAAC/shut-up-hit.gif",
             "https://c.tenor.com/3i8E86ZksXYAAAAC/sanji-luffy.gif",
             "https://c.tenor.com/m4_-1He6mC8AAAAC/taiga-aisaka-starling-bg-waifu.gif",
             "https://c.tenor.com/YRaOUlVOIccAAAAd/fight-anime.gif"]

hug_gifs = ["https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif",
            "https://c.tenor.com/we1trpFB2F0AAAAC/neko-hug.gif",
            "https://c.tenor.com/xIuXbMtA38sAAAAd/toilet-bound-hanakokun.gif",
            "https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif"]

bite_gifs = ["https://c.tenor.com/noV5mMA7T8oAAAAC/loli-bite.gif",
            "https://c.tenor.com/6HhJw-4zmQUAAAAC/anime-bite.gif",
            "https://c.tenor.com/JKUW0YQtyTAAAAAC/cheek-kiss.gif",
            "https://c.tenor.com/Nk-Eq8_ZiNwAAAAC/index-toaru.gif"]

kiss_gifs = ["https://c.tenor.com/yoMKK29AMQsAAAAC/kiss-toradora.gif",
             "https://c.tenor.com/lYKyQXGYvBkAAAAC/oreshura-kiss.gif",
             "https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif",
             "https://c.tenor.com/QQnlCFl0UTwAAAAC/maken-ki-kiss-cheek.gif"]

punch_gifs = ["https://c.tenor.com/EdV_frZ4e_QAAAAC/anime-naruto.gif",
              "https://c.tenor.com/gmvdv-e1EhcAAAAC/weliton-amogos.gif",
              "https://c.tenor.com/aEX1wE-WrEMAAAAC/anime-right-in-the-stomach.gif",
              "https://c.tenor.com/dhiZs4RULI0AAAAC/ippo-hajime-no-ippo.gif"]

slap_gifs = ["https://c.tenor.com/Ws6Dm1ZW_vMAAAAS/girl-slap.gif",
             "https://c.tenor.com/eU5H6GbVjrcAAAAC/slap-jjk.gif",
             "https://c.tenor.com/blbrtpA-HTgAAAAC/tapa.gif",
             "https://c.tenor.com/nBaCVW8855oAAAAC/anime-slap.gif"]

bonk_gifs = ["https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif",
             "https://c.tenor.com/FJsjk_9b_XgAAAAC/anime-hit.gif",
             "https://c.tenor.com/31WOy2yRK3QAAAAC/chuunibyou-hit.gif",
             "https://c.tenor.com/E6njrpISBV4AAAAC/bonk-hit.gif"]

#punch command#
@client.command()
async def punch(ctx, member: discord.Member ):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description= f"{ctx.author.mention} punches {member.mention}"
    )
    embed.set_image(url=(random.choice(punch_gifs)))

    await ctx.send(embed=embed)
#kiss command#
@client.command()
async def kiss(ctx, member: discord.Member):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description= f"{ctx.author.mention} kisses {member.mention}<3"
    )
    embed.set_image(url=(random.choice(kiss_gifs)))

    await ctx.send(embed=embed)
#bite command#
@client.command()
async def bite(ctx, member: discord.Member ):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description= f"{ctx.author.mention} bites {member.mention}"
    )
    embed.set_image(url=(random.choice(bite_gifs)))

    await ctx.send(embed=embed)
#hug#
@client.command()
async def hug(ctx, member: discord.Member):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description= f"{ctx.author.mention} hugs {member.mention}"
    )
    embed.set_image(url=(random.choice(hug_gifs)))

    await ctx.send(embed=embed)

#kick#
@client.command()
async def kick(ctx, member: discord.Member):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description= f"{ctx.author.mention} kicks {member.mention}"
    )
    embed.set_image(url=(random.choice(kick_gifs)))

    await ctx.send(embed=embed)

#slap#
@client.command()
async def slap(ctx, member: discord.Member):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description=f"{ctx.author.mention} slaps {member.mention}"
    )
    embed.set_image(url=(random.choice(slap_gifs)))

    await ctx.send(embed=embed)

#BONK#
@client.command()
async def bonk(ctx, member: discord.Member):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description=f"{ctx.author.mention} BONKS {member.mention}"
    )
    embed.set_image(url=(random.choice(bonk_gifs)))

    await ctx.send(embed=embed)
