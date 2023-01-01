import json

import discord
from discord.ext import commands

from common import *
from database import *


#The cog itself

class WatchStatus(commands.Cog):
    """ A cog that allows its client bot to watch member statuses """
    
    def __init__(self, client):
        self.client = client

    def get_lastStatus(self, user_id): 
        cursor = getdb().cursor()

        stmt = "SELECT status FROM Statuses WHERE user_id=%s ORDER BY created DESC LIMIT 1;"
        params = [user_id]
        cursor.execute(stmt, params)
        result = cursor.fetchone()

        if (result == None): return False
        return result[0]

    def save_status(self, user_id, new_status): 
        db = getdb()
        cursor = db.cursor()
        
        stmt = "INSERT INTO Statuses (user_id, status) VALUES (%s, %s);"
        params = [user_id, new_status]
        cursor.execute(stmt, params)
        db.commit()

    def checkStatus(self, user, oldActivity, newActivity):
        """
        Checks if we are watching a user and if said user has changed their activity (custom status).

        Args:
            user (Member): the user
            oldActivity (str): The activity of the user before the change detected by the bot
            newActivity (str): The activity of the user after the change detected by the bot

        Returns:
            A discord channel (GuildChannel) if we are watching the user and their activity has changed.
            False (bool) if one of the conditions is not met
        """

        if not newActivity: return False

        #Check if we are watching this user's status
        cursor = getdb().cursor()

        cursor.execute("SELECT status_channel FROM WatchingStatus WHERE user_id=%s LIMIT 1;", [user.id])
        status_channel_id = cursor.fetchone()

        if (status_channel_id == None): return False
        status_channel_id = status_channel_id[0]
        
        #Check if this is the right server
        status_channel = self.client.get_channel(status_channel_id)
        if (user.guild != status_channel.guild):
            return False

        watch_status = self.get_lastStatus(user.id)

        if watch_status:

            #If newActivity is different from both oldActivity and the last saved status
            if ((oldActivity != newActivity) and (watch_status != newActivity)): 
                return status_channel

        return False

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """
        Checks if a member has changed their profile.

        Args:
            before (Member): the member's old info
            after (Member): the member's new info
        """

        if not (after.activity): return

        statusChannel = self.checkStatus(before, str(before.activity), str(after.activity))

        if (statusChannel):
            await statusChannel.send(f"> {after.activity}")
            self.save_status(after.id, str(after.activity))
            
    @commands.command()
    async def ping_WatchStatus(self, ctx):
        await ctx.send(f"Pong_WatchStatus!\nLatency: **{round(self.client.latency * 1000)}ms**")
        
async def setup(client):
    await client.add_cog(WatchStatus(client))