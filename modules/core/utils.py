import os
import glob

import discord
from discord.ext import commands

import logging
from logging.handlers import RotatingFileHandler

from modules.core import logger

# _log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
# _logFile = os.path.dirname(os.path.realpath(__file__))+"/root.log"
# _my_handler = RotatingFileHandler(_logFile, mode='a', maxBytes=10*1000000, backupCount=10, encoding=None, delay=0)
# _my_handler.setFormatter(_log_formatter)
# _my_handler.setLevel(logging.INFO)
# log = logging.getLogger('root')
# log.setLevel(logging.INFO)
# log.addHandler(_my_handler)

class modules():
    def loadCogs(bot):
        for module in glob.glob("modules/*/module.py"):
            module = module.replace("\\", ".").replace("/", ".")
            try:
                bot.load_extension(module[:-3])
                logger.log(f'Loading Module {module}')
            except (discord.ext.commands.ExtensionNotFound, ModuleNotFoundError):
                logger.log(f'Failed to load module: {module}', "error")

    def addCogs(bot, cogs):
        for cog in cogs:
            try:
                bot.add_cog(cog(bot))
                logger.log(f'Loading cog: {cog.__name__}')
            except (TypeError, AttributeError):
                try:
                    logger.log(f'Failed to load cog: {cog.__name__}', "error")
                except AttributeError:
                    logger.log(f'Failed to load cog: {cog}', "error")