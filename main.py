#Libraries this program needs
import discord

from discord.ext import commands

#from discord_slash import SlashCommand, SlashContext
#from discord_slash.utils.manage_commands import create_choice, create_option

import keep_alive
import music
import os


bot = commands.Bot(command_prefix= "!c ", intents = discord.Intents.all())

#slash = SlashCommand(bot, sync_commands = True)
bot.remove_command('help')

cogs = [music]
for i in range (len(cogs)):
  cogs[i].setup(bot)


keep_alive.keep_alive()
carolinareaper_token = os.environ['carolinareaper_token']
bot.run(carolinareaper_token)