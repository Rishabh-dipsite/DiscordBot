import discord
import help

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

client.run('NzY1NDg2NTM1MTUxNDUyMTkx.X4Vg5A.A8KyisV8ug0S4ReR4_jt8VB1eDc')