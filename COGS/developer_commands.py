import guilded
from guilded.ext import commands
import asyncio
import glob
import os
import sys

class developer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='load', description='Loads a cog.')
    async def load(self, ctx:commands.Context, *, cog_name: str):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)
        ocog_name = cog_name

        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name
        try:
            self.bot.load_extension(cog_name)
            self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Loaded cog {self.bot.COLORS.item_name}{cog_name}')
            em = guilded.Embed(description="**Cog loaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
        except Exception as e:
            if ocog_name == "all":
                cogspathpy = [os.path.basename(f) for f in glob.glob(f'{self.bot.CONFIGS.cogs_dir}*.py')]
                cogs = [f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + os.path.splitext(f)[0] for f in cogspathpy]
                for cog in cogs:
                    try:
                        self.bot.load_extension(cog)
                        self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Loaded cog {self.bot.COLORS.item_name}{cog}')
                    except commands.ExtensionAlreadyLoaded:
                        pass
                    except Exception as e:
                        em = guilded.Embed(description=f"Failed to load cog `{cog}`", color=0x363942)
                        await ctx.reply(embed=em, private=ctx.message.private)
                        self.bot.traceback(e)
                em = guilded.Embed(description="**All cogs loaded.**", color=0x363942)
                await ctx.reply(embed=em, private=ctx.message.private)
                return
            em = guilded.Embed(description="Failed to load cog.", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
            self.bot.traceback(e)

    @commands.command(name='unload', description='Unloads a cog.')
    async def unload(self, ctx:commands.Context, *, cog_name: str):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)
        ocog_name = cog_name
        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name

        if ocog_name == "all" and (not cog_name in self.bot.extensions):
            for cog in [cog for cog in self.bot.extensions]:
                if cog in self.bot.extensions:
                    if self.bot.extensions[cog] == sys.modules[__name__]:
                        em = guilded.Embed(description=f"`{cog}` cog wasn't unloaded, you do need access to these commands. Use reload instead.", color=0x363942)
                        await ctx.reply(embed=em, private=ctx.message.private)
                        continue
                    try:
                        self.bot.unload_extension(cog)
                        self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Unloaded cog {self.bot.COLORS.item_name}{cog}')
                    except commands.ExtensionNotLoaded:
                        pass
                else:
                    em = guilded.Embed(description=f"`{cog}` cog isn't loaded.", color=0x363942)
                    await ctx.reply(embed=em, private=ctx.message.private)
            em = guilded.Embed(description="**All cogs unloaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
        else:
            if cog_name in self.bot.extensions:
                try:
                    self.bot.unload_extension(cog)
                    self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Unloaded cog {self.bot.COLORS.item_name}{cog_name}')
                except commands.ExtensionNotLoaded:
                    pass
                em = guilded.Embed(description="**Cog unloaded.**", color=0x363942)
                await ctx.reply(embed=em, private=ctx.message.private)
            else:
                em = guilded.Embed(description="That cog isn't loaded.", color=0x363942)
                await ctx.reply(embed=em, private=ctx.message.private)

    @commands.command(name='reload', description='Reloads a cog.')
    async def reload(self, ctx:commands.Context, *, cog_name: str = None):
        if not ctx.author.id in self.bot.CONFIGS.owners:
            return await ctx.reply('No.', private=ctx.message.private)
        ocog_name = cog_name
        if not cog_name.startswith(f'{self.bot.CONFIGS.cogs_dir[:-1]}.'):
            cog_name = f'{self.bot.CONFIGS.cogs_dir[:-1]}.' + cog_name

        if ocog_name == "all" and (not cog_name in self.bot.extensions):
            for cog in [cog for cog in self.bot.extensions]:
                try:
                    self.bot.reload_extension(cog)
                    self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Reloaded cog {self.bot.COLORS.item_name}{cog}')
                except Exception as e:
                    em = guilded.Embed(description=f"Failed to reload cog `{cog}`", color=0x363942)
                    await ctx.reply(embed=em, private=ctx.message.private)
                    self.bot.traceback(e)
            em = guilded.Embed(description="**All cogs reloaded.**", color=0x363942)
            await ctx.reply(embed=em, private=ctx.message.private)
        else:
            try:
                self.bot.reload_extension(cog_name)
                self.bot.print(f'{self.bot.COLORS.cog_logs}[COGS] {self.bot.COLORS.normal_message}Reloaded cog {self.bot.COLORS.item_name}{cog_name}')
                em = guilded.Embed(description="**Cog reloaded.**", color=0x363942)
                await ctx.reply(embed=em, private=ctx.message.private)
            except Exception as e:
                em = guilded.Embed(description="Failed to reload cog.", color=0x363942)
                await ctx.reply(embed=em, private=ctx.message.private)
                self.bot.traceback(e)

    @commands.command(name='eval', aliases=['exec'], description='eval/exec something for devs only')
    async def asyncexecute(self, ctx:commands.Context):
        troll = False # do you want to troll someone who tries to run eval without permissions?
        if not ctx.author.id in self.bot.CONFIGS.owners:
            if troll:
                await ctx.message.add_reaction(90001732)
                await asyncio.sleep(2)
            return await ctx.reply('YOU REALLY THOUGHT' if troll else "Access denied.", private=ctx.message.private)
        async def aexec(code, message, bot):
            exec(f'async def __ex(message, bot):\n    '+(''.join(f'\n    {l}'for l in code.split('\n'))).strip(), globals(), locals())
            return (await locals()['__ex'](message, bot))
        prefix = ctx.clean_prefix
        cmd = ((ctx.message.content)[len(prefix) + 4:]).strip()
        try:
            await ctx.message.add_reaction(90001733)
            await aexec(cmd, ctx.message, self.bot)
        except Exception as e:
            self.bot.traceback(e)
            await ctx.message.add_reaction(90002175)
            await ctx.message.reply(f'**Eval failed with Exception.**\nPlease check console.', private=ctx.message.private)
        else:
            await ctx.message.add_reaction(90002171)
        await ctx.message.remove_reaction(90001733)

def setup(bot):
	bot.add_cog(developer(bot))
