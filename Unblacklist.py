import discord
import AsyncDataBase
async def Unblacklist(ctx):
	if (not isinstance(ctx.channel, discord.channel.DMChannel)):
		for i in ctx.mentions:
			if await AsyncDataBase.read("Blacklist", i.id) != False:
				await AsyncDataBase.remove("Blacklist", i.id)