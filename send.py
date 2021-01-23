
from embed import embed
import datetime
from textwrap import wrap
import AsyncDataBase
from reset import reset
eyes = u"\U0001F440"
noEntrySign = u"\U0001F6AB"
redCross = 	u"\u274C"
async def Send(client, categoryIds, message):
    guild = client.get_guild(713704403567378473) #get the staff guild
    userMessage = await AsyncDataBase.read("User_Messages", 786320320276856872)
    userMessage = userMessage[0][1]
    category = await AsyncDataBase.read("Category", 786320320276856872)
    _ = wrap(userMessage, 1)
    x = ""
    for i in _:
        x = x + i + "\n"
    if category != 0:
        channel = guild.get_channel(categoryIds[category[0][1]]) #gets the proper channel it should be sending to
        msg = await channel.send(embed=await embed(message.author,"{}#{}".format(message.author.name, 
            message.author.discriminator),"<@{}>".format(message.author.id),fields=[{"value":'"{}"'.format(userMessage), 
            "name":"message"}, {"value":"Use the eyes to show the user that their message has been seen\n\nUse the red cross to mark the request as closed\n\nUse the 'no entry sign' emoji to blacklist the user", 
            "name":"Reactions"}])) #creates a embed (with multiple dicts in the field arg to create multiple text fields)
        await msg.add_reaction(eyes) #add reactions
        await msg.add_reaction(redCross)
        await msg.add_reaction(noEntrySign)
        await message.channel.send(embed = await embed(message.author, "Submitted", "",
            fields=[{"value":"Your message has been sent to the Aus Sea staff, they will help you shortly", "name":"____________"}], avatar=False)) #sends message to the user informing them their message has been sent
        await AsyncDataBase.remove("User_Messages", 786320320276856872) #resets the variables
        await reset(message.author)