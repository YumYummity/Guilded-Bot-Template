Back to [Example Functions](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/FUNCTIONS/FUNCTIONS.md)

> [!WARNING]
> This is not officially supported code. This implementation is a hacky way involving the user api.
>
> This may be patched at any time.

# The Fetch Channels Function
This is not a guide. This is the plain code for how to fetch a server's channels.

This was made to mimic `guilded.py` as much as possible. It also caches these into `guilded.py` like `fetch_channel` does.

## The Code
```python
import guilded
from guilded.ext import commands
from typing import List

async def fetch_channels(server: guilded.Server, client: guilded.Client | commands.Bot) -> List[guilded.abc.ServerChannel]:
    """|coro|

    Fetch the list of channels in a server.

    Returns
    --------
    List[:class:`ServerChannel`]
        The channels of the server.
    """
    data = await client.http.request(client.http.Route('GET', f'/teams/{server.id}/channels', override_base=client.http.Route.USER_BASE))

    channels = []
    for channel in data["channels"]:
        channel["serverId"] = channel["teamId"]
        channel_object = client.http.create_channel(data=channel)
        channels.append(channel_object)
        # Bot DM channels do not exist yet, but this prevents the server channel cache from breaking when they are added.
        if channel_object.type == guilded.ChannelType.dm:
            client.http.add_to_dm_channel_cache(channel_object)
        else:
            client.http.add_to_server_channel_cache(channel_object)
    return channels
```

## Usage
The arguments you need to pass are the `server` and `client/bot`.

### Example Usage
Putting the code into a file called `utilities.py`:
```python
from utilities import fetch_channels

async def some_command(ctx: commands.Context):
    channels = await fetch_channels(ctx.server, ctx.bot)
```