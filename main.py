import discord
from discord.ext import commands #imports

client = commands.Bot(command_prefix = "&", self_bot=False) #initialising client

#assigning variables
tick = "✅"
one = "1⃣"
two = "2⃣"
three ="3⃣"
four = "4⃣"

@client.event #decorating this fucntion as an event
async def on_message(message):

	#if the channel is a dm and the author of the message variable is not the bot
	if isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user): 
		x = await message.channel.send("Hi there! If you need some help, please react to this message so we can get started.") #sends back the same message (for now, it'll send a helpful response message soon)
		await x.add_reaction(tick)

	# if the channel is a dm, the messsage author isn't the bot itself and the message content matches the same str as below (janky but will be moved to a file soon) 
	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author == 
		client.user) and (message.content == "-----------------\nWhat category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other\n-----------------"):
		await message.add_reaction(one) #add the reactions to the bot so that the user can select a bot
		await message.add_reaction(two)
		await message.add_reaction(three)
		await message.add_reaction(four)


	@client.event
	async def on_reaction_add(reaction, user):

		# when a message has the "tick" emoji added, the user id is not the bot's and the channel is a dm 
		if reaction.emoji == tick and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nWhat category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other\n-----------------")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == one and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm		
		if reaction.emoji == two and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == three and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == four and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
client.run("token here")
