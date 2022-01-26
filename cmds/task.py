import discord
from discord.ext import commands, tasks
from core.classs import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)        # keep classs.py __init__ bot

        """ async def interval():
            await self.bot.wait_until_ready()       #wait bot online
            self.channel = self.bot.get_channel(934720325000777819)
            while not self.bot.is_closed():
                await self.channel.send("Bot is running !")
                await asyncio.sleep(10)     #sleep(seconds)

        self.bg_task = self.bot.loop.create_task(interval()) """

        async def time_task():
            await self.bot.wait_until_ready()       #wait bot online
            self.channel = self.bot.get_channel(935857983366234112)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%M')
                with open('setting.json','r',encoding = 'utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time']:
                    await self.channel.send("Task is working !")
                    await self.channel.send(datetime.datetime.utcnow())       #set_time while time == set_time
                    await asyncio.sleep(1)                              #send message
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch:int):       #ch:int 註解int型態
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')      #self.channel.mention = hashtag sth

    @commands.command()
    async def set_time(self, ctx, time):
        with open('setting.json','r',encoding = 'utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json','w',encoding = 'utf8') as jfile:
            json.dump(jdata,jfile,indent=4)
def setup(bot):
    bot.add_cog(Task(bot))