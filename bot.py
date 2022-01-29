from ast import AsyncFunctionDef
from dis import dis
from tokenize import Token
from unicodedata import name
import discord
from discord.ext import commands
import json
import os
import keep_alive                                               #import keep_alive
from discord_slash import SlashCommand                          #from discord_slash import Slashcommand

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    # with open(file name, mode = r or w..., encoding = 'utf8') as rename 'jfile'
    # variable 'jdata' = json.load('jfile')

intents = discord.Intents.default()                             #初始設定
intents.members = True
bot = commands.Bot(command_prefix="!", intents = intents)       #setting commands prefix
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)  #setting slash command

@bot.event                                                      #Bot online message
async def on_ready():
    print(">> AJ_Bot is online <<")

@bot.command()                                                  #Cog commands load file
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()                                                  #Cog commands unload file
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')

@bot.command()                                                  #Cog commands reload file
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')

for Filename in os.listdir('./cmds'):                           #Cog load all file(.py)
    if Filename.endswith('.py'):                                #use (prefix)help to search all commands
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":                                      #Bot run setting
    keep_alive.keep_alive()                                     #24H bot online
    bot.run(jdata['TOKEN'])                                     # Index = 'TOKEN'