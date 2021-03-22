import discord, AsyncDataBase, embed, Blacklist
tick = "✅"
one = "1⃣"
two = "2⃣"
three ="3⃣"
four = "4⃣"
time = None
eyes = u"\U0001F440"
noEntrySign = u"\U0001F6AB"
redCross = 	u"\u274C"
def check(c):
	try:
		int(c)
		return True
	except ValueError:
		return False
#this is to make sure the user cant add a second reaction and screw the bot over, it'll be called after the user chooses a reaction
async def clear_react(message, client):#function to reset reactions
	lis = [one, two, three, four]
	for i in lis:
		await message.remove_reaction(i, client.user) #cant remove all due to not being able to remove the users

async def on_reaction(reaction, user, client):
# if the user is the bot
		if (user == client.user):
			return
		# if the emoji is "eyes" it'll grab the description of the embed (the user id of the message the reaction is attached to,
		# this is done by grabbing the description of the embed, removing everything except the id, then turning it into an integer and using that to get the user)
		# which it will then send a message to
		if (reaction.emoji == eyes):
			await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if check(c)))
			).send(embed = await embed.embed(reaction.message.author, "Update!", "",
			fields=[{"value":"Your message has been seen by <@{}>, they will dm you shortly".format(user.id), "name":"____________"}], avatar=False))
			await reaction.message.clear_reaction(eyes) #makes it so that the staff cant send multiple "seen" messages 

		if (reaction.emoji == redCross):
			await client.get_user(int(
				''.join(c for c in reaction.message.embeds[0].description if check(c)))
			).send(embed = await embed.embed(reaction.message.author, "Update!", "",
			fields=[{"value":"Your ticket has been closed by a staff member, hope we helped!", "name":"____________"}], avatar=False))
			await reaction.message.clear_reaction(redCross)
		
		if (reaction.emoji == noEntrySign):
			if not (await AsyncDataBase.read("Blacklist", reaction.message.id)):
				await Blacklist.Blacklist(reaction.message, client, int(''.join(c for c in reaction.message.embeds[0].description if check(c))))
				await reaction.message.clear_reaction(noEntrySign)
			USER_ID = int(''.join(c for c in reaction.message.embeds[0].description if check(c)))
			await AsyncDataBase.addEntry("Blacklist", USER_ID)
		# if the channel is not a dm, return
		if not isinstance(reaction.message.channel, discord.channel.DMChannel):
			return
		
		# when a message has the "tick" emoji added
		if (reaction.emoji == tick):
			msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Categories", "", 
				fields=[{"value":"What category would you place your request under?\n\n"+one+" Moderation\n\n"+two+" Tournaments\n\n"+three+" Mentoring\n\n"+four+" Other", 
				"name":"____________"}], avatar=False))
			await msg.add_reaction(one) #add the reactions to the bot so that the user can select a channel
			await msg.add_reaction(two)
			await msg.add_reaction(three)
			await msg.add_reaction(four)
			
		# when a message has the "one" emoji added
		elif (reaction.emoji == one):
			if await AsyncDataBase.read("selectionModMode", user.id):
				await AsyncDataBase.addEntry("ModCategory", user.id, CAT=1)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			else:
				await AsyncDataBase.addEntry("Category", user.id, CAT=1)
				await AsyncDataBase.addEntry("selectionModMode", user.id, BOOL=True)
				await clear_react(reaction.message, client)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "More Info", "", 
				fields=[{"value":"What sort of moderation issue is it? Giving us this information helps us provide better support\n\n"+one+" Harassment\n\n"+two+" NSFW\n\n"+three+" Spam\n\n"+four+" Scamming ", "name":"____________"}], avatar=False))
				await msg.add_reaction(one) #add the reactions to the bot so that the user can select a sub category		
				await msg.add_reaction(two)
				await msg.add_reaction(three)
				await msg.add_reaction(four)

		# when a message has the "two" emoji added		
		elif (reaction.emoji == two):
			if await AsyncDataBase.read("selectionModMode", user.id):
				await AsyncDataBase.addEntry("ModCategory", user.id, CAT=2)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			else:
				await AsyncDataBase.addEntry("Category", user.id, CAT=2)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				await clear_react(reaction.message, client)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
					fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
					"name":"____________"}], avatar=False))
						
		# when a message has the "three" emoji added
		elif (reaction.emoji == three):
			if await AsyncDataBase.read("selectionModMode", user.id):
				await AsyncDataBase.addEntry("ModCategory", user.id, CAT=3)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			else:
				await AsyncDataBase.addEntry("Category", user.id, CAT=3)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				await clear_react(reaction.message, client)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
					fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
					"name":"____________"}], avatar=False))
			
		# when a message has the "three" emoji added
		elif (reaction.emoji == four):
			if await AsyncDataBase.read("selectionModMode", user.id):
				await AsyncDataBase.addEntry("ModCategory", user.id, CAT=4)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
				fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
				"name":"____________"}], avatar=False))
			else:
				await AsyncDataBase.addEntry("Category", user.id, CAT=4)
				await AsyncDataBase.addEntry("UserInputMode", user.id, BOOL=True)
				await clear_react(reaction.message, client)
				msg = await reaction.message.channel.send(embed=await embed.embed(reaction.message.author, "Your Message", "", 
					fields=[{"value":"Please type your message below and use &send to submit your message to the staff", 
					"name":"____________"}], avatar=False))