Back to [Example Checks](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/CHECKS/CHECKS.md)

# Checking a member's permissions
This guide will tell you how to check if a server member has a specified permission.

> [!IMPORTANT]
> The object has to be a `guilded.Member` object.
>
> You cannot check the permissions of a `guilded.User` object.

### Getting a Member object
Usually, when a command is run `ctx.author` is automatically a `guilded.Member` object.

```python
# in a cog
@commands.command(name="example", description="example command")
async def example(self, *, ctx: commands.Context):
    member = ctx.author
```

However, to be absolutely sure, you can check for the attribute "`.server`" using Python's builtin `hasattr()` function.

```python
# in a cog
@commands.command(name="example", description="example command")
async def example(self, *, ctx: commands.Context):
    member = ctx.author if hasattr(ctx.author, "server") else None
```

If you are confident that the command was run in a server and the user is in the server, you can additionally fetch the member.

```python
# in a cog
@commands.command(name="example", description="example command")
async def example(self, *, ctx: commands.Context):
    member = ctx.author if hasattr(ctx.author, "server") else None
    if member is None:
        try:
            member = await ctx.server.getch_member(ctx.author.id) if hasattr(ctx, "server") else None
        except guilded.NotFound:
            pass
```

If the `member` variable is still `None` after this, then the author is not in the server.

> [!NOTE]
> If you are checking ANOTHER user's permissions, you can use:
> ```python
> member = await server.getch_member("user id")
> ```

### Checking for a specific permission
A link to every permission can be found [here](https://guildedpy.readthedocs.io/en/stable/api.html?highlight=server_permissions#guilded.Permissions.administrator).

In order to check permissions, you can access the `guilded.Member.server_permissions` object.

For example, if you wanted to make sure the user had permission to update the server, you can do:

```python
# in a cog
@commands.command(name="example", description="example command")
async def example(self, *, ctx: commands.Context):
    member = ctx.author if hasattr(ctx.author, "server") else None
    if member is None:
        try:
            member = await ctx.server.getch_member(ctx.author.id) if hasattr(ctx, "server") else None
        except guilded.NotFound:
            pass
    
    if member.server_permissions.update_server:
        # they have update server permissions
    else:
        # they don't have update server permissions
```

### Conclusion
You can now check permissions. That's it.