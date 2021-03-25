
from embed import embed
import datetime
from textwrap import wrap
import AsyncDataBase, reset
eyes = u"\U0001F440"
noEntrySign = u"\U0001F6AB"
redCross = 	u"\u274C"

async def reaction_confirm(msg, message):
    await msg.add_reaction(eyes) #add reactions
    await msg.add_reaction(redCross)
    await msg.add_reaction(noEntrySign)
    await message.channel.send(embed = await embed(message.author, "Submitted", "",
        fields=[{"value":"Your message has been sent to the Aus Sea staff, they will help you shortly", "name":"____________"}], avatar=False)) #sends message to the user informing them their message has been sent
    await reset.reset(message.author)

async def Send(client, category, categoryIds, message, time):
    
    guild = client.get_guild(713704403567378473) #get the staff guild
    userMessage = ""

    async for m in message.channel.history(after=time, oldest_first=True):
        if m != message:
            if m.author != client.user:
                userMessage = "{} {}".format(userMessage, m.content)

    userMessage[2:]
    category = await AsyncDataBase.read("Category", message.author.id)


    if category != 0:
        if len (userMessage) == 0:
            msg = await message.channel.send(embed=await embed(message.author, "Categories", "", 
				fields=[{"value":"Too few characters. I guess you got no issue then", 
				"name":"____________"}], avatar=False))
            await reset.reset(message.author)
            return
        if len(userMessage) >= 1024:
            msg = await message.channel.send(embed=await embed(message.author, "Categories", "", 
				fields=[{"value":"Too many characters. Try not to send too much information with the first message, staff will follow up and ask for more information if necessary", 
				"name":"____________"}], avatar=False))
            await reset.reset(message.author)
            return
        channel = guild.get_channel(categoryIds[category]) #gets the proper channel it should be sending to
        msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
                message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'"{}"'.format(userMessage), 
                "name":"Message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
                "name":"Reactions"}]))
        await reaction_confirm(msg, message)
        if await AsyncDataBase.read("ModCategory", message.author.id) != None and category == 1:
            if await AsyncDataBase.read("ModCategory", message.author.id) == 1:
                await channel.send("<@&713704594718457897> - Harassment")
                return

            elif await AsyncDataBase.read("ModCategory", message.author.id) == 2:
                await channel.send("<@&742691006943854682> - NSFW")
                return

            elif await AsyncDataBase.read("ModCategory", message.author.id) == 3:
                await channel.send("<@&742691006943854682> - Spam")
                return

            elif await AsyncDataBase.read("ModCategory", message.author.id) == 4:
                await channel.send("<@&742691006943854682> - Scamming/Selling Codes")
                return     

            elif await AsyncDataBase.read("ModCategory", message.author.id) == 5:
                await channel.send("<@&742691006943854682> - Boosting")
                return

            elif await AsyncDataBase.read("ModCategory", message.author.id) == 6:
                await channel.send("<@&713704594718457897> - Submitting Appeal")
                return
        
        if category == 2:
            await channel.send("<@&742691076443471944> - Tournament Help")
            return
        
        if category == 3:
            # if user selects they had a problem with a mentor it will return 1 anything else is a glitch
            if await AsyncDataBase.read("mentorSelect", message.author.id) == 1:
                await channel.send("<@&742691913169109003> - Problem with mentor")
            else:
                return
        
        if category == 4:
            return