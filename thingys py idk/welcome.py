@client.event
async def on_member_join(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    channel = member.guild.get_channel(int(channel_id))
    backround = Editor("pic.png")
    profile_image = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_image).resize((150, 150)).circle_image()
    poppins = Font.poppins(size=50, variant="bold")
    poppins_small = Font.poppins(size=20, variant="light")
    random_color = ["black", "white", "blue", "red", "green", "cyan", "brown", "orange", "yellow", "gray", "purple"]

    backround.paste(profile, (325, 90))
    backround.ellipse((325, 90), 150, 150, outline=random.choice(random_color), stroke_width=5)
    backround.text((400 - 2, 260 - 2), f"WELCOME TO {member.guild.name}", font=poppins, color="black", align="center")
    backround.text((400 + 2, 260 - 2), f"WELCOME TO {member.guild.name}", font=poppins, color="black", align="center")
    backround.text((400 - 2, 260 + 2), f"WELCOME TO {member.guild.name}", font=poppins, color="black", align="center")
    backround.text((400 + 2,  260 + 2), f"WELCOME TO {member.guild.name}", font=poppins, color="black", align="center")
    backround.text((400, 260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
    backround.text((400 - 1, 325 - 1), f"{member.name}#{member.discriminator}", font=poppins_small, color="black", align="center")
    backround.text((400 + 1, 325 - 1), f"{member.name}#{member.discriminator}", font=poppins_small, color="black", align="center")
    backround.text((400 - 1, 325 + 1), f"{member.name}#{member.discriminator}", font=poppins_small, color="black", align="center")
    backround.text((400 + 1,  325 + 1), f"{member.name}#{member.discriminator}", font=poppins_small, color="black", align="center")
    backround.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")


    file = File(fp=backround.image_bytes, filename="pic.png")
    await channel.send(f"Hello {member.mention}", file=file)


@client.command(name='welcome')
async def set_welcome_channel(ctx, channel: discord.TextChannel):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict[str(ctx.guild.id)] = str(channel.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)

    await ctx.send(f'Sent welcome channel for {ctx.message.guild.name} to {channel.name}')
