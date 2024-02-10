**WIP**

Back to [Example Databases](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/DATABASES/DATABASES.md)

# Implementing PostgreSQL into your Guilded Bot
This guide will show you how to implement a psql database into your bot, as well as changing server prefixes using psql.

### Requirements
An additional library needs to be installed: `asyncpg`

Please install it with `pip install asyncpg`.

## Connecting to the DB
In your main file (`main.py`), import the library you just installed: `import asyncpg`

In your `on_ready` function, at the start, add the following lines:
```py
try:
    bot.db
except:
    bot.db = await asyncpg.create_pool("YOUR PSQL CONNECTION URI", min_size=1,max_size=1)
```

> [!NOTE]
> The `on_ready` function may be called multiple times.
>
> Using the try-catch, we attempt to check if `bot.db` was previously defined already.
>
> Only if it's not, we connect to the db with a pool and define `bot.db`

> [!NOTE]
> The database connection URI should look something like this:
>
> `postgresql://username:password@ip:port/user`
>
> `port` should default to 5432

Based on your database and user count, determine how many connections are necessary. By default, psql servers allow a maximum of 100, but some headroom should be given. We recommend a maximum of `75` connections.

## Queries and Executions
WIP

## Changing, Setting, and Fetching Prefixes
WIP