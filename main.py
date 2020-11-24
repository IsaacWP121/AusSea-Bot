import discord, datetime, AsyncDataBase, Token #imports
from discord.ext import commands 
from string import digits
from embed import embed
from send import Send

client = commands.Bot(command_prefix = "&", self_bot=False) #initialising client

#this is to make sure the user cant add a second reaction and screw the bot over, it'll be called after the user chooses a reaction
async def clear_react(message):#function to reset reactions
	global one
	global two
	global three
	global four
	lis = [one, two, three, four]
	for i in lis:
		await message.remove_reaction(i, client.user) #cant remove all due to not being able to remove the users

# this is used to print out in terminal when the bot is ready
@client.event
async def on_ready():
	print("{} is ready".format(client.user))


@client.event
async def on_connect():
	#assigning variables & making them global so that I can access them from other functions
	global tick
	global one
	global two
	global three
	global four
	global userInputMode
	global category
	global categoryIds
	global eyes
	global noEntrySign
	global redCross
	global TimeoutTime
	TimeoutTime = None
	four = "4⃣"
	tick = "✅"
	one = "1⃣"
	two = "2⃣"
	three ="3⃣"
	eyes = u"\U0001F440"
	noEntrySign = u"\U0001F6AB"
	redCross = 	u"\u274C"
	userInputMode = False
	category = 0
	await AsyncDataBase.create()
	categoryIds = {1:750590527249973369, 2:750590465149239346, 3:750590556777873429, 4:750613194875076618}


@client.event #decorating this function as an event
async def on_message(message):
	global userInputMode
	global category
	global TimeoutTime
	# if the message is not a dm or if message is from bot, return (Do not proceed)
	#Blacklist/Unblacklist someone
	if (not isinstance(message.channel, discord.channel.DMChannel)):
		#if message.content == "&blacklist":
		
		#if message.content == "&unblacklist":


		return
	
	if message.author == client.user:
		return

	if (await AsyncDataBase.read("Blacklist", message.author.id)):
		return
	# if its the cancel command reset the bot's state
	if ("&cancel" == message.content):
		userInputMode = False
		category = 0

	#if the message variable is not the bot
	elif (userInputMode != True):
		msg = await message.channel.send(embed = await embed(message.author, "Hey!", "", fields=
		[{"value":"Hi there! If you need some help, please react to this message so we can get started.\nYou can cancel at any time with &cancel", "name":"____________"}],
		 avatar=False)) #sends back the same message (for now, it'll send a helpful response message soon)
		await msg.add_reaction(tick)

		# if its the send command the get the server, remove the \n that was left at the end from the conjoining of all the users messages and embed/send it
	elif (userInputMode == True and message.content == "&send"):
		await Send(client, TimeoutTime, userMessage, category, categoryIds, message)

		# join the messages and add a newline between them
	elif (userInputMode == True):
		if datetime.datetime.now() <= TimeoutTime:
			_ = await AsyncDataBase.read("User_Messages", message.author.id)
			if _ == False:
				await AsyncDataBase.addEntry("User_Messages", (message.author.id), Message=message.content)
			else:
				x = "{} {}".format([x[1] for x in _][0], message.content)
				print(x)
				await AsyncDataBase.update("User_Messages", (x, message.author.id))
		else:
			userInputMode = False #resets the variables
			category = 0
			userMessage = ""
			TimeoutTime = None
			await message.channel.send(embed = await embed(message.author, "Timeout", "",
				 fields=[{"value":"You waited too long to finish your request, please try again", "name":"____________"}], avatar=False))

	@client.event
	async def on_reaction_add(reaction, user):
		global userInputMode
		global category
		global TimeoutTime

		# if the user is the bot
		if (user == client.user):
			return
		# if the emoji is "eyes" it'll grab the description of the embed (the user id of the message the reaction is attached to,
		# this is done by grabbing the description of the embed, removing everything except the id, then turning it into an integer and using that to get the user)
		# which it will then send a message to
		if (reaction.emoji == eyes):
			await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if c in digits))
			).send(embed = await embed(message.author, "Update!", "",
		 fields=[{"value":"Your message has been seen by a staff member, they will dm you shortly", "name":"____________"}], avatar=False))
			await reaction.message.clear_reaction(eyes) #makes it so that the staff cant send multiple "seen" messages 

		if (reaction.emoji == redCross):
			await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if c in digits))
			).send(embed = await embed(message.author, "Update!", "",
		 fields=[{"value":"Your ticket has been closed by a staff member, have a good day!", "name":"____________"}], avatar=False))
			await reaction.message.clear_reaction(redCross)
		
		if (reaction.emoji == noEntrySign):
			if not (await AsyncDataBase.read("Blacklist", [message.id])):
				await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if c in digits))).send(embed = 
				await embed(message.author, "Blacklisted", "",
			fields=[{"value":"You have been banned from using this bot, don't waste your time", 
			"name":"____________"}], avatar=False))
				await reaction.message.clear_reaction(redCross)
				USER_ID = int(''.join(c for c in reaction.message.embeds[0].description if c in digits))
				await AsyncDataBase.addEntry("Blacklist", [USER_ID])
			
		# if the channel is not a dm, return
		if not isinstance(message.channel, discord.channel.DMChannel):
			return
		
		# when a message has the "tick" emoji added
		if (reaction.emoji == tick):
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Categories", "", 
				fields=[{"value":"What category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other", 
				"name":"____________"}], avatar=False))
			await msg.add_reaction(one) #add the reactions to the bot so that the user can select a bot
			await msg.add_reaction(two)
			await msg.add_reaction(three)
			await msg.add_reaction(four)
			
		# when a message has the "one" emoji added
		elif (reaction.emoji == one):
			userInputMode = True
			TimeoutTime = datetime.datetime.now() + datetime.timedelta(hours = 1) 
			category = 1
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))

			
		# when a message has the "two" emoji added		
		elif (reaction.emoji == two):
			userInputMode = True
			TimeoutTime = datetime.datetime.now() + datetime.timedelta(hours = 1) 
			category = 2
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			
		# when a message has the "three" emoji added
		elif (reaction.emoji == three):
			userInputMode = True
			TimeoutTime = datetime.datetime.now() + datetime.timedelta(hours = 1)
			category = 3
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
				
		# when a message has the "four" emoji added
		elif (reaction.emoji == four):
			userInputMode = True
			TimeoutTime = datetime.datetime.now() + datetime.timedelta(hours = 1)
			category = 4
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			


@client.event
async def on_member_join(member):
	guild = client.get_guild(179077200149086209)
	channel = guild.get_channel(179077200149086209)
	await channel.send("Hi <@{}>, welcome to Aus SEA Brawlhalla! Please checkout <#{}> and go <#{}>, enjoy your stay!\n<:{}:{}>".format(
		member.id, 231799301410390017, 455290609800839178, "AusSEAWave", 752031381613183028))


if __name__ == "__main__":
	client.run(Token.token())
