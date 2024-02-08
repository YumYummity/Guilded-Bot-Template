[Overview](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/README.md) / **Setup** / [Cogs](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/COGS/COGS.md) / [Logging](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/logs/LOGGING.md) / [Examples](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/EXAMPLES.md)

# Setup
## Getting Files
### Git Clone
1. Make sure you have [Git](https://git-scm.com/downloads) installed
2. Run `git clone https://github.com/YumYummity/guilded-bot-template`

### ZIP
You can download this repository as a .zip file by using this link: https://github.com/YumYummity/guilded-bot-template/archive/refs/heads/main.zip
1. Download the file using the link above
2. Extract the file with your preferred application

## With Files
1. Rename `config.json.txt` to `config.json`
2. Fill out `config.json`, replacing the necessary values
3. Ensure you have the required version of Python with `python3 --version` (or `python --version`)
    - This should be at least 3.7.*
4. Install the required libraries. `pip install -r requirements.txt`
5. Run `main.py`

### Optional
You can read [Command Examples](https://github.com/YumYummity/Guilded-Bot-Template/blob/main/EXAMPLES/COMMANDS/COMMANDS.md) to see some pre-built commands. These also come with a related guide.

### Debug Mode
You can change the variable `debug_mode` in `main.py` to turn on `guilded.py` debug.