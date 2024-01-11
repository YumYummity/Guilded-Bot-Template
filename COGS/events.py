from colorama import Fore, init as coloramainit
coloramainit()
import guilded
from guilded.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener("message")
    async def messagemoment(self, event: guilded.MessageEvent):
        message = event.message
        if self.bot.user.id in message.raw_user_mentions and len(message.raw_user_mentions) == 1:
            if message.content == f"@{self.bot.user.display_name}":
                try:
                    await message.reply(embed=guilded.Embed(title="That's Me!",description=f"Hi, {event.message.author.mention}! My prefix is `{self.bot.command_prefix}`.\nPlease check `{self.bot.command_prefix}help` for more info."), private=message.private)
                except:
                    pass
            

def setup(bot):
	bot.add_cog(events(bot))