from modules.core import utils

import discord
from discord.ext import commands


class Empty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    # cogs = {Empty}
    cogs = {}
    utils.modules.addCogs(bot, cogs)
