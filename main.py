import discord
from discord.ext import commands
from model import get_class
# The intents variable stores the bot's priviliges
intents = discord.Intents.default()
# Enabling the message-reading privelege
intents.message_content = True
# Creating a bot in the client variable and transferring it the priveleges
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Sirvioooooooo, si funciono, me conecté como:  {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hola'):
        await message.channel.send("Holaa mi bro O(∩_∩)O")
    elif message.content.startswith('adios'):
        await message.channel.send("Chaito que te cuides mi broo []~(￣▽￣)~*")
    elif message.content.startswith('¿como estas?'):
        await message.channel.send("pues yo estoy bien, bien gracias por preguntar mi amig@, y tu? （￣︶￣）↗　")
    elif message.content.startswith('yo estoy bien'):
        await message.channel.send("que buenoo, me alegra mi bro, espero que sigas asi (👉ﾟヮﾟ)👉")
    elif message.content.startswith('yo estoy mal'):
        await message.channel.send("ohh.. espero que te mejores pronto mi bro, animos!")
    elif message.content.startswith('¿Cuales son las reglas?'):
        await message.channel.send("CLARO!, aqui te presentamos nuestras reglas de nuestro servidor, espero que no rompas ninguna de ellas colega: No spam, no mandar contenido +18, no insultar a otros")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
          #  await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
            await ctx.send(get_class (model_path="./p.IA", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Olvidaste subir la imagen :(")
    