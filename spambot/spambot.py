import discord
client=discord.Client()


@client.event
async def on_message(message):
    mes=message.content
    if message.author.bot == False:
        if len(message.content)==6:
            for j in range(5):
                await message.channel.send(mes.upper())

client.run("NzU5NzY2MTI0NDI1Mzc5ODUw.X3CRVw.6txeRkLLw8uIcmIHSOk5oM3P7qg")
        
