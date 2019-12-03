
import logging
import asyncio
import yaml
import discord
from discord.ext import commands
import os
from traceback import format_exception, format_exc
from datetime import datetime
from discord import ChannelType
'''Bot framework that can dynamically load and unload cogs.'''

config = yaml.safe_load(open('config.yml'))
secure = yaml.safe_load(open('secure.yml'))
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    config['prefix']),
    description='')

bot.loaded_cogs = []
bot.unloaded_cogs = []

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


def initLogging():
    logformat = "%(asctime)s %(name)s:%(levelname)s:%(message)s"
    logging.basicConfig(level=logging.INFO, format=logformat,
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.getLogger("discord").setLevel(logging.WARNING)
    return logging.getLogger("Datapunto Bot")

def check_if_dirs_exist():
    '''Function that creates the "cogs" directory if it doesn't exist already'''
    os.makedirs('cogs', exist_ok=True)

def load_autoload_cogs():
    '''
    Loads all .py files in the cogs subdirectory that are in the config file as "autoload_cogs" as cogs into the bot. 
    If your cogs need to reside in subfolders (ie. for config files) create a wrapper file in the cogs 
    directory to load the cog.
    '''
    for entry in os.listdir('cogs'):
        if entry.endswith('.py') and os.path.isfile('cogs/{}'.format(entry)) and entry[:-3] in config['autoload_cogs']:
            try:
                bot.load_extension("cogs.{}".format(entry[:-3]))
                bot.loaded_cogs.append(entry[:-3])
            except Exception as e:
                print(e)
            else:
                print('Succesfully loaded cog {}'.format(entry))

def get_names_of_unloaded_cogs():
    '''
    Creates an easy loadable list of cogs.
    If your cogs need to reside in subfolders (ie. for config files) create a wrapper file in the auto_cogs
    directory to load the cog.
    '''
    for entry in os.listdir('cogs'):
        if entry.endswith('.py') and os.path.isfile('cogs/{}'.format(entry)) and entry[:-3] not in bot.loaded_cogs:
            bot.unloaded_cogs.append(entry[:-3])

check_if_dirs_exist()
load_autoload_cogs()
get_names_of_unloaded_cogs()

@bot.command(aliases=['listcogs'])
async def list_cogs(ctx):
    '''Lists all cogs and their status of loading.'''
    cog_list = commands.Paginator(prefix='', suffix='')
    cog_list.add_line('**✅ Succesfully loaded:**')
    for cog in bot.loaded_cogs:
        cog_list.add_line('- ' + cog)
    cog_list.add_line('**❌ Not loaded:**')
    for cog in bot.unloaded_cogs:
        cog_list.add_line('- ' + cog)
    
    for page in cog_list.pages:
        await ctx.send(page)

@bot.command(pass_context=True)
async def textchannels(ctx):
    channels = (c.name for c in ctx.message.guild.channels if c.type==ChannelType.text)
    await ctx.send("\n".join(channels))

@bot.command()
async def close(self):
    await self.channels['bot-test'].send(f'We leaveing, bois')
    await asyncio.sleep(2)
    await super().close()

class Datapunto(commands.Bot):
    def __init__(self, command_prefix, description):
        super().__init__(command_prefix=command_prefix, description=description)
        
        self.startup = datetime.now()
        
        self.channels = {
            'wiiu-assistance-roleplay': None,
            '3ds-assistance-roleplay': None,
        }


        self.assistance_channels = {
         self.channels['3ds-assistance-roleplay'],
         self.channels['wiiu-assistance-roleplay'],
        }

    bot.load_extension("jishaku")

pic_ext = ['.jpg','.png','.jpeg']


async def on_error(self, event_method, *args, **kwargs):
    await self.channels['bot-err'].send(f'Error in {event_method}:')
    msg = format_exc()
    for chunk in [msg[i:i + 1800] for i in range(0, len(msg), 1800)]:
       await self.channels['bot-err'].send(f'```\n{chunk}\n```')

@bot.event
async def on_ready():
    print('----------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

bot.run(secure["token"])
