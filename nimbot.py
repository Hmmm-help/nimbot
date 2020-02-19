import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name= "average")
async def average(ctx,a,b):
    await ctx.send((a+b)/2)
bot.run(token)

#Aaliyah Garcia
#This took forever, I am tearing up cause I am tired
#Wish I had a taco right now
#Wondering if this will ever get easy
