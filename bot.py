from ast import AsyncFunctionDef
from dis import dis
from tokenize import Token
import discord
from discord.ext import commands
import json
import random

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
async def ping(ctx):        # ctx include<username, id, server location, channel location>
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

@bot.command()
async def image_web(ctx):
    image_web = (jdata['url_pic'])      # url not file, so can't use "discord.File"
    await ctx.send(image_web)

@bot.command()
async def image_random(ctx):
    random_pic = random.choice(jdata['pic_random'])     #import random
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

@bot.command()
async def image_1(ctx):
    picture = discord.File(jdata['pic1'])
    await ctx.send(file = picture)

@bot.command()
async def image_2(ctx):
    picture = discord.File(jdata['pic2'])
    await ctx.send(file = picture)

bot.run(jdata['TOKEN'])     # Index = 'TOKEN'
