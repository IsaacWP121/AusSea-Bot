import discord
#this allows me to create embeds in 2 lines instead of 4 or 5
async def embed(author, Title, Description, Colour=discord.Colour.blue(), fields=[], avatar=True):
	embed = discord.Embed(colour=discord.Colour.blue(), title=Title, description=Description) #creates the initial embed
	if avatar == True: #if avatars are turned on
		embed.set_thumbnail(url="{}".format(author.avatar_url)) #then add the author's avatar
	for i in fields:
		embed.add_field(name=i["name"], value=i["value"], inline=False) #add the text field below with the values from field
	return embed