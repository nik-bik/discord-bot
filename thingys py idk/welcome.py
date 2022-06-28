@client.event
async def on_member_join(member):
    channel = client.get_channel(844235494749765654)
    backround = Editor("pic.png")
    profile_image = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_image).resize((150, 150)).circle_image()
    poppins = Font.poppins(size=50, variant="bold")
    poppins_small = Font.poppins(size=20, variant="light")

    backround.paste(profile, (325, 90))
    backround.ellipse((325,90), 150, 150, outline="black", stroke_width=5)
    backround.text((400, 260), f"WELCOME TO {member.guild.name}", color="black", font=poppins, align="center")
    backround.text((400, 260),f"WELCOME TO {member.guild.name}", color="black", font=poppins, align="center")
    backround.text((400, 325), f"{member.guild.name}#{member.discriminator}", color="white", font=poppins_small, align="center")


    file = File(fp=backround.image_bytes, filename="pic.png")
    await channel.send(f"Hello {member.mention}")
    await channel.send(file=file)
