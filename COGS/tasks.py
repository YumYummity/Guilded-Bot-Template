import asyncio

import guilded
from guilded.ext import commands

class tasks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        asyncio.create_task(self.change_status())
    
    async def change_status(self):
        while True:
            # [emoji id / None, status message, delay]
            statuses = [
                [None, f"Watching {len(await self.bot.fetch_servers())} servers!", 10],
                [None, f"Helping you build Guilded bots!", 10],
                [None, f"https://github.com/YumYummity/Guilded-Bot-Template/tree/main", 10]
            ]
            for status in statuses:
                await self.bot.set_status(status[0] if status[0] else 90002547, status[1])
                await asyncio.sleep(status[2])

def setup(bot):
	bot.add_cog(tasks(bot))