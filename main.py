import discord
from discord.ext import commands #imports

client = commands.Bot(command_prefix = "&", self_bot=False) #initialising client

@client.event #decorating this fucntion as an event
async def on_message(message):

	#if the channel is a dm and the author of the message variable is not the bot
	if isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user): 
		await message.channel.send("Hi there! If you need some help, please react to this message so we can get started.") #sends back the same message (for now, it'll send a helpful response message soon)
	
	# if the channel is a dm, the messsage author isn't the bot itself and the message content matches the same str as below (janky but will be moved to a file soon) 
	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author ==
		client.user) and (message.content == "Hi there! If you need some help, please react to this message so we can get started."): 
		await message.add_reaction("✅")

	# if the channel is a dm, the messsage author isn't the bot itself and the message content matches the same str as below (janky but will be moved to a file soon) 
	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author == 
		client.user) and (message.content == "-----------------\nWhat category would you place your request under?\n\n1⃣ Moderation\n\n2⃣ Tournaments\n\n3⃣ Mentoring\n\n4⃣ Other\n-----------------"):
		await message.add_reaction("1⃣") #add the reactions to the bot so that the user can select a bot
		await message.add_reaction("2⃣")
		await message.add_reaction("3⃣")
		await message.add_reaction("4⃣")


	@client.event
	async def on_reaction_add(reaction, user):

		# when a message has the "tick" emoji added, the user id is not the bot's and the channel is a dm 
		if reaction.emoji == "✅" and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nWhat category would you place your request under?\n\n1⃣ Moderation\n\n2⃣ Tournaments\n\n3⃣ Mentoring\n\n4⃣ Other\n-----------------")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == "1⃣" and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm		
		if reaction.emoji == "2⃣" and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == "3⃣" and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == "4⃣" and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nPlease type your message below")
client.run("token here")
