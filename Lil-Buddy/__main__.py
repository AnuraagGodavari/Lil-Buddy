import json

import discord
from discord.ext import commands

#The bot
lilbuddy = commands.Bot(command_prefix = 'lb.', intents = discord.Intents().all())

#Utility functions
def can_singleTrigger(user):
	"""
	Get @everyone role with id tracked in watch_statuses as 'singleEventTrigger_id'. 
	This id is unique to every server, so this should only return True once per user no matter how many servers they share with LilBuddy.
	
	Args:
		user (Member): the person to check if we can singleTrigger.
	"""
	
	with open("watch_statuses.json") as f:
		watch_statuses = json.load(f)
		
	return next((role for role in user.roles if role.id == watch_statuses[str(user.id)]["singleEventTrigger_id"]), False)

def watchingForStatus(user, oldActivity, newActivity):
	"""
	Checks if we are watching a user and if said user has changed their activity (custom status).
	
	Args:
		user (Member): the user
		oldActivity (str): The activity of the user before the change detected by the bot
		newActivity (str): The activity of the user after the change detected by the bot
	
	Returns:
		A channel ID (int) if we are watching the user and their activity has changed.
		False (bool) if one of the conditions is not met
	"""
	
	with open("watch_statuses.json") as f:
		watch_statuses = json.load(f)
		
	if str(user.id) in watch_statuses.keys():
		
		if ((oldActivity != newActivity) and can_singleTrigger(user)): return watch_statuses[str(user.id)]["channel"]
	
	return False

#Command functions
@lilbuddy.event
async def on_ready():
	"""
	Detects when the bot has been fully loaded and is online
	"""
	
	print("Bot ready!")
	
@lilbuddy.event
async def on_member_update(before, after):
	"""
	Checks if a member has changed their profile.
	
	Args:
		before (Member): the member's old info
		after (Member): the member's new info
	"""
	
	statusChannel_id = watchingForStatus(before, before.activity, after.activity)
	
	if (statusChannel_id and after.activity):
		statusChannel = lilbuddy.get_channel(statusChannel_id)
		await statusChannel.send(f"<@{after.id}> new status:\n> {after.activity}")

def main():
	with open("token.txt", 'r') as tokenF:
		token = tokenF.read()

	lilbuddy.run(token)

if __name__ == "__main__":
	main()