import asyncio
import discord
import re
from subprocess import call
from discord.ext import commands
from cogs.checks import is_admin, check_admin, check_bot_or_admin

git_blacklist = [
    'ls',
    'cat',
    'rm',
    'rmdir',
    'curl',
    'pip',
    'wget',
    'aplay',
]

class git(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None
    

    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=600.0, type=commands.BucketType.channel)
    async def pksm(self, ctx, auto=False):
        """Compiles the latest commit of PKSM"""
        tmp = await ctx.send('Cloning...')

        git_clone_pksm = await self.bot.async_call_shell("git clone --recursive https://github.com/FlagBrew/PKSM.git")
        with open("git_clone_PKSM_log.txt", "a+",encoding="utf-8") as f:
            print(git_clone_pksm, sep="\n\n", file=f)

        commit_id = await self.bot.async_call_shell(
            "cd PKSM && "
            "git rev-parse HEAD"
        )
        with open("git_rev-parse_PKSM_log.txt", "a+",encoding="utf-8") as f:
            print(commit_id, sep="\n\n", file=f)
        
        await tmp.edit(content=f"```{git_clone_pksm}```")
        git_submodule_pksm = await self.bot.async_call_shell(
            "cd PKSM && "
            "git submodule init && "
            "git submodule update"
        )

        await tmp.edit(content=f"```{git_submodule_pksm}```")
        await asyncio.sleep(2)
        await tmp.edit(content=f"Building...")
        
        git_make_pksm = await self.bot.async_call_shell(
            "cd PKSM && "
            "make all && "
            "cd 3ds/out && "
            "mv *.3dsx *.cia /home/glazed/DatapuntoBot/PKSM/out/ && "
            "cd /home/glazed/DatapuntoBot/PKSM/out && "
            "zip -r PKSM_Latest.zip ./*"
        )
        with open("git_make_PKSM_log.txt", "a+",encoding="utf-8") as f:
            print(git_make_pksm, sep="\n\n", file=f)
            print("_/\_/\_/\_/\_", sep="\n\n", file=f)
        
        await tmp.delete()
        await ctx.channel.send(content=f"Build completed.", file=discord.File(f'/home/glazed/DatapuntoBot/PKSM/out/PKSM_Latest.zip'))
        await self.bot.async_call_shell(f"rm -rf PKSM")
        


    @commands.command()
    @commands.guild_only()
    @is_admin()
    async def commit(self, ctx):
        """Commit the latest changes to the repo"""
        if await intprompt("Commit?", 60.0):
           await ctx.send("Confirmed")
        else:
            await ctx.send("Cancelled")


    @commands.command()
    async def pull(self, ctx):
        """Pull the latest commit from the repo"""
        await ctx.send("Pulling changes...")
        call(['git', 'pull'])
        await ctx.send("👋 Restarting bot!")
        await self.bot.close() 


    @commands.guild_only()
    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def devkitarm(self, ctx, auto=False):
        tmp = await ctx.send('doing the shit...')

        echo_devkitarm = await self.bot.async_call_shell("echo $DEVKITARM")
        with open("echo_devkitarm_log.txt", "a+",encoding="utf-8") as f:
            print(echo_devkitarm, sep="\n\n", file=f)
        await tmp.delete()
        await ctx.channel.send(f"```peepee\n\n{echo_devkitarm}```")

    @commands.command()
    @is_admin()
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def compile(self, ctx, builddir, url, *, makecommand=None):
        """Compiles a repo from source
        Provide the github repo link, the build directory and the build command.
        Use */ to specify that the build directory is the current one.
        Submodules are automatically handled, don't bother with that.
        """
                            
        if makecommand is None:
            makecommand = "make"
        def check(git_blacklist, makecommand):
            return {x in git_blacklist} & {makecommand}
            
        if str(git_blacklist) in makecommand:
            await ctx.send("you motherfucker")

        await ctx.send(f"{builddir} is the building directory\n\n` {url} ` is the github repo's link\n\n{makecommand} is the building command")

        if url[-4:] != ".git":
            name = url[19:].split('/')[1]
        else:
            name = url[19:-4].split('/')[1]
        
        tmp = await ctx.send(f"**Compiling {name}...**")
        git_output = await self.bot.async_call_shell(
            f'rm -r -f tmp_compile && '
            f'mkdir tmp_compile && '
            f'cd tmp_compile && '
            f'git clone {url} && '
            f'cd $(basename $_ .git){builddir} && '
            f'git submodule init &&' # just in case it's needed
            f'git submodule update &&'
            f'{makecommand} && '
            f'zip -r {name}.zip ./*'
        )
        with open("compile_log.txt", "a+",encoding="utf-8") as f:
            print(git_output, sep="\n\n", file=f)

        hasted_output = await self.bot.haste(git_output)
        await tmp.delete()

        await ctx.send(f"{name}'s compile log:\n{hasted_output}")
        await ctx.channel.send(content=f"Build completed.", file=discord.File(f'/home/glazed/DatapuntoBot//tmp_compile/{name}/{name}.zip'))
        cleaning_output = await self.bot.async_call_shell(
            'rm -r -f tmp_compile'
        )

    #@commands.command()
    #async def compile2(self, ctx, url, buildfilepattern, *, makecommand="make"):
    #    tmp = await ctx.send('Cloning...')

    #    name = url[19:-4].split('/')[1]
    #    if url[:19] != "https://github.com/" or url[-4:] != ".git" or name == "":
    #        await tmp.edit(content=f"Bad URL")
    #        return

    #    git_clone = await self.bot.async_call_shell("git clone --recursive --recurse-submodules %s" % url)
    #    with open("git_clone_log.txt", "a+",encoding="utf-8") as f:
    #        print(git_clone, sep="\n\n", file=f)

    #    commit_id = await self.bot.async_call_shell(
    #    "cd %s && "
    #    "git rev-parse HEAD" % name
    #    )
    #    with open("git_rev-parse_log.txt", "a+",encoding="utf-8") as f:
    #        print(commit_id, sep="\n\n", file=f)

    #    await tmp.edit(content=f"```{git_clone}```")

    #    git_make = await self.bot.async_call_shell(
    #    "cd %s && "
    #    "mkdir DataPunto_out && "
    #    "mv %s DataPunto_out/ && "
    #    "zip -r DataPunto_out.zip DataPunto_out/" % (name, buildfilepattern)
    #    )
    #    with open("git_make_log.txt", "a+",encoding="utf-8") as f:
    #        print(git_make, sep="\n\n", file=f)

    #    await tmp.delete()
    #    await ctx.channel.send(content=f"Build completed.", file=discord.File(f'DataPunto_out.zip'))
#       await self.bot.async_call_shell(f"cd .. && rm -rf %s" % name)
        

def setup(bot):
    bot.add_cog(git(bot))
