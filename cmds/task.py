from discord.ext import commands
from core.classs import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)                                                    #keep classs.py __init__ bot

        """ async def interval():
            await self.bot.wait_until_ready()       #wait bot online
            self.channel = self.bot.get_channel(934720325000777819)
            while not self.bot.is_closed():
                await self.channel.send("Bot is running !")
                await asyncio.sleep(10)     #sleep(seconds)

        self.bg_task = self.bot.loop.create_task(interval()) """

        async def time_task():                                                              #整點報時_module
            await self.bot.wait_until_ready()                                               #wait bot online
            self.channel = self.bot.get_channel(934720325000777819)
            while not self.bot.is_closed():
                now_time = datetime.datetime.utcnow().strftime('%M%S')                         #(min,sec)
                with open('setting.json','r',encoding = 'utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time']:                                               #set_time while time == set_time
                    await self.channel.send("Task is working !")                        
                    await self.channel.send(datetime.datetime.utcnow())       
                    await asyncio.sleep(1)                             
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()                                                                     #set_channel
    async def set_channel(self, ctx, ch:int):                                               #ch:int 註解int型態
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')                              #self.channel.mention = hashtag sth

    @commands.command()                                                                     #read and write on JsonFile(time_setting)
    async def set_time(self, ctx, time):
        with open('setting.json','r',encoding = 'utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json','w',encoding = 'utf8') as jfile:
            json.dump(jdata,jfile,indent=4)

def setup(bot):
    bot.add_cog(Task(bot))