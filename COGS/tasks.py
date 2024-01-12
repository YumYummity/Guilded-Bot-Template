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
            server_count = len(await self.bot.fetch_servers())
            statuses = [
                [None, f"Watching {server_count} server{'s' if server_count != 1 else ''}!", 10],
                [None, f"Helping you build Guilded bots!", 30],
                [None, f"https://github.com/YumYummity/Guilded-Bot-Template/tree/main", 60]
            ]
            for status in statuses:
                try:
                    await self.bot.set_status(status[0] if status[0] else 90002547, content=status[1])
                    self.bot.info(f"Status changed to {self.bot.COLORS.item_name}{status[1]}{self.bot.COLORS.normal_message} with emoji id {self.bot.COLORS.item_name}{status[0] if status[0] else '90002547 (None)'}{self.bot.COLORS.normal_message} for {self.bot.COLORS.item_name}{status[2]}{self.bot.COLORS.normal_message} seconds")
                    await asyncio.sleep(status[2])
                except Exception as e:
                    self.bot.warn(f"An error occurred while attempting to change the bot's status: {self.bot.COLORS.item_name}{e}")

def setup(bot):
	bot.add_cog(tasks(bot))