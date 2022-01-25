import discord
from discord.ext import commands, tasks
from core.classs import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def interval():
            await self.bot.wait_until_ready()       #wait bot online
            self.channel = self.bot.get_channel(934720325000777819)
            while not self.bot.is_closed():
                await self.channel.send("Bot is running !")
                await asyncio.sleep(10)     #sleep(seconds)

        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):       #ch:int 註解int型態
        self.set_channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

def setup(bot):
    bot.add_cog(Task(bot))