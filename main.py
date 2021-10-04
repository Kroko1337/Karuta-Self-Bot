import threading
import time
import discord
from discord.ext import commands
from discord import *

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix=">>>", self_bot=True, intents=intents)
start: bool = True
currentTime: float


async def update(textChannel: TextChannel, prefix: str):
    while True:
        global start
        global currentTime
        if (time.time().real * 1000 - currentTime) >= 1.8e+6 or start:
            start = False
            currentTime = time.time().real * 1000
            await textChannel.send(prefix + "d")
            print("Sending message!")


@bot.event
async def on_ready():
    global start
    global currentTime
    print("Intents:")
    for intent in bot.intents:
        intent: bool = intent
        print(intent)

    print("Bot is ready!")
    print("User ->", bot.user)
    start = True
    currentTime = time.time().real * 1000
    textChannel: TextChannel = await bot.fetch_channel(channelId)
    # thread = threading.Thread(target=await update(textChannel, commandPrefix))
    # thread.run()

    # threading.Thread(target=await check(currentTime, channel, start)).start() <- infinite loop problem


@bot.event
async def on_reaction_add(reaction: Reaction, user: User):
    print("test")
    message: Message = reaction.message
    author: User = message.author
    isBot: bool = author.bot
    reactions: list(Reaction) = message.reactions
    if isBot:
        if len(reactions) == 3 and str(reaction.emoji) == '3️⃣':
            await message.add_reaction(reactions[2])
            print("Reaction added")


@bot.command()
async def info(ctx: discord.ext.commands.Context):
    embed = discord.Embed(title="Karuta Destroyer", description="Version: 1.0.0\nDeveloper: Kroko", color=0x34a8eb)
    textChannel: TextChannel = ctx.channel
    await textChannel.send(embed=embed)
    commandMessage: Message = ctx.message
    await commandMessage.delete()


# ODI0MzM1MzU5OTMyMTA0NzE0.YVoBNA.cxxe0DJ5ipLQ6o7NVjUqYLtu6Uw
# 878089602659926090
# 894312131980300334
token = input("Discord Token:\n")
channelId = input("ChannelID:\n")
commandPrefix = input("Command Prefix:\n")
bot.run(token, bot=False)
