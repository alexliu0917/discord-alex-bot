from keys import token
import discord
import asyncio
import re
import datetime
from alexBotTime import getEorzeaTime, nodeFinder

client = discord.Client() # connect to discord

@client.event
async def on_ready():
    print('{0.user} is up and running'.format(client))

pogFilter = re.compile('po+g', re.IGNORECASE)
p_o_gFilter = re.compile('p o g', re.IGNORECASE)
p0gFilter = re.compile('p0g', re.IGNORECASE)
otherFilter = re.compile('p.*og$', re.IGNORECASE)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if p_o_gFilter.search(message.content) or message.content.startswith('p og') or message.content.startswith('po g') or pogFilter.search(message.content) \
         or p0gFilter.search(message.content) or otherFilter.search(message.content):
        await message.channel.send('not pog at all')
    
    if message.content.startswith('$etime'):
        await message.channel.send('Current Eorzean time is ' + getEorzeaTime())
        await message.channel.send(nodeFinder())
    

    for role in message.role_mentions: # respond to certain role mentions
        if role.name == 'Alright, we\'re all here.':
            rollcall = await message.channel.send('Who\'s coming?')
            await rollcall.add_reaction('👍')

        if role.name == '3':
            rollcall = await message.channel.send('Who\'s coming?')
            await rollcall.add_reaction('👍')
            await asyncio.sleep(5)
            print(rollcall.reactions)


client.run(token)