import discord
from dotenv import dotenv_values
import requests
import json

token = dotenv_values('.env')["TOKEN"]

client = discord.Client(intents=discord.Intents.all())

# Get Omaha weather data
def get_weather():
    response = requests.get(
        "https://api.weather.gov/gridpoints/OAX/80,47/forecast")
    json_data = json.loads(response.text)
    weather = str(json_data["properties"]["periods"][0]["temperature"]) + \
        "°F\n" + str(json_data["properties"]["periods"][0]["detailedForecast"])

    return (weather)


# On Ready
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

# Message Commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Welcome message
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    # Get weather
    elif message.content.startswith('$weather'):
        weather = get_weather()
        await message.channel.send(weather)


client.run(token)
