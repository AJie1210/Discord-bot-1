from ast import AsyncFunctionDef
from dis import dis
from tokenize import Token
import discord
from discord.ext import commands
import json
import os

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    # with open(file name, mode = r or w..., encoding = 'utf8') as rename 'jfile'
    # variable 'jdata' = json.load('jfile')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '!', intents = intents)

@bot.event
async def on_ready():
    print(">> AJ_Bot is online <<")

@bot.event
async def on_member_join(member: discord.Member):
    server = bot.get_guild(int(jdata['Guild']))
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'New member {member.mention} joined !')
    await channel.send(f'Welcome to the \"{server}\"')

@bot.event
async def on_member_remove(member: discord.Member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'Member {member.mention} left')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])     # Index = 'TOKEN'
