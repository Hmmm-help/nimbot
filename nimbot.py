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
async def average(ctx,*args: float):
    await ctx.send(sum(args)/len(args))

@bot.command(name= "dicebattle")
async def dicebattle(ctx,a:int,b:int,c:int,d:int,e:int,f:int,ai_num:int):
    import random
    score = {"Your_Dice": 0, "Tie": 0, "AI_Dice": 0}
    ai_dice = random.sample(range(ai_num), 6)
    die_a = [a,b,c,d,e,f]
    print(ai_dice,die_a)
    dx = random.choice(die_a)
    dy = random.choice(ai_dice)
    print(f"Your Roll: {dx}| AI Roll: {dy}")
    if dx > dy:
        score["Your_Dice"] += 1
    elif dx < dy:
        score["AI_Dice"] += 1
    elif dy == dx:
        score["Tie"] += 1
    k = max(score.values())
    c = (list(score.keys())[list(score.values()).index(k)])
    if c == "Tie":
        await ctx.send(f"Oh Wow, Its Basically a {c}!")
    else:
        await ctx.send(f"Damn, {c} Wins!")

bot.run(token)


#Aaliyah Garcia
#This took forever, I am tearing up cause I am tired
#Wish I had a taco right now
#Wondering if this will ever get easy
