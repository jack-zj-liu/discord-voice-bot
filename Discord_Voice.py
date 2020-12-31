import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

TOKEN = 'NzI0MzY3OTA1MTE4MjI0Mzk3.Xu_Kcg.XnBf68_2cF2USpLjWS2jtZj-zNI'
BOT_PREFIX = '/'

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print("Logged in as: " + client.user.name + '\n')


@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"""The bot has connected to {channel}\n""")

    await ctx.send(f"""Joined {channel}""")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"""the bot has left {channel}""")
        await ctx.send(f"""left {channel}""")
    else:
        print("bot was told to leave this channel, but was not able to")
        await ctx.send("Don't think I am in a voice channel")


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile("songs.np3")


client.run(TOKEN)
