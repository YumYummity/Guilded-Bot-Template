import guilded
from guilded.ext import commands

from colorama import Fore, Back, Style, init as coloramainit
coloramainit(autoreset=True)

import json, os, glob, logging
from logging.handlers import RotatingFileHandler

cogspath = "COGS/"
cogspathpy = [os.path.basename(f) for f in glob.glob(f'{cogspath}*.py')]
cogs = [f'{cogspath[:-1]}.' + os.path.splitext(f)[0] for f in cogspathpy]
logs_dir = 'logs'
errors_dir = os.path.join(logs_dir, 'errors')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
if not os.path.exists(errors_dir):
    os.makedirs(errors_dir)
logger = logging.getLogger('guilded')
logger.setLevel(logging.INFO)
# Create the rotating file handler with the logs folder
file_handler = RotatingFileHandler(f'{logs_dir}/guilded.log', maxBytes=32 * 1024 * 1024, backupCount=5)
file_handler.setLevel(logging.INFO)
# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class CONFIGS():
    '''
    Configs to start the bot.
    '''
    with open(f'config.json', 'r') as config:
        configdata = json.load(config)
    token:str = configdata['token']
    botid:str = configdata['bot_id']
    botuserid:str = configdata['bot_user_id']
    supportserverid:str = configdata['support_server']
    supportserverinv:str = configdata['support_server_invite']
    defaultprefix:str = configdata['default_prefix']
    owners:list = configdata['owners']
    error_logs_dir = errors_dir
    cogs_dir = cogspath

async def getprefix(bot: commands.Bot, message: guilded.Message) -> list:
    '''
    Get the prefix of a server.
    '''
    return [CONFIGS.defaultprefix]

bot = commands.Bot(command_prefix=getprefix, bot_id = CONFIGS.botid, experimental_event_style=True, owner_ids=CONFIGS.owners)
bot.CONFIGS = CONFIGS

@bot.event
async def on_ready():
    for cog in cogs:
        bot.load_extension(cog)
        print(f'{Fore.GREEN}Loaded cog {Fore.LIGHTBLUE_EX}{cog}')

    print(f'{Fore.GREEN}Bot ready! Logged in as {Fore.LIGHTBLUE_EX}{bot.user}')

if __name__ == '__main__':
    bot.run(CONFIGS.token)


