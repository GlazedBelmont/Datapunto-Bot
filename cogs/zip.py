import os
import zipfile
from discord.ext import commands
from discord.ext.commands import Cog
# from cogs.git import zipname

class Zip(Cog):
    def __init__(self, bot):
        self.bot = bot

    async def zipfile(path, ziph):
        for root, dirs, files in os.walk(path):
            for files in files:
                ziph.write(os.path.join(root, file))
        zipf = zipfile.ZipFile('example.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir('./GodMode9/',zipf)
        zipf.close()

def setup(bot):
    bot.add_cog(Zip(bot))
