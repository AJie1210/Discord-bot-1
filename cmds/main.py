from dis import dis
import imp
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):        # ctx include<username, id, server location, channel location>
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(Main(bot))