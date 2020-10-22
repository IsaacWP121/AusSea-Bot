
from embed import embed
import datetime
four = "4⃣"
tick = "✅"
one = "1⃣"
two = "2⃣"
three ="3⃣"
eyes = u"\U0001F440"
noEntrySign = u"\U0001F6AB"
redCross = 	u"\u274C"
async def Send(client, TimeoutTime, userMessage, category, categoryIds, message):
    if datetime.datetime.now() < TimeoutTime:
        guild = client.get_guild(713704403567378473) #get the staff guild
        userMessage = userMessage[:-1] #removes the new line at the end of the message for formatting purposes
        if category != 0:
            channel = guild.get_channel(categoryIds[category]) #gets the proper channel it should be sending to
            msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
				message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'"{}"'.format(userMessage), 
				"name":"message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
				"name":"Reactions"}])) #creates a embed (with multiple dicts in the field arg to create multiple text fields)
            await msg.add_reaction(eyes) #add reactions
            await msg.add_reaction(redCross)
            await msg.add_reaction(noEntrySign)
            await message.channel.send(embed = await embed(message.author, "Submitted", "",
			 fields=[{"value":"Your message has been sent to the Aus Sea staff, they will help you shortly", "name":"____________"}], avatar=False)) #sends message to the user informing them their message has been sent
            userInputMode = False #resets the variables
            category = 0
            userMessage = ""
        else:
            userInputMode = False #resets the variables
            category = 0
            userMessage = ""
            TimeoutTime = None
            await message.channel.send(embed = await embed(message.author, "Timeout", "",
            	 fields=[{"value":"You waited too long to finish your request, please try again", "name":"____________"}], avatar=False))