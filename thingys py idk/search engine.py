api_key = "AIzaSyBRK-61Y-rcHCZDA0M6i58eeV0tsdSOfJA"
@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="de90d356f1ec3f07f", searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1,)