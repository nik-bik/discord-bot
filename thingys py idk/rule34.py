
ltime = time.asctime(time.localtime())
Client = discord.Client()
r = rule34.Rule34


def xmlparse(str):
    root = et.parse(u.urlopen(str))
    for i in root.iter('post'):
        fileurl = i.attrib['file_url']
        return fileurl


def xmlcount(str):
    root = et.parse(u.urlopen(str))
    for i in root.iter('posts'):
        count = i.attrib['count']
        return count


def pidfix(str):
    ye = int(xmlcount(r.urlGen(tags=str, limit=1)))
    ye = ye - 1
    return ye


def rdl(str, int):
    print(f'[INFO {ltime}]: integer provided: {int}')

    if int > 2000:
        int = 2000
    if int == 0:
        int == 0
        print(f'[INFO {ltime}]: Integer is 0, accommodating for offset overflow bug. ')
    elif int != 0:
        int = random.randint(1, int)
    print(f'[INFO {ltime}]: integer after randomizing: {int}')
    xurl = r.urlGen(tags=str, limit=1, PID=int)
    print(xurl)
    wr = xmlparse(xurl)

    if 'webm' in wr:
        if 'sound' not in str:
            if 'webm' not in str:
                print(f'[INFO {ltime}]: We got a .webm, user didnt specify sound. Recursing. user tags: {str}')
                wr = rdl(str, pidfix(str))
        else:
            pass
    elif 'webm' not in wr:
        print(f'[INFO {ltime}]: Not a webm, dont recurse.')
    return wr


async def statuschange():
    while True:
        await client.change_presence(activity=discord.Game(name='...'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name='w-w-what'))
        await asyncio.sleep(10)


@client.command()
async def r4(ctx, *arg):
    answer = ''
    arg = str(arg)
    arg = arg.replace(',', '')
    arg = arg.replace('(', '')
    arg = arg.replace(')', '')
    arg = arg.replace("'", '')
    print(f'[DEBUG {ltime}]: arg is now {arg}')
    waitone = await ctx.send("***:desktop: We're polling Rule34! Please wait a few seconds.***")
    newint = pidfix(arg)
    if newint > 2000:
        newint = 2000
        answer = rdl(arg, random.randint(1, newint))
    if newint > 1:

        answer = rdl(arg, random.randint(1, newint))
    elif newint < 1:
        if newint == 0:
            answer = rdl(arg, 0)
        elif newint != 0:
            answer = rdl(arg, 1)

    if 'webm' in answer:
        await waitone.delete
        await ctx.send(answer)
    elif 'webm' not in answer:
        embed = discord.Embed(title=f'Rule34: {arg}', color=ctx.author.color)
        embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
        embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
        embed.set_image(url=f'{answer}')
        embed.set_footer(text="",
                         icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
        waitone.delete
        await ctx.send(embed=embed)
