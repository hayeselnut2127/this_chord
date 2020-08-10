import discord
import config

TOKEN = config.DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$h'):
        await message.channel.send('Hello!')

client.run(TOKEN)