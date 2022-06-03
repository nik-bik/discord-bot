@client.command()
async def iplookup(ctx, *, ipaddr: str = '9.9.9.9'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}?key=")
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
