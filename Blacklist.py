import discord
import AsyncDataBase
from embed import embed
async def Blacklist(ctx):
    if (not isinstance(ctx.channel, discord.channel.DMChannel)):
        try:
            if ctx.content.split()[1].lower() == "list":
                try:
                    values = await AsyncDataBase.readall("Blacklist")
                    _ = ""
                    for i in values:
                        _ = _ + "<@{}> ".format(i[0])
                    _ = _[:-1]
                    await ctx.channel.send(embed = await embed(ctx.author, "Currently Blacklisted", "",
			    fields=[{"value":_, "name":"____________"}], avatar=False))
                except:
                    await ctx.channel.send(embed = await embed(ctx.author, "Currently Blacklisted", "",
			    fields=[{"value":"None currently blacklisted", "name":"____________"}], avatar=False))

        except:
            print("error")

        for i in ctx.mentions:
            if await AsyncDataBase.read("Blacklist", i.id) == False:
                await AsyncDataBase.addEntry("Blacklist", i.id)