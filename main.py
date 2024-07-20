import discord
from discord.ext import commands
import random



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')



eco_tips = [
    "Reduce your plastic use by carrying reusable bags.",
    "Save water by taking shorter showers.",
    "Turn off lights when not in use to save energy.",
]


eco_facts = [
    "Recycling one ton of paper saves 17 trees.",
    "The Great Barrier Reef is the world's largest coral reef system.",
    "A single tree can absorb up to 48 pounds of CO2 per year.",
]


eco_challenges = [
    "Avoid using single-use plastics for a week.",
    "Plant a tree in your community.",
    "Reduce your meat consumption for a week.",
]


recycling_guide = {
    "plastic": "Rinse and separate by type. Avoid recycling contaminated plastic.",
    "paper": "Remove staples and paper clips. Flatten and bundle.",
    "glass": "Rinse and sort by color. Do not include broken glass.",
}



eco_news = [
    "New study shows impact of climate change on Arctic ice.",
    "Local community organizes beach cleanup event.",
    "Innovative solutions to reduce ocean plastic pollution.",
]






@bot.command('tip')
async def send_tip(ctx):
    tip = random.choice(eco_tips)
    await ctx.send(tip)


@bot.command('fact')
async def send_fact(ctx):
    fact = random.choice(eco_facts)
    await ctx.send(fact)


@bot.command('challenge')
async def send_challenge(ctx):
    challenge = random.choice(eco_challenges)
    await ctx.send(challenge)


@bot.command('recycle')
async def send_recycling_info(ctx, material: str):
    info = recycling_guide.get(material.lower())
    if info:
        await ctx.send(info)
    else:
        await ctx.send("Sorry, I don't have information on that material.")


@bot.command('news')
async def send_news(ctx):
    news = random.choice(eco_news)
    await ctx.send(news)









bot.run('token')
