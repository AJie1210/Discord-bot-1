from dis import dis
import discord
from discord.ext import commands
from core.classs import Cog_Extension
import datetime

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):        # ctx include<username, id, server location, channel location>
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def R6E_embed(self, ctx):
        embed=discord.Embed(title="Rainbow Six Extraction", url="https://www.youtube.com/watch?v=-_QWD81HdAM", description="Official Introduce Video", color=0x0008ff, 
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="Leoson20718", url="https://discord.gg/xrtXZz4b", icon_url="https://cdna.artstation.com/p/assets/images/images/042/134/628/medium/jing-zhang-01.jpg?1633655009")
        embed.set_thumbnail(url="https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1oH1jUZj1VZYxey5Mp8vYP/558408976d9552372a2cc3952db69458/page-meta_R6X.png")
        embed.add_field(name="Leoson's Server", value="https://discord.gg/xrtXZz4b", inline=False)
        embed.add_field(name="Rainbow Six Extraction's Server", value="https://discord.gg/m59zUuNc5N", inline=True)
        embed.set_footer(text="Rainbow Six Extraction")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))