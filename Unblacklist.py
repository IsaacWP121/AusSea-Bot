import discord
import AsyncDataBase
from embed import embed
async def Unblacklist(ctx):
	if (not isinstance(ctx.channel, discord.channel.DMChannel)):
		for i in ctx.mentions:
			if await AsyncDataBase.read("Blacklist", i.id) != False:
				await AsyncDataBase.remove("Blacklist", i.id)
				_ = "<@{}>".format(i.id)
				await ctx.channel.send(embed = await embed(ctx.author, "Removed", "",
			        fields=[{"value":_ + " Has been removed from the blacklist", "name":"____________"}], avatar=False))