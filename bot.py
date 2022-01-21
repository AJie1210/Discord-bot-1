from ast import AsyncFunctionDef
from tokenize import Token
import discord
from discord.ext import commands
import json

with open('setting.json', mode = 'r', encoding='utf8')as jfile:
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
async def ping(ctx):    # ctx include<username, id, server location, channel location>
    await ctx.send(f'{round(bot.latency*1000)} (ms)')
bot.run(jdata['TOKEN'])     # Index = 'TOKEN'