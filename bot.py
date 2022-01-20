from ast import AsyncFunctionDef
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '!', intents = intents)

@bot.event
async def on_ready():
    print(">> AJ_Bot is online <<")

@bot.event
async def on_member_join(member: discord.Member):
    server = bot.get_guild(933732477216899182)
    channel = bot.get_channel(933785604792131584)
    await channel.send(f'A member {member.mention} join !')
    await channel.send(f'Welcome to the {server}')

@bot.event
async def on_member_remove(member: discord.Member):
    channel = bot.get_channel(933733567601709056)
    await channel.send(f'Member {member.mention} left')

bot.run('OTMzNjEyMTEzNDY3OTQwOTE3.YekECQ.zeQ0d13I_MUEkELihDsLplx1IZE')