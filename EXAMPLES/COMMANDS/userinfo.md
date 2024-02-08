Back to [Example Commands](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/COMMANDS/COMMANDS.md)

# Starting an User Info Command
This guide will walk you through the process of starting a basic user info command. This guide will assume you are using a cog, but code will not indented like in a cog. [Cogs Guide](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/COGS/COGS.md)

A default prefix of `!` is assumed here.

### Registering the command
The simple code to register a user info command is:
```py
@commands.command(name="userinfo", description="Your command description", aliases=["who"])
async def userinfo(self, ctx: commands.Context, *, user: str = None):
```

You should already know what the first line does. If you don't, please familiarize yourself with the [guilded.py documentation](https://guildedpy.readthedocs.io/en/stable/ext/commands/commands.html?highlight=bot.command#commands) (links directly to the related section).

For the second line, it determines the user to fetch the user data on.

`*, user: str = None` means any input after the original command (eg. `!userinfo SOME ARGUMENTS`) gets assigned to the `user` variable. In this case, the `user` variable would be assigned the value "`SOME ARGUMENTS`". In the case no arguments are supplied (eg. `!userinfo`), the `user` variable defaults to None.

> [!IMPORTANT]  
> Why aren't we using the `guilded.Member` converter? [Related Documentation](https://guildedpy.readthedocs.io/en/stable/ext/commands/commands.html?highlight=member%20converter#guilded-converters)
> 
> ```python
> async def userinfo(self, ctx: commands.Context, *, user: guilded.Member = None):
> ```
>
> The `guilded.Member` converter does NOT work with pings, but will work with user ids
>
> `!userinfo @user` will NOT work with the `guilded.Member` converter.
>
> `!userinfo userid` will work with the `guilded.Member` converter.
>
> If we want to support mentions as a valid input, the `guilded.Member` converter cannot be used. The same applies to the `guilded.User` converter.

### Getting the user
Now that we've defined our command, we need to determine the user to fetch the data from.
```py
@commands.command(name="userinfo", description="Your command description", aliases=["who"])
async def userinfo(self, ctx: commands.Context, *, user: str = None):
    if user is None:
        user = ctx.author
    else:
        user_mentions =  ctx.message.raw_user_mentions
        if len(user_mentions) > 0:
            user = await ctx.server.fetch_member(user_mentions[-1])
        else:
            try:
                user = await ctx.server.fetch_member(user)
            except guilded.NotFound:
                try:
                    user = await self.bot.fetch_user(user)
                except guilded.NotFound:
                    user = None

    if user is None:
        await ctx.send(embed=guilded.Embed(title="Invalid User Selected", description="You selected an invalid user. Please try again!", color=guilded.Color.red()))
```

While this may seem complicated, it's actually pretty simple. Since `user` can be an id or mention, we can check to see if it's either.

First, we should determine if there is no user specified. Since `user` defaults to `None` if nothing is passed, we can check that.
```py
if user is None:
    user = ctx.author
```
If no user is specified, set the user to the author of the command.

However, if something is passed (whether it's a user or not), we can start checking to see if it's a valid user.
```py
else:
    user_mentions =  ctx.message.raw_user_mentions
    if len(user_mentions) > 0:
        user = await ctx.server.fetch_member(user_mentions[-1])
    else:
        try:
            user = await ctx.server.fetch_member(user)
        except guilded.NotFound:
            try:
                user = await self.bot.fetch_user(user)
            except guilded.NotFound:
                user = None
```
First, we check if there are any mentions in the command. If found, we ignore any passed content (assuming it's a mention) and attempt to get the LAST mention (if there are multiple). `ctx.message.raw_user_mentions` returns a list of ids mentioned.

> [!NOTE]
> We get the LAST mention. If you want to get the FIRST mention, you can change it to:
>
> ```py
> user_mentions[0]
> ```
>
> You may also want to restrict the amount of mentions to 1:
>
> ```py
> elif len(user_mentions) > 1:
>     # do something
> ```

If there are no mentions, we assume that the passed content for `user` is a user id. From there, we first attempt to fetch it as a server member. Using a try-catch, we determine if it's a valid member or not. If it is, everything is continued. If it isn't, the same is repeated, except this time we attempt to fetch it as a normal Guilded user.

Then, if the `user` variable is still `None` (no mentions, and an invalid id was passed), we tell this to the author of the command.
```py
if user is None:
    await ctx.send(embed=guilded.Embed(title="Invalid User Selected", description="You selected an invalid user. Please try again!", color=guilded.Color.red()))
```

### Conclusion
From this point on, you can use the `user` variable as you wish. It will either be a `guilded.Member` or `guilded.User` object.