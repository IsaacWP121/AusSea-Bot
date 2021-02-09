import discord
import AsyncDataBase
from embed import embed
async def Blacklist(ctx, client=None, id=None):
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
                return

        except:
            print("error")

        try:
            if id != None:
                await client.get_user(id).send(embed = 
				await embed(ctx.author, "Blacklisted", "",
			fields=[{"value":"I have banned you from using this bot, Ima go get some milk, I'll be back in an hour", 
			"name":"____________"}], avatar=False))
                _ = "<@{}>".format(id)
                await ctx.channel.send(embed = await embed(ctx.author, "Added", "",
                    fields=[{"value":_ + " Has been added to the blacklist", "name":"____________"}], avatar=False))
                return
        except:
            print("error")
        try:
            for i in ctx.mentions:
                if await AsyncDataBase.read("Blacklist", i.id) == False:
                    await AsyncDataBase.addEntry("Blacklist", i.id)
                    _ = "<@{}>".format(i.id)
                    await ctx.channel.send(embed = await embed(ctx.author, "Added", "",
                        fields=[{"value":_ + " Has been added to the blacklist", "name":"____________"}], avatar=False))
                    return
        except:
            print("error")


        try:
            await ctx.channel.send(embed = await embed(ctx.author, "The fuck", "",
                fields=[{"value":"Life is hard, try using &blacklist list or &blacklist <user>", "name":"____________"}], avatar=False))
        except:
            print("error")