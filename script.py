import discord
import help
from dotenv import load_dotenv
load_dotenv()
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    help.printHelp()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        message.channel.send('Hello!')

    if message.content.startswith('$help'):
        await help.readHelp(message)

client.run(os.environ.get("token"))