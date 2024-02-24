import guilded
from guilded.ext import commands

class developer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='load', description='Loads a cog.')
    async def load(self, ctx:commands.Context, *, cog_name: str):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)

        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name
        try:
            self.bot.load_extension(cog_name)
            self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Loaded cog {self.bot.COLORS.item_name}{cog_name}')
        except Exception as e:
            em = guilded.Embed(description="Failed to load cog.", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
            self.bot.traceback(e)
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
            self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Unloaded cog {self.bot.COLORS.item_name}{cog_name}')
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
            self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Reloaded cog {self.bot.COLORS.item_name}{cog_name}')
        except Exception as e:
            em = guilded.Embed(description="Failed to reload cog.", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
            self.bot.traceback(e)
        else:
            em = guilded.Embed(description="**Cog reloaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)

    @commands.command(name='eval', aliases=['exec'], description='eval/exec something for devs only')
    async def asyncexecute(self, ctx:commands.Context):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)
        async def aexec(code, message, bot):
            exec(f'async def __ex(message, bot):\n    '+(''.join(f'\n    {l}'for l in code.split('\n'))).strip(), globals(), locals())
            return (await locals()['__ex'](message, bot))
        prefix = ctx.clean_prefix
        cmd = ((ctx.message.content)[len(prefix) + 4:]).strip()
        try:
            await aexec(cmd, ctx.message, self.bot)
        except Exception as e:
            self.bot.traceback(e)
            await ctx.message.add_reaction(90002175)
            await ctx.message.reply(f'**Eval failed with Exception.**\nPlease check console.', private=ctx.message.private)
        else:
            await ctx.message.add_reaction(90002171)

def setup(bot):
	bot.add_cog(developer(bot))
