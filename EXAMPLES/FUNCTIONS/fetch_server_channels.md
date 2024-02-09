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
    token = client.http.token
    if not token:
        return []
    
    headers = {
        "user-agent": client.http.user_agent,
        "accept": "application/json, text/javascript, */*; q=0.01",
        "authorization": f"Bearer {token}"
    }

    url = f"https://www.guilded.gg/api/teams/{server.id}/channels"
    
    async with client.http.session.get(url, headers=headers) as resp:
        if resp.status != 200:
            return []  # or raise an exception if needed
        data = await resp.json()

    channels = []
    for channel in data["channels"]:
        channel["serverId"] = channel["teamId"]
        channel_object = client.http.create_channel(data=channel)
        channels.append(channel_object)
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
    channels = await fetch_channels(ctxserver, ctx.bot)
```