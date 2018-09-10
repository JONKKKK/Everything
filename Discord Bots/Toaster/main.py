import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-ping'):
        await client.send_message(message.channel, content = 'Pong!')

with open('C:/Users/matth/Desktop/Everything/token.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
