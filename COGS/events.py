import guilded
from guilded.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener("on_command")
    async def commandwasrun(self, ctx: commands.Context):
        self.bot.print(f'{self.bot.COLORS.command_logs}[COMMAND] {self.bot.COLORS.user_name}{ctx.author.name}{self.bot.COLORS.normal_message} ran command {self.bot.COLORS.item_name}{ctx.command.qualified_name}{self.bot.COLORS.normal_message} on the server {self.bot.COLORS.item_name}{ctx.server.name}{self.bot.COLORS.normal_message}. Full command: {self.bot.COLORS.item_name}{ctx.message.content}')


    @commands.Cog.listener("on_message")
    async def messagemoment(self, event: guilded.MessageEvent):
        message = event.message
        if self.bot.user.id in message.raw_user_mentions and len(message.raw_user_mentions) == 1:
            if message.content.strip() == f"@{self.bot.user.display_name}":
                try:
                    await message.reply(embed=guilded.Embed(title="That's Me!",description=f"Hi, {event.message.author.mention}! My prefix is `{(await (self.bot.command_prefix)(self.bot, message))[0]}`.\nPlease check `{(await (self.bot.command_prefix)(self.bot, message))[0]}help` for more info."), private=message.private)
                    self.bot.print(f'{self.bot.COLORS.command_logs}[COMMAND] {self.bot.COLORS.user_name}{message.author.name}{self.bot.COLORS.normal_message} ran command {self.bot.COLORS.item_name}@PING{self.bot.COLORS.normal_message} on the server {self.bot.COLORS.item_name}{message.server.name}{self.bot.COLORS.normal_message}. Full command: {self.bot.COLORS.item_name}{message.content}')
                except:
                    pass
            

def setup(bot):
	bot.add_cog(events(bot))