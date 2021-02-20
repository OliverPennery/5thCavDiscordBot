import os
import glob
import sys
import time
import subprocess

import discord
from discord.ext import commands
from modules.core import utils
from modules.core import logger

# log = logging.getLogger('discord')
# log.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# log.addHandler(handler)

TOKEN = os.environ.get('DISCORD_TOKEN')

#intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.log(f'{bot.user}, ready to serve {len(bot.users)} users in {len(bot.guilds)} servers', "ready")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'modules.{extension}')
    logger.log(f'load {extension}', "log")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'modules.{extension}')
    logger.log(f'unload {extension}', "log")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'modules.{extension}')
    logger.log(f'reload {extension}', "log")

def main():
    utils.modules.loadCogs(bot)
    try:
        bot.run(TOKEN)
    except(KeyboardInterrupt):
        sys.exit("Bot Terminated (KeyboardInterrupt)")


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        print("[DiscordBot] Interrupted")

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
#         print(f'{message.author} : {message.guild}')


