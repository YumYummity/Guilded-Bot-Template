[Overview](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/README.md) / [Setup](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/SETUP.md) / **Cogs** / [Logging](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/logs/LOGGING.md) / [Examples](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/EXAMPLES.md)

# Cogs
A cog is a way to organize your commands and/or events into a file, which you can then load. You can update commands by simply reloading a cog after you make changes, meaning this is a great way to modify your code without restarting the entire bot!

As mentioned in the Final Comments section of the Overview: If you are having trouble with any of these steps (or understanding most of the code), `guilded.py` may be too advanced for you. Consider learning some more Python first.

This does not contain everything you need to know about cogs, but rather some of the basics.

### Basic Code
Let's take at the example code for a cog with no functionality. This guide assumes you are familiar with classes. If not, please familiarize yourself. Good resource: https://www.w3schools.com/python/python_classes.asp

The example:
```python
import guilded
from guilded.ext import commands

class COGNAME(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot):
	bot.add_cog(COGNAME(bot))
```

The first two lines import `guilded.py`, as well as the `commands` extension. This should be added to every cog file.
```python
import guilded
from guilded.ext import commands
```

The third line creates a class that serves as your cog, and it inherits from the `commands.Cog` `class` provided by the `guilded.py` library. The name assigned to this class should be unique, and will be referenced in the last line.
```python
class COGNAME(commands.Cog):
```

The fourth and fifth line pass the `bot` object into the class. Classes have a function called `__init__()`, which is always executed when the class is being initiated.

We use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created.
```python
    def __init__(self, bot: commands.Bot):
        self.bot = bot
```

Finally, the last two lines setup the entire python file to load the cog when `guilded.py` attempts to load the file. If the `setup` function is not present, `guilded.py` cannot load the cog. `COGNAME` should be replaced with the unique name you gave to your class in line three.
```python
def setup(bot):
    bot.add_cog(COGNAME(bot))
```

### Making Commands
When you usually make a command, you use the `@bot.command()` (or similar) decorator. This guide assumes you know how to make a normal command.

To make a command in a cog, it's pretty much the same. First, you make sure your command's function is inside the class, indented properly.
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def ping_command(ctx: commands.Context):
        await ctx.send(f"Pong!")

def setup(bot):
	bot.add_cog(example_cog(bot))
```

Then, you use the `@commands.command()` decorator instead of the `@bot.command()` decorator. These work the exact same.
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping_command(ctx: commands.Context):
        await ctx.send(f"Pong!")

def setup(bot):
	bot.add_cog(example_cog(bot))
```

Now, there's a common mistake everyone makes. If you get an error similar to `TypeError: {FUNCTION NAME}() takes exactly {n} positional argument(s) ({n} given)`, you probably made this mistake.

Functions in classes MUST have the `self` argument as the first argument in their definitions. Everything else afterwards is the same.
```python
async def ping_command(self, ctx: commands.Context):
```
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping_command(self, ctx: commands.Context):
        await ctx.send(f"Pong!")

def setup(bot):
	bot.add_cog(example_cog(bot))
```

You may also access the `bot` object as `self.bot`.
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping_command(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency*1000, 3)}ms ping.")

def setup(bot):
	bot.add_cog(example_cog(bot))
```

### Handling Events
> [!IMPORTANT]  
> This template uses the **experimental event style** provided by `guilded.py`. For more information, check the Overview.

Like before, everything is pretty much the same. This guide assumes you know how to make a normal event handler.

Again, you make sure your command's function is inside the class, indented properly.
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def on_message(event: guilded.MessageEvent):
        print(event.message.content)

def setup(bot):
	bot.add_cog(example_cog(bot))
```

Then, you use the `@commands.Cog.listener()` decorator instead of the `@bot.event` decorator. Notice that the `listener()` decorator accepts arguments unlike the `event` decorator.
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(event: guilded.MessageEvent):
        print(event.message.content)

def setup(bot):
	bot.add_cog(example_cog(bot))
```
An example with arguments used may look like:
```python
@commands.Cog.listener("on_message")
async def MESSAGE_RECEIVED(event: guilded.MessageEvent):
    print(event.message.content)
```

Remember the common mistake everone makes? Functions in classes MUST have the `self` argument as the first argument in their definitions. Everything else afterwards is the same.
```python
async def on_message(self, event: guilded.MessageEvent):
```
```python
import guilded
from guilded.ext import commands

class example_cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, event: guilded.MessageEvent):
        print(event.message.content)

def setup(bot):
	bot.add_cog(example_cog(bot))
```
