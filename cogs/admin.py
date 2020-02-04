import asyncio
import discord
from subprocess import call
from discord.ext import commands
from cogs.checks import is_admin, prompt


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None



    @is_admin()
    @commands.command(aliases = ['reboot', 'restart'])
    async def close(self, ctx):
        await ctx.channel.send("Ah shit, here we go again")
        await self.bot.close()

    @commands.command(hidden=True)
    @commands.has_role(575834911425167414)
    async def fullclose(self, ctx):
        await self.bot.async_call_shell("")

    @commands.command()
    async def guildleave(self, ctx, serverid: int):
        server = self.bot.get_guild(serverid)
        await ctx.send(f"{server}")

        if server not in self.bot.guilds:
            await ctx.send("I'm not even in this server apparently")
            return
        else:
            if serverid is None:
                server = self.bot.get_guild(ctx.guild.id)

        if server != self.bot.get_guild(554178232531025940) and server != self.bot.get_guild(632566001980145675):
            await ctx.send(f"I'll be leaving {server}")

            if await prompt(self, ctx, "Continue?"):
                return
            await ctx.send(f"I have left {server}")
            await server.leave()
                
        else:
            await ctx.send(f"I cannot leave `{server}`\nIt's my home <:blobaww:569934894952611851>")
        
    @commands.command()
    async def guildtest(self, ctx):
        msg = "```"
        for guild in self.bot.guilds:
            msg += f"{guild}\n"
        msg += "```"
        await ctx.send(msg)
        

    @commands.command()
    async def prompttest(self, ctx):
        if await prompt(self, ctx, "Am I a good bot?"):
            return
        await ctx.send("<:blobaww:569934894952611851>")
        
def setup(bot):
    bot.add_cog(admin(bot))
