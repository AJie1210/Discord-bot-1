import discord
from discord.ext import commands
from core.classs import Cog_Extension
import random
import json
import datetime


with open('setting.json', mode = 'r', encoding='utf8') as jfile:        
    jdata = json.load(jfile)
    # load JsonFile
    # with open(file name, mode = r or w..., encoding = 'utf8') as rename 'jfile'
    # variable 'jdata' = json.load('jfile')

class React(Cog_Extension):
    @commands.command()                                     #return web_image
    async def image_web1(self, ctx):
        image_web1 = (jdata['url_pic'])                     #url not file, so can't use "discord.File"
        await ctx.send(image_web1)
    
    @commands.command()                                     #return web_image
    async def image_web2(self, ctx):
        image_web2 = (jdata['url_pic_kanahei'])
        await ctx.send(image_web2)

    @commands.command()                                     #return local_image(random)
    async def image_random(self, ctx):
        random_pic = random.choice(jdata['pic_random'])     #import random
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()                                     #return local_image
    async def image_1(self, ctx):
        picture = discord.File(jdata['pic1'])
        await ctx.send(file = picture)

    @commands.command()
    async def image_2(self, ctx):                           #return local_image
        picture = discord.File(jdata['pic2'])
        await ctx.send(file = picture)
    
    @commands.command()                                     #return time_now(utc)
    async def time_now(self, ctx):
        time = datetime.datetime.now()
        await ctx.send(time)

    @commands.group()                                       #group commands and subcommand
    async def subcommand(self, ctx):
        await ctx.send("Subcommand")
    @subcommand.command()
    async def sub1(self, ctx):
        await ctx.send("this is subcommand 1 ")
    @subcommand.command()
    async def sub2(self, ctx):
        await ctx.send("this is subcommand 2 ")
    @subcommand.command()
    async def sub3(self, ctx):
        await ctx.send("this is subcommand 3 ")
        
def setup(bot):
    bot.add_cog(React(bot))