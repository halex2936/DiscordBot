import logging
from urllib.request import urlopen

import nacl
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

import discord
from discord.ext import commands

soup =""

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

token ='NjE5NTM0MDI3OTg4NDAyMTg4.GIL0Xo.I-Ja8ZpzOhUi674hglUxmCrFQlIzm5lmAK-m0g'
intents = discord.Intents.default()
intents.message_content = True
#the bot subclass is just a more robust client so I named the bot a client.
client = commands.Bot(command_prefix="!", intents = intents)

#To make sure the bot is working / online and the token matches the bot intended for it
'''

@client.event
async def on_ready():
    print(f'We logged in as {client.user}')
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#Youtube_DL is no longer working and no lorger supported
#https://www.youtube.com/results?search_query=song
@client.command(pass_context=True)
async def play(ctx):
    author = ctx.author
    channel = author.voice.channel
    vc = await channel.connect()


    arguments = "https://www.youtube.com/results?search_query="
    sear = ""
    if (len(args) == 0):
        arguments = "INVALID ENTRY"
        soup = arguments
    else:
        if (len(args) > 1):
            sear = "+".join(args)
            arguments += sear
        else:
            if ("https://www.youtube.com/" in args[0] or "https://youtu.be/" in args[0]):
                arguments = args[0]
            else:
                sear = args[0]
                arguments += sear
        soup = BeautifulSoup(urlopen(arguments))
        soup = soup.title.string
    vc.play(discord.FFmpegAudio("https://www.youtube.com/watch?v=ssKWFlclNFg&list=RDscZnl-40IEE"))
    await ctx.send(soup)




client.run(token, log_handler=handler, log_level=logging.DEBUG)