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
	tick = "✅"
	one = "1⃣"
	two = "2⃣"
	three ="3⃣"
	four = "4⃣"
	userInputMode = False
	category = 0
	userMessage = ""
	categoryIds = {1:750590527249973369, 2:750590465149239346, 3:750590556777873429, 4:750613194875076618} #all the different channel id's

@client.event #decorating this fucntion as an event
async def on_message(message):
	global userInputMode
	global category
	global userMessage

	# if the message is not a dm or if message is from bot, return (Do not proceed)
	if (not isinstance(message.channel, discord.channel.DMChannel) or message.author == client.user):
		return
	
	# if its the cancel command reset the bot's state
	if ("&cancel" in message.content):
		userInputMode = False
		category = 0
		userMessage = ""

	#if the message variable is not the bot
	elif (userInputMode != True): 
		msg = await message.channel.send("Hi there! If you need some help, please react to this message so we can get started.\nYou can cancel at any time with &cancel") #sends back the same message (for now, it'll send a helpful response message soon)
		await msg.add_reaction(tick)

	# if its the send command the get the server, remove the \n that was left at the end from the conjoining of all the users messages and embed/send it
	elif (userInputMode == True and message.content == "&send"):
		guild = client.get_guild(713704403567378473)
		userMessage = userMessage[:-1]
		if category != 0:
			channel = guild.get_channel(categoryIds[category])
			embed = discord.Embed(colour = discord.Colour.blue(), title="{}{}".format(message.author.name, message.author.discriminator), description= "<@{}>".format(message.author.id))
			embed.set_thumbnail(url="{}".format(message.author.avatar_url))
			embed.add_field(name="Message", value='"{}"'.format(userMessage))
			await channel.send(embed=embed)

	# join the messages and add a newline between them
	elif (userInputMode == True):
		userMessage = "{}{}\n".format(userMessage, message.content)
	#

	#this is to make sure the user cant add a second reaction and screw the bot over, itll be called after the user chooses a reaction
	async def clear_react(message):
		global one
		global two
		global three
		global four
		lis = [one, two, three, four]
		for i in lis:
			await message.remove_reaction(i, client.user) #cant remove all due to not being able to remove the users

	@client.event
	async def on_reaction_add(reaction, user):
		global userInputMode
		global category
		
		#  If the user id is the bot's or if the channel is not a dm, return
		if(user == client.user or not isinstance(message.channel, discord.channel.DMChannel)):
			return		
		
		# when a message has the "tick" emoji added
		if (reaction.emoji == tick):
			msg = await reaction.message.channel.send("-----------------\nWhat category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other\n-----------------")
			await msg.add_reaction(one) #add the reactions to the bot so that the user can select a bot
			await msg.add_reaction(two)
			await msg.add_reaction(three)
			await msg.add_reaction(four)
			
		# when a message has the "one" emoji added
		elif (reaction.emoji == one):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 1
			
		# when a message has the "two" emoji added		
		elif (reaction.emoji == two):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 2
			
		# when a message has the "three" emoji added
		elif (reaction.emoji == three):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 3	
			
		# when a message has the "four" emoji added
		elif (reaction.emoji == four):
			await clear_react(reaction.message)
			await reaction.message.channel.send("Please type your message below and use &send to submit your message to the staff")
			userInputMode = True
			category = 4
#when the user joins the server the bot will welcome them
@client.event
async def on_member_join(member):
	guild = client.get_guild(179077200149086209)
	channel = guild.get_channel(179077200149086209)
	await channel.send("Hi <@{}>, welcome to Aus SEA Brawlhalla! Please checkout #rules and go #set-your-roles, enjoy your stay!".format(member.id))

if __name__ == "__main__":
	client.run("token here")
