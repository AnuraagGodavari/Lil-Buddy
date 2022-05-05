import json

import discord
from discord.ext import commands

from common import *


#Utility functions

def get_watchStatuses(): 
	with open(watch_statuses_file) as f: return json.load(f)

def save_watchStatuses(new_watchStatuses): 
	with open(watch_statuses_file, 'w') as f: json.dump(new_watchStatuses, f, indent = 4) 

def can_singleTrigger(user):
	"""
	Get @everyone role with id tracked in watch_statuses as 'singleEventTrigger_id'. 
	This id is unique to every server, so this should only return True once per user no matter how many servers they share with LilBuddy.

	Args:
		user (Member): the person to check if we can singleTrigger.
	"""

	watch_statuses = get_watchStatuses()

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

	if not newActivity: return False

	watch_statuses = get_watchStatuses()

	if str(user.id) in watch_statuses.keys():

		#If newActivity is different from both oldActivity and the last saved status
		if ((oldActivity != newActivity) and (watch_statuses[str(user.id)]["lastStatus"] != newActivity)): 

			watch_statuses[str(user.id)]["lastStatus"] = newActivity
			save_watchStatuses(watch_statuses)

			return watch_statuses[str(user.id)]["channel"]

	return False


#The cog itself

class WatchStatus(commands.Cog):
	""" A cog that allows its client bot to watch member statuses """
	
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		"""
		Checks if a member has changed their profile.

		Args:
			before (Member): the member's old info
			after (Member): the member's new info
		"""

		#If we can't trigger an event this user object, end function here
		if not can_singleTrigger(after): return
		if not (after.activity): return

		statusChannel_id = watchingForStatus(before, str(before.activity), str(after.activity))

		if (statusChannel_id):
			statusChannel = self.client.get_channel(statusChannel_id)
			await statusChannel.send(f"> {after.activity}")
			
	@commands.command()
	async def ping_WatchStatus(self, ctx):
		await ctx.send(f"Pong_WatchStatus!\nLatency: **{round(self.client.latency * 1000)}ms**")
		
def setup(client):
	client.add_cog(WatchStatus(client))