import discord, AsyncDataBase, reaction_code, message_code, randomstatus, Token #imports
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc
from string import digits
from discord.ext import commands

client = commands.Bot(command_prefix = "&", self_bot=False, intents=discord.Intents.all()) #initializing client
activity = discord.Activity(name=randomstatus.randomstatus(), type=discord.ActivityType.watching)
scheduler = AsyncIOScheduler(timezone=utc)

async def offline_mode_on():
	activity = discord.Activity(name="Mod Mail Is Offline", type=discord.ActivityType.watching)
	await AsyncDataBase.update("Offline", 1, BOOL=True)
	await client.change_presence(activity=activity)


async def offline_mode_off():
	activity = discord.Activity(name="Mod Mail Is Online", type=discord.ActivityType.watching)
	await AsyncDataBase.update("Offline", 1, BOOL=False)
	await client.change_presence(activity=activity)


# this is used to print out in terminal when the bot is ready
@client.event
async def on_ready():
	print("{} is ready".format(client.user))
	await AsyncDataBase.removeall()
	await AsyncDataBase.create()
	await AsyncDataBase.addEntry("Offline", 1, BOOL=False)
	await client.change_presence(activity=activity)
	scheduler.add_job(offline_mode_on, "cron", hour="11", minute="30")
	scheduler.add_job(offline_mode_off, "cron", hour="14")
	scheduler.start()


@client.event #decorating this function as an event
async def on_message(message):
	await message_code.on_message(message, client)


@client.event
async def on_reaction_add(reaction, user):
	await reaction_code.on_react(reaction, user, client)


@client.event
async def on_member_join(member):
	guild = client.get_guild(179077200149086209)
	channel = guild.get_channel(179077200149086209)
	await channel.send("Hi <@{}>, welcome to Aus SEA Brawlhalla! Please checkout <#{}> and go <#{}>, enjoy your stay!\n<:{}:{}>".format(
		member.id, 231799301410390017, 455290609800839178, "AusSEAWave", 752031381613183028))


if __name__ == "__main__":
	client.run(Token.token())