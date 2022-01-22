import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    # with open(file name, mode = r or w..., encoding = 'utf8') as rename 'jfile'
    # variable 'jdata' = json.load('jfile')

class React(Cog_Extension):
    @commands.command()
    async def image_web(self, ctx):
        image_web = (jdata['url_pic'])      # url not file, so can't use "discord.File"
        await ctx.send(image_web)

    @commands.command()
    async def image_random(self, ctx):
        random_pic = random.choice(jdata['pic_random'])     #import random
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()
    async def image_1(self, ctx):
        picture = discord.File(jdata['pic1'])
        await ctx.send(file = picture)

    @commands.command()
    async def image_2(self, ctx):
        picture = discord.File(jdata['pic2'])
        await ctx.send(file = picture)

def setup(bot):
    bot.add_cog(React(bot))