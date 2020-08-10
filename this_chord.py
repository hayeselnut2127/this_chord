import discord

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

client.run("NzQyMzI0NjAzODc5NDI0MDgx.XzEdqQ.db5W2NYmnFm7fhYm-WJ4SQIbWRk")