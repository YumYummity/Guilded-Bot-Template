import traceback

from colorama import Fore, init as coloramainit
coloramainit()
import guilded
from guilded.ext import commands

class developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='eval', aliases=['exec'], description='eval/exec something for devs only')
    async def asyncexecute(self, ctx:commands.Context):
        async def aexec(code, message):
            exec(f'async def __ex(message):\n    '+(''.join(f'\n    {l}'for l in code.split('\n'))).strip(), globals(), locals())
            return (await locals()['__ex'](message))
        async def evalcheck(userid):
            if userid in self.bot.CONFIGS.owners:
                return True
            return False
        prefix = ctx.clean_prefix
        cmd = ((ctx.message.content)[len(prefix) + 4:]).strip()
        if (await evalcheck(ctx.author.id)):
            try:
                await aexec(cmd, ctx.message)
            except Exception as e:
                result = ("".join(traceback.format_exception(e, e, e.__traceback__))).replace('`', '\`')
                print(result)
                await ctx.message.reply(f'**Eval failed with Exception.**\nPlease check console.')
                await ctx.message.add_reaction(90002175)
            else:
                await ctx.message.add_reaction(90002171)

def setup(bot):
	bot.add_cog(developer(bot))