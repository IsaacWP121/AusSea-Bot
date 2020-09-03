import discord
from discord.ext import commands #imports

client = commands.Bot(command_prefix = "&", self_bot=False) #initialising client

@client.event #decorating this fucntion as an event
async def on_message(message):
	if isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user): #if the channel is a dm and the author of the message variable is not the bot
		await message.channel.send(message.content) #sends back the same message (for now, it'll send a helpful response message soon)

client.run("token here")
