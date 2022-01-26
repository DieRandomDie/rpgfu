from functions import cls, checkfile, time_text
import discord
import asyncio
from discord.ext import commands, tasks
import time
import json


client = commands.Bot(command_prefix='!')
client.tick = 0
client.seconds = 0
channel_id = 934490823100366868
if not checkfile("token.dat"):
    with open('token.dat', 'w') as token_data:
        token_data.write(input("Bot token: "))
with open('token.dat') as token_data:
    token = token_data.readline()
    print('Token fetched')
    print('Connecting...')


@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    await channel.send("Hello world!")


@client.command()
async def tick(ctx):
    channel = client.get_channel(channel_id)
    await channel.send("Current tick {t}".format(t=client.tick))


@tasks.loop(seconds=1)
async def ticker():
    await client.wait_until_ready()
    client.seconds += 1
    cls()
    if client.seconds % 6 == 0:
        client.tick += 1
    print('Time elapsed: ' + time_text(client.seconds))
    print('Current Tick: {}'.format(client.tick))


ticker.start()
client.run(token)

