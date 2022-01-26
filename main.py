from os import path
import discord
import asyncio
from discord.ext import commands, tasks
import time
import json


client = commands.Bot(command_prefix='!')
client.tick = 0
channel_id = 934490823100366868
if not path.exists("token.dat"):
    with open('token.dat', 'w') as token_data:
        token_data.write(input("Bot token: "))
with open('token.dat') as token_data:
    token = token_data.readline()
    print('Token fetched')
    print('Connecting...')


@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    print(channel)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await channel.send("Hello world!")


@client.command()
async def tick(ctx):
    channel = client.get_channel(channel_id)
    await channel.send("Current tick {t}".format(t=client.tick))


@tasks.loop(seconds=6)
async def ticker():
    await client.wait_until_ready()
    client.tick += 1


ticker.start()
client.run(token)

