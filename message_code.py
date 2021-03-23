import discord, AsyncDataBase, embed, Blacklist, Unblacklist, datetime, reset, send
tick = "✅"
time = None
category = 0
categoryIds = {1:750590527249973369, 2:750590465149239346, 3:750590556777873429, 4:750613194875076618}


async def on_message(message, client):
	global time
	if message.author == client.user:
		return


	elif not isinstance(message.channel, discord.channel.DMChannel):
		try:
			if message.content.split()[0].lower() == "&blacklist":
				await Blacklist.Blacklist(message)
			elif message.content.split()[0].lower() == "&unblacklist":
				await Unblacklist.Unblacklist(message)
		except:
			return
		return


	elif (await AsyncDataBase.read("Blacklist", message.author.id)):
		return


	elif (await AsyncDataBase.read("Offline", 1)) == 1 or (await AsyncDataBase.read("Offline", 1)) == True:
		msg = await message.channel.send(embed = await embed.embed(message.author, "Hey!", "", fields=
				[{"value":"Hi there! The mod mail functions are temporarily disabled in order to make sure our staff get a bit of a break. Message us back in {} hours and we'll help you out then!".format("?"), "name":"____________"}],
				avatar=False))
		return

	# if its the cancel command reset the bots state
	elif ("&cancel" == message.content.lower()):
		await reset.reset(message.author)
	
	#if the message variable is not the bot
	elif (await AsyncDataBase.read("UserInputMode", message.author.id) != 1):
		if (datetime.datetime.utcnow() - message.author.created_at) > datetime.timedelta(days=7):
			msg = await message.channel.send(embed = await embed.embed(message.author, "Hey!", "", fields=
				[{"value":"Hi there! If you need some help, please react to this message so we can get started.\nYou can cancel at any time with &cancel", "name":"____________"}],
				avatar=False)) #sends back the same message (for now, it'll send a helpful response message soon)
			await msg.add_reaction(tick)
			time = msg.created_at
		else:
			msg = await message.channel.send(embed = await embed.embed(message.author, "Hey!", "", fields=
				[{"value":"Hi there! I see your account is less then 1 week old. Try again in a little bit", "name":"____________"}],
				avatar=False)) #sends back the same message (for now, it'll send a helpful response message soon)

	# join the messages and add a newline between them
	elif (await AsyncDataBase.read("UserInputMode", message.author.id) == 1):
		# if its the send command the get the server, remove the \n that was left at the end from the conjoining of all the users messages and embed/send it
		if message.content.lower() == "&send":
			await send.Send(client, category, categoryIds, message, time)
			return

		#run for every object in the message.channel.history dataset (with that pulling from the last two messages, 
		# the first of which will always be the message just sent by the user)
		async for m in message.channel.history(limit=2):
			if m != message:
				if not round((datetime.datetime.utcnow()-m.created_at).total_seconds()/60) > 10: #round the timedelta between the current utc time and the time of the last sent message to minutes
					return

				else: #else runs this code
					userInputMode = False #resets the variables
					await message.channel.send(embed = await embed.embed(message.author, "Timeout", "",
						fields=[{"value":"You waited too long to finish your request, please try again", "name":"____________"}], avatar=False))
					await reset.reset(message.author)