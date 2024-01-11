import traceback

from colorama import Fore, init as coloramainit
coloramainit()
import guilded
from guilded.ext import commands

class COGNAME(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', description='Loads a cog.')
    async def load(self, ctx:commands.Context, *, cog_name: str):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)

        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name
        try:
            self.bot.load_extension(cog_name)
        except Exception as e:
            em = guilded.Embed(description="Failed to load cog.", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
            tb = ''.join(traceback.format_exception(e, e, e.__traceback__))
            print(tb)
        else:
            em = guilded.Embed(description="**Cog loaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)

    @commands.command(name='unload', description='Unloads a cog.')
    async def unload(self, ctx:commands.Context, *, cog_name: str):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)
        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name

        if cog_name in self.bot.extensions:
            self.bot.unload_extension(cog_name)
            em = guilded.Embed(description="**Cog unloaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
        else:
            em = guilded.Embed(description="That cog isn't loaded.", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)

    @commands.command(name='reload', description='Reloads a cog.')
    async def reload(self, ctx:commands.Context, *, cog_name: str = None):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)
        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name

        try:
            self.bot.unload_extension(cog_name)
            self.bot.load_extension(cog_name)
        except Exception as e:
            em = guilded.Embed(description="Failed to reload cog.", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
            tb = ''.join(traceback.format_exception(e, e, e.__traceback__))
            print(tb)
        else:
            em = guilded.Embed(description="**Cog reloaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)

def setup(bot):
	bot.add_cog(COGNAME(bot))