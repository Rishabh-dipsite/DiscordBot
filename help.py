async def readHelp(message):
    print("Message read " + message.content)
    textMsg = 'Following are list of valid routines:\n'

    await message.channel.send(getHelp(textMsg))

def printHelp():
    print("message from another file")

def getHelp(textMsg):
    textMsg += "1. One\n"
    textMsg += "2. Two\n"
    textMsg += "3. Three"
    return textMsg