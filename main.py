import discord
from discord.ext import commands #imports

client = commands.Bot(command_prefix = "&", self_bot=False) #initialising client

@client.event
async def on_connect():
	#assigning variables
	global tick
	global one
	global two
	global three
	global four
	global userInputMode
	global category
	global categoryIds
	global userMessage
	four = "4⃣"
	tick = "✅"
	one = "1⃣"
	two = "2⃣"
	three ="3⃣"
	userInputMode = False
	category = 0
	userMessage = ""
	categoryIds = {1:750590527249973369, 2:750590465149239346, 3:750590556777873429, 4:750613194875076618}

@client.event #decorating this fucntion as an event
async def on_message(message):
	global userInputMode
	global category
	global userMessage


	if isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user) and "&cancel" in message.content:
		userInputMode = False
		category = 0
		userMessage = ""

	#if the channel is a dm and the author of the message variable is not the bot
	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user) and userInputMode != True: 
		msg = await message.channel.send("Hi there! If you need some help, please react to this message so we can get started.\nYou can cancel at any time with &cancel") #sends back the same message (for now, it'll send a helpful response message soon)
		await msg.add_reaction(tick)

	# if the channel is a dm, the messsage author isn't the bot itself and the message content matches the same str as below (janky but will be moved to a file soon) 
	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author == 
		client.user) and (message.content == "-----------------\nWhat category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other\n-----------------") and userInputMode != True:
		await message.add_reaction(one) #add the reactions to the bot so that the user can select a bot
		await message.add_reaction(two)
		await message.add_reaction(three)
		await message.add_reaction(four)

	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user) and userInputMode == True and message.content == "&send":
		guild = client.get_guild(713704403567378473)
		userMessage = userMessage[:-1]
		if category != 0:
			channel = guild.get_channel(categoryIds[category])
			embed = discord.Embed(colour = discord.Colour.blue(), title="{}{}".format(message.author.name, message.author.discriminator), description= "<@{}>".format(message.author.id))
			embed.set_thumbnail(url="{}".format(message.author.avatar_url))
			embed.add_field(name="Message", value='"{}"'.format(userMessage))
			await channel.send(embed=embed)

	elif isinstance(message.channel, discord.channel.DMChannel) and (message.author != client.user) and userInputMode == True:
			userMessage = "{}{}\n".format(userMessage, message.content)
	#

	async def clear_react(message):
		global one
		global two
		global three
		global four
		lis = [one, two, three, four]
		for i in lis:
			await message.remove_reaction(i, client.user)

	@client.event
	async def on_reaction_add(reaction, user):
		global userInputMode
		global category
		# when a message has the "tick" emoji added, the user id is not the bot's and the channel is a dm 
		if reaction.emoji == tick and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await reaction.message.channel.send("-----------------\nWhat category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other\n-----------------")

		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == one and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 1
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm		
		if reaction.emoji == two and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 2
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == three and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 3		
		# when a message has the "one" emoji added, the user id is not the bot's and the channel is a dm
		if reaction.emoji == four and user != client.user and isinstance(message.channel, discord.channel.DMChannel):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 4	

if __name__ == "__main__":
	client.run("token here")
