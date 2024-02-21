import discord
import users as users
import youtube_dl
from discord.ext import commands
import os
from discord import game
import json
import time
import websockets

client = commands.Bot(command_prefix="!")
client.remove_command('help')
player_dict = dict()
players = {}





#Events#
#@client.event
#async def on_message(message):
    #if message.content.lower().startswith('!clear'):
        #if "<@&400341342267637762>" in [role.id for role in
                           #message.author.roles]:
            #async def clear(ctx, amout=100):
                #channel = ctx.message.channel
                #messages = []
                #async for message in client.logs_from(channel, limit=int(amout) + 1):
                    #messages.append(message)
                #await client.delete_messages(messages)
                #await client.say('Beweise Vernichtet')
        #else:
                #await client.send_message(message.channel, "You dont have the Permissions to do this")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='mit der Matrix'))
    print("Bot ist Online")

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='User')
    await client.add_roles(member, role)

#help
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.gold()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!join', value='Joint dem Channel des Befehls schreiber', inline=False)
    embed.add_field(name='!leave', value='Leaved dem Channel des Befehls schreiber', inline=False)
    embed.add_field(name='!twitter', value='Twitter Kanal von Sakreton', inline=False)
    embed.add_field(name='!twitch', value='Twitch Kanal von Sakreton', inline=False)
    embed.add_field(name='!clear', value='Cleart den Channel nur (Admins und Mods)', inline=False)
    embed.add_field(name='!play', value='Spielt Musik ab (Youtube Link nicht vergessen)', inline=False)
    embed.add_field(name='!stop', value='Stoppt das Lied', inline=False)
    embed.add_field(name='!pause', value='Pausiert das Lied', inline=False)
    embed.add_field(name='!resume', value='Setzt das Lied fort', inline=False)
    embed.add_field(name='!nacht', value='Sagt Gute Nacht', inline=False)
    embed.add_field(name='!bruder', value='Nasenbluten', inline=False)
    embed.add_field(name='!fortnite', value='FÜR FORTNITE', inline=False)
    embed.add_field(name='!ehre', value='Ehre genommen', inline=False)
    embed.add_field(name='!nero', value='Mein Erschaffer', inline=False)
    embed.add_field(name='!spaß', value='Spaß', inline=False)
    await client.send_message(author, embed=embed)
#Commands

@client.command()
async def nacht():
    await client.say('Gute Nacht')

@client.command()
async def nero():
    await client.say('test')

@client.command()
async def spaß():
    await client.say('Ich bin Bruno und ich bin der Kamera Mann')


@client.command()
async def ehre():
    await client.say('Ehre genommen')

@client.command()
async def bruder():
    await client.say('Muss los')

@client.command()
async def fortnite():
    await client.say('Für Fortnite')

@client.command()
async def twitter():
    await client.say('https://twitter.com/DerNephren')

@client.command()
async def twitch():
    await client.say('https://www.twitch.tv/DerNephren')

@client.command(pass_context=True)
async def clear(ctx, amout=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amout) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Beweise Vernichtet')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
#Musikbot
@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

client.run("")