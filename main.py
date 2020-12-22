import discord
import crudLib
import pymongo
import tokenlib

client = discord.Client()

def loadMem():
    for guild in client.guilds:
        for member in guild.members:
            yield member
def memInDB(username):
    exist = False
    user = crudLib.getUsername(username)
    if user == None:
        exist = False
    else:
        exist = True
    return exist

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="All The Users"))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user = message.author.name + message.author.discriminator
    
    print(user)
    if memInDB(user):
        messageCount = crudLib.getMessCount(user)
        messageCount = messageCount + 1
        print(messageCount)
        crudLib.setMessCount(user, messageCount)
    else:
        crudLib.addUser(user)
        crudLib.setMessCount(user, 1)
    #if message.content.startswith('hello'):
     #   await message.channel.send('Hello!')

client.run(tokenlib.bottoken)
