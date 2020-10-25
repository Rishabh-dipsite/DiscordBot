import discord
import help
import env

client = discord.Client()
emb = discord.Embed()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    help.printHelp()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        emb.clear_fields()
        # creating embed
        emb.title='Welcome Tile'
        emb.description='hello {0}, welcome to {1}.'.format(message.author.mention, message.guild)
        emb.colour= discord.colour.Color(0x0011FF)
        helpString = help.getHelp('')
        emb.add_field(name='Help Menu',value='#Following are the menu:\n {0}'.format(helpString))

        await message.channel.send(embed=emb)

    if message.content.startswith('$help'):
        emb.title='Help Tile'
        await help.readHelp(message)
    
client.run(env.token)