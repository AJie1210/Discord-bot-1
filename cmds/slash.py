import discord
import json
from discord.ext import commands
from core.classs import Cog_Extension
from discord_slash import SlashContext, cog_ext

with open('setting.json', mode = 'r', encoding='utf8') as jfile:        
    jdata = json.load(jfile)

class Slash(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot

    @cog_ext.cog_slash(name="hello", description="slash test")
    async def response(self, ctx: SlashContext):
        embed = discord.Embed(title="Hi, nice to meet you")
        await ctx.send(content="test", embeds=[embed])
    
    @cog_ext.cog_slash(name="ping", description="ping test")
    async def delay(self, ctx : SlashContext):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(Slash(bot))