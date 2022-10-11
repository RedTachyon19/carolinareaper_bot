#Libraries this program needs
import discord

from discord.ext import commands

import os
import keep_alive
import music


bot = commands.Bot(command_prefix= "!c ", intents = discord.Intents.all())

bot.remove_command('help')

cogs = [music]
for i in range (len(cogs)):
  cogs[i].setup(bot)


keep_alive.keep_alive()
carolinareaper_token = os.environ['carolinareaper_token']
bot.run(carolinareaper_token)
