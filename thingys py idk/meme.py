@client.command()
async def meme(ctx):
    memeAPI = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")
    memeData=json.load(memeAPI)

    memeUrl =memeData['url']
    memeName = memeData['title']
    memePoster = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']

    embed = discord.Embed(title=memeName)
    embed.set_image(url=memeUrl)
    embed.set_footer(text=f"Meme by {memePoster} | Subreddit {memeSub} | Post: {memeLink}")
    await ctx.send(embed=embed)
