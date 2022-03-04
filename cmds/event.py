from discord.ext import commands
from core.classs import Cog_Extension
import json

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = self.bot.get_guild(int(jdata['Guild']))
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))       #Welcome message
        await channel.send(f'New member {member.mention} joined !')
        await channel.send(f'Welcome to the \"{server}\"')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))         #Leave message
        await channel.send(f'Member {member.mention} left')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = jdata['keywords']
        if msg.content in keyword and msg.author != self.bot.user:          #keyword reply
            await msg.channel.send('Hi , nice to meet you !')

def setup(bot):
    bot.add_cog(Event(bot))