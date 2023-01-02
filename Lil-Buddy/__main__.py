import os, asyncio
from dotenv import load_dotenv
import json

import discord
from discord.ext import commands

from common import *
from database import *

#The bot
lilbuddy = commands.Bot(command_prefix = 'lb.', intents = discord.Intents().all())


@lilbuddy.event
async def on_ready():
	""" Detects when the bot has been fully loaded and is online """
	print("Bot ready!")

@lilbuddy.command()
async def load(ctx, cog):
	pass

@lilbuddy.command()
async def unload(ctx, cog):
	pass

		
@lilbuddy.command()
async def ping(ctx):
	await ctx.send(f"Pong!\nLatency: **{round(lilbuddy.latency * 1000)}ms**")

async def setup():
	
	for filename in os.listdir(f"{pwdir}/Cogs"):
		if filename.endswith(".py"):
			await lilbuddy.load_extension(f"Cogs.{filename[:-3]}")

def main():
	
	load_dotenv()
	token = os.getenv('TOKEN')
	
	lilbuddy.run(token)

if __name__ == "__main__":
	asyncio.run(setup())
	main()
