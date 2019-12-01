import asyncio
import discord
from discord.ext import commands

class wget(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None

    @commands.guild_only()
    @commands.command()
    async def gm9(self, ctx):
        tmp = await ctx.send('Fetching the latest commit...')
        wget_output_gm9 = await self.bot.async_call_shell("mkdir GodMode9 && cd GodMode9 && wget -O 'GodMode9_Latest.zip' http://d0k3.secretalgorithm.com/GodMode9/latest.zip")
        await tmp.delete()
        await ctx.channel.send(content=f"Here you go! <:blobaww:569934894952611851> ", file=discord.File('/home/glazed/DatapuntoBot/GodMode9/GodMode9_Latest.zip'))
        wget_output_clear = await self.bot.async_call_shell(f"rm -rf GodMode9")


def setup(bot):
    bot.add_cog(wget(bot))
