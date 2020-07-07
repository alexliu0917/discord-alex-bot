from keys import token
import discord
import re

client = discord.Client() # connect to discord

@client.event
async def on_ready():
    print('{0.user} is up and running'.format(client))

pogFilter = re.compile('pog', re.IGNORECASE)
p_o_gFilter = re.compile('p o g', re.IGNORECASE)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if p_o_gFilter.search(message.content) or message.content.startswith('p og') or message.content.startswith('po g') or pogFilter.search(message.content):
        await message.channel.send('not pog at all')

    if message.content.startswith('prog'):
        await message.channel.send('not prog at all')
    
    for role in message.role_mentions: # respond to certain role mentions
        if role.name == 'Alright, we\'re all here.':
            rollcall = await message.channel.send('Who\'s coming?')
            await rollcall.add_reaction('👍')


client.run(token)