import asyncio
import discord
import sys
import math
import re

from subprocess import call
from discord.ext import commands
from cogs.checks import is_admin

class vcinjects(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None



    @commands.command()
    @is_admin()
    async def inesfix(self, ctx, filename=None):
        if filename is None:
            filename = ctx.message.attachments[0].filename

        attachment_url = ctx.message.attachments[0].url
        file_resp = await self.bot.aiosession.get(attachment_url)
        file = await file_resp.read()
        with open(filename, "wb") as f:
            f.write(file)
        try:
            f = open(filename)
            # Do something with the file
        finally:
            f.close()
        tmp = "`"
        tmp += filename
        tmp += "`"
        await ctx.send(tmp)

        await ctx.send(attachment_url)









def setup(bot):
    bot.add_cog(vcinjects(bot))


    