import discord
from discord.ext import commands
import asyncio

from ifunnyscraper import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix='-', intents=intents)

@client.event
async def on_ready():
    print("Ready for theft!")

@client.command()
async def end(ctx):
    await ctx.send("I am shutting down.")
    await client.close()

@client.command()
async def stopstealing(ctx):
    client.loop.close()
        

@client.command()
async def stealmemes(ctx):
    url = "https://ifunny.co/"
    session = setWebdriver(url)
    
    client.loop.create_task(getLink(ctx, session))

    
async def getLink(ctx, session):
    previousLink = "placeholder"
    link = "placeholder2"
    while True:
        session.refresh()
        
        if link != "Empty":
            link = soupSearch(session.page_source)
            if previousLink != link:
                await ctx.send(link)
                previousLink = link
            
        await asyncio.sleep(300)  

client.run('TOKEN')

# TODO:
# improve webscraping, needs to account for all img/vids
# implement selenium automatic login