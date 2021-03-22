
from embed import embed
import datetime
from textwrap import wrap
import AsyncDataBase, reset
eyes = u"\U0001F440"
noEntrySign = u"\U0001F6AB"
redCross = 	u"\u274C"
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
        if len(userMessage) == 200:
            return True
        channel = guild.get_channel(categoryIds[category]) #gets the proper channel it should be sending to
        if await AsyncDataBase.read("ModCategory", message.author.id) == 1:
            msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
            message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'\n\n<@&713704594718457897> - Harassment\n"{}"'.format(userMessage), 
            "name":"Message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
            "name":"Reactions"}]))
        elif await AsyncDataBase.read("ModCategory", message.author.id) == 2:
            msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
            message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'\n\n<@&742691006943854682> - NSFW\n"{}"'.format(userMessage), 
            "name":"Message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
            "name":"Reactions"}]))
        elif await AsyncDataBase.read("ModCategory", message.author.id) == 3:
            msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
            message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'\n\n<@&742691006943854682> - Spam\n"{}"'.format(userMessage), 
            "name":"Message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
            "name":"Reactions"}]))
        elif await AsyncDataBase.read("ModCategory", message.author.id) == 4:
            msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
            message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'\n\n<@&742691006943854682> - Scamming/Selling Codes\n"{}"'.format(userMessage), 
            "name":"Message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
            "name":"Reactions"}]))
        else:
            msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
                message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'"{}"'.format(userMessage), 
                "name":"message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
                "name":"Reactions"}])) #creates a embed (with multiple dicts in the field arg to create multiple text fields)
        await msg.add_reaction(eyes) #add reactions
        await msg.add_reaction(redCross)
        await msg.add_reaction(noEntrySign)
        await message.channel.send(embed = await embed(message.author, "Submitted", "",
            fields=[{"value":"Your message has been sent to the Aus Sea staff, they will help you shortly", "name":"____________"}], avatar=False)) #sends message to the user informing them their message has been sent
        await reset.reset(message.author)
        return