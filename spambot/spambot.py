import discord
client=discord.Client()

key1="NzU5NzY2MTI0NDI1Mzc5ODUw.X3CRVw."
key2="yD4b3RWYYjDORbYJpNtZhBHwUYQ"
@client.event
async def on_message(message):
    mes=message.content
    if message.author.bot == False:
        if len(message.content)==6:
            for j in range(5):
                await message.channel.send(mes.upper())


client.run(key1+key2)
