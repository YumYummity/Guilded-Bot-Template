# Guilded Bot Template
This template includes:
- Basic help command
- Cog handling
- Cogs loading/unloading/reloading commands for owners
- Advanced logging
- Errors logging (when an error (traceback) occurs, it'll save to a txt file and tell the user the error ID)
- Permission missing error handling (when a permission is missing, it'll tell the user exactly what permissions are missing)
- Eval/exec command
- Config file
- Replies on ping

# Logging
- Use `bot.traceback(Exception)` to log and format errors. Otherwise, they won't be logged properly.
    - You can use `print()` for debug statements you don't want logged.
- Use `bot.print()` to print things. Otherwise, it won't be logged properly. This will also add a timestamp.
    - You can use `print()` for debug statements you don't want logged.
- Use `bot.info()` to print info messages.
- Use `bot.error()` to print error messages.
- Use `bot.success()` to print success messages.
- Use `bot.warn()` to print warning messages.
![image](https://github.com/YumYummity/Guilded-Bot-Template/assets/103061664/4326b287-ebf3-4e31-a175-348bf1342cf1)

## Logging Colors
### Explanation
- You can use `bot.COLORS.item_name` when logging to highlight a input or item in logs.
    - Example: `f"A user ran the command {bot.COLORS.item_name}!help{bot.COLORS.normal_message} on a server."`
- You can use `bot.COLORS.user_name` when logging to highlight a user's name in logs.
    - Example: `f"{bot.COLORS.user_name}{ctx.author.name}{bot.COLORS.normal_message} ran a command.`
- You can use `bot.COLORS.cog_logs` to color a [COGS] log. (Use `bot.print`!)
    - Example: `bot.print(f"{bot.COLORS.cog_logs}[COGS]{bot.COLORS.normal_message} Loaded cog.")`
    - `error_logs`, `warn_logs`, `info_logs`, and `success_logs` are also available, but it is recommended to use the `bot.error()`, `bot.warn()`, `bot.info()`, and `bot.success()` functions instead.
- You can use `bot.COLORS.reset` to completely reset any formatting.
- You can use `bot.COLORS.normal_message` to format normal text in logs.
- `bot.COLORS.timestamp` exists as a color for the timestamps in front of a log message. You can use it to highlight any timestamps you may have.
### Changing Colors
Edit the following `class` in `main.py` to change colors.
![image](https://github.com/YumYummity/Guilded-Bot-Template/assets/103061664/2642ead3-3c6d-4b24-8a4f-918d5ca93908)


# Setup
1. Rename `config.json.txt` to `config.json`
2. Fill out `config.json`
3. Run `main.py`
