# main.py - https://discord.com/api/oauth2/authorize?client_id=1207681524980383754&permissions=377957137408&scope=bot
import os

import discord
from discord.ext import commands

import NLGlite.NLGlite

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

AI_TOKEN = os.getenv('OPEN_API_KEY')

model = NLGlite.NLGlite.NLGlite_()


@bot.event
async def on_ready():
    global model

    model.set_config_file_path(
        "C:/Users/Danbo/Documents/UoN_CompSci/Year "
        "3/COMP3003/Project/NLGlite/src/data/config/books/crimeandpunishment.lcfg")
    print(f'Connecting to discord: \t{bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    request_string = "[" + message.author.name + "]" + ":[" + message.content + "]"
    print(f'Received message: \t\t\"{request_string}\"')
    new_message = model.generate_sentences(1, False)
    if new_message != "":
        await message.channel.send(new_message)
    else:
        print(f'Error: \t\t\tReturn string is empty')


@bot.command()
async def usage(ctx):
    await ctx.send("Commands: \n"
                   "$usage       -> Display usage"
                   "$roll {size} -> Rolls a dice of specified size. Only rolls allowed dice.\n"
                   "\n"
                   "Chatting to the Bot: \n"
                   "Simply respond to the bot prompts as you would a regular DM")


bot.run(TOKEN)
