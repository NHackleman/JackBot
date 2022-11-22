import discord
from dotenv import dotenv_values

token = dotenv_values('.env')["TOKEN"]

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)
