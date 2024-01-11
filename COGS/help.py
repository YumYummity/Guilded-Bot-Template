from colorama import Fore, init as coloramainit
coloramainit()
import guilded
from guilded.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='help', description='Help for every command this bot has!', aliases=['h'])
    async def help(self, ctx:commands.Context, *, command:str=None) -> guilded.Message|guilded.ChatMessage:
        '''
        Help command
        '''
        if command:
            command = command.lower()
        prefixdata = ctx.prefix
        if command:
            if command.startswith(prefixdata):
                command = command[len(prefixdata):len(command)]
        inviteandsupport = f'\n\n[Invite](https://guilded.gg/b/{self.bot.CONFIGS.botid}) || [Support Server]({self.bot.CONFIGS.supportserverinv})'
        helpcmd = []
        if command:
            helpcmd = None
            for i in self.bot.commands:
                if (i.qualified_name).lower() == command or command in i.aliases:
                    helpcmd = i
                    break
        else:
            for i in self.bot.commands:
                helpcmd.append(i.qualified_name)
        if command is None:
            embedig = guilded.Embed(
                title='Command Help',
                description=f'Command Count: `{len(self.bot.commands)}`\n**Do {prefixdata}help <command> for more info!**{inviteandsupport}'
            )
            embedig.add_field(name="Commands", value=", ".join(helpcmd), inline=False)
        elif command:
            if not helpcmd:
                return await ctx.reply('Command not found.', private=True)
            embedig = guilded.Embed(
                title='Command Help',
                description=f'Command `{helpcmd.qualified_name}`\'s information.{inviteandsupport}'
            )
            embedig.add_field(name='Command Description', value=f'{helpcmd.description}')
            aliases = helpcmd.aliases
            if (", ".join(aliases)).strip() == '':
                aliases = 'None'
            else:
                aliases = ", ".join(aliases)
            embedig.add_field(name='Command Aliases', value=f'{aliases}')
        await ctx.reply(embed=embedig, private=ctx.message.private)

def setup(bot):
	bot.add_cog(help(bot))