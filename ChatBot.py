import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix="-")
client.remove_command('help')
Client = discord.Client()
player_dict = dict()
players = {}
chat_filter = ["FUCK", "FICK", "STFU", "DEINE MUTTER","BITCH","SCHLAMPE","HURENSOHN"]
bypass_list = ["0"]
TOKEN = ("***")
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Chat Überwachung'))
    print("Der Wächter ist Online")

@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** Bei Fragen, Beschwerden oder Anregungen bitte an einen Mod, Admin oder an den Owner wenden. ")
                except discord.errors.NotFound:
                    return

client.run(TOKEN)
