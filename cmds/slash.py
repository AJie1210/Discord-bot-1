import discord
import json
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

    @cog_ext.cog_slash(name="Artstation", description="Artstation_website")
    async def artstation(self, ctx : SlashContext):
        await ctx.send('https://www.artstation.com/?sort_by=popular')

    @cog_ext.cog_slash(name="Bahamut",description="Bahamut_website")
    async def Bahamut(self, ctx : SlashContext):
        await ctx.send('https://www.gamer.com.tw/')

    @cog_ext.cog_slash(name="R6Stats",description="RainbowSixSeigestats_website")
    async def rainbowSix(self, ctx : SlashContext):
        await ctx.send('https://r6.tracker.network/')

    @cog_ext.cog_slash(name="DiscordBot-Web", description="Discord Portal_website")
    async def discordportal(self, ctx : SlashContext):
        await ctx.send('https://discord.com/developers/applications')
    
    

def setup(bot):
    bot.add_cog(Slash(bot))