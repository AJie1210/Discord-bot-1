import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):      #__init__ bot
    def __init__(self, bot):
        self.bot = bot