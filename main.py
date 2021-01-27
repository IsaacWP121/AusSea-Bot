import discord, datetime, AsyncDataBase #imports
from discord.ext import commands
from Blacklist import Blacklist
from Unblacklist import Unblacklist
from string import digits
from embed import embed
from send import Send
from Token import token
from reset import reset

client = commands.Bot(command_prefix = "&", self_bot=False, intents=discord.Intents.all()) #initializing client
activity = discord.Activity(name="Jason get banned", type=discord.ActivityType.watching)

#declarations
tick = "✅"
one = "1⃣"
two = "2⃣"
three ="3⃣"
four = "4⃣"
eyes = u"\U0001F440"
noEntrySign = u"\U0001F6AB"
redCross = 	u"\u274C"
userInputMode = False
category = 0
categoryIds = {1:750590527249973369, 2:750590465149239346, 3:750590556777873429, 4:750613194875076618}


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
	await AsyncDataBase.create()


@client.event #decorating this function as an event
async def on_message(message):
	global userInputMode
	global category

	if message.author == client.user:
		return

	if not isinstance(message.channel, discord.channel.DMChannel):
		try:
			if message.content.split()[0].lower() == "&blacklist":
				await Blacklist(message)
			elif message.content.split()[0].lower() == "&unblacklist":
				await Unblacklist(message)
		except:
			return
		return
	
	if (await AsyncDataBase.read("Blacklist", message.author.id)):
		return
	# if its the cancel command reset the bots state
	if ("&cancel" == message.content.lower()):
		await reset(message.author)
	
	#if the message variable is not the bot
	
	if (await AsyncDataBase.read("UserInputMode", message.author.id) != 1):
		msg = await message.channel.send(embed = await embed(message.author, "Hey!", "", fields=
			[{"value":"Hi there! If you need some help, please react to this message so we can get started.\nYou can cancel at any time with &cancel", "name":"____________"}],
			avatar=False)) #sends back the same message (for now, it'll send a helpful response message soon)
		await msg.add_reaction(tick)

	# join the messages and add a newline between them
	if (await AsyncDataBase.read("UserInputMode", message.author.id) == 1):
		# if its the send command the get the server, remove the \n that was left at the end from the conjoining of all the users messages and embed/send it
		if message.content.lower() == "&send":
			_ = await AsyncDataBase.read("User_Messages", message.author.id)
			await Send(client, category, categoryIds, message)
			return

		#run for every object in the message.channel.history dataset (with that pulling from the last two messages, 
		# the first of which will always be the message just sent by the user)
		async for m in message.channel.history(limit=2):
			if m != message:
				if not round((datetime.datetime.utcnow()-m.created_at).total_seconds()/60) > 10: #round the timedelta between the current utc time and the time of the last sent message to minutes
					# if that is not over 10 min run the code
					_ = await AsyncDataBase.read("User_Messages", message.author.id) 
					if _ == False:
						await AsyncDataBase.addEntry("User_Messages", (message.author.id), Message=message.content)
					else:
						x = "{} {}".format([x for x in _][0], message.content)
						await AsyncDataBase.update("User_Messages", message.author.id, Message=x)
				
				else: #else runs this code
					userInputMode = False #resets the variables
					await message.channel.send(embed = await embed(message.author, "Timeout", "",
						fields=[{"value":"You waited too long to finish your request, please try again", "name":"____________"}], avatar=False))
					await reset(message.author)
@client.event
async def on_reaction_add(reaction, user):
		global userInputMode
		global category
		message = reaction.message

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
			fields=[{"value":"Your message has been seen by <#{}>, they will dm you shortly".format(user.id), "name":"____________"}], avatar=False))
			await reaction.message.clear_reaction(eyes) #makes it so that the staff cant send multiple "seen" messages 

		if (reaction.emoji == redCross):
			await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if c in digits))
			).send(embed = await embed(message.author, "Update!", "",
			fields=[{"value":"Your ticket has been closed by a staff member, have a good day!", "name":"____________"}], avatar=False))
			await reaction.message.clear_reaction(redCross)
		
		if (reaction.emoji == noEntrySign):
			if not (await AsyncDataBase.read("Blacklist", message.id)):
				await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if c in digits))).send(embed = 
				await embed(message.author, "Blacklisted", "",
			fields=[{"value":"I have banned you from using this bot, Ima go get some milk, I'll be back in an hour", 
			"name":"____________"}], avatar=False))
				await reaction.message.clear_reaction(noEntrySign)
			USER_ID = int(''.join(c for c in reaction.message.embeds[0].description if c in digits))
			await AsyncDataBase.addEntry("Blacklist", USER_ID)
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
			await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
			await AsyncDataBase.addEntry("Category", user.id, CAT=1)
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			await AsyncDataBase.addEntry("Category", user.id, CAT=1)
			await clear_react(reaction.message)

		# when a message has the "two" emoji added		
		elif (reaction.emoji == two):
			userInputMode = True
			await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
			await AsyncDataBase.addEntry("Category", user.id, CAT=2)
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			await AsyncDataBase.addEntry("Category", user.id, CAT=2)
			await clear_react(reaction.message)
						
		# when a message has the "three" emoji added
		elif (reaction.emoji == three):
			await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
			await AsyncDataBase.addEntry("Category", user.id, CAT=3)
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			await AsyncDataBase.addEntry("Category", user.id, CAT=3)
			await clear_react(reaction.message)
			
		# when a message has the "three" emoji added
		elif (reaction.emoji == four):
			userInputMode = True
			await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
			await AsyncDataBase.addEntry("Category", user.id, CAT=4)
			await clear_react(reaction.message)
			msg = await reaction.message.channel.send(embed=await embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			await AsyncDataBase.addEntry("Category", user.id, CAT=4)
			await clear_react(reaction.message)

@client.event
async def on_member_join(member):
	guild = client.get_guild(179077200149086209)
	channel = guild.get_channel(179077200149086209)
	await channel.send("Hi <@{}>, welcome to Aus SEA Brawlhalla! Please checkout <#{}> and go <#{}>, enjoy your stay!\n<:{}:{}>".format(
		member.id, 231799301410390017, 455290609800839178, "AusSEAWave", 752031381613183028))

if __name__ == "__main__":
	client.run(token())