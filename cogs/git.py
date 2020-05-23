import asyncio
import discord
import re
from subprocess import call
from discord.ext import commands
from cogs.checks import is_admin, check_admin, check_bot_or_admin



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
        git_clone_pksm = await self.bot.async_call_shell(
            "mkdir tmp_compile && "
            "cd tmp_compile && "
            "git clone --recursive https://github.com/FlagBrew/PKSM.git")
        with open(f"{self.bot.logs_dir}" + "git_clone_PKSM_log.txt", "a+",encoding="utf-8") as f:
            print(git_clone_pksm, sep="\n\n", file=f)

        commit_id = await self.bot.async_call_shell(
            "cd tmp_compile/PKSM && "
            "git rev-parse HEAD"
        )
        with open(f"{self.bot.logs_dir}" + "git_rev-parse_PKSM_log.txt", "a+",encoding="utf-8") as f:
            print(commit_id, sep="\n\n", file=f)
        
        await tmp.edit(content=f"```{git_clone_pksm}```")
        git_submodule_pksm = await self.bot.async_call_shell(
            "cd tmp_compile/PKSM && "
            "git submodule init && "
            "git submodule update"
        )

        await tmp.edit(content=f"```{git_submodule_pksm}```")
        await asyncio.sleep(2)
        await tmp.edit(content=f"Building...")
        
        git_make_pksm = await self.bot.async_call_shell(
            "cd tmp_compile/PKSM && "
            "make all && "
            "cd 3ds/out && "
            f"mkdir {self.bot.home_path}/tmp_compile/PKSM/out && "
            f"mv *.3dsx *.cia {self.bot.home_path}/tmp_compile/PKSM/out/ && "
            f"cd {self.bot.home_path}/tmp_compile/PKSM/out/ && "
            "zip -r PKSM_Latest.zip ./*"
        )
        with open(f"{self.bot.logs_dir}" + "git_make_PKSM_log.txt", "a+",encoding="utf-8") as f:
            print(git_make_pksm, sep="\n\n", file=f)
            print("_/\_/\_/\_/\_", sep="\n\n", file=f)
        
        await tmp.delete()
        await ctx.channel.send(content=f"Build completed.", file=discord.File(f'{self.bot.home_path}/tmp_compile/PKSM/out/PKSM_Latest.zip'))
        await self.bot.async_call_shell(f"cd tmp_compile && rm -rf PKSM")
        


    @commands.command()
    @commands.guild_only()
    @is_admin("Bot-Admin")
    async def commit(self, ctx):
        """Commit the latest changes to the repo"""
        if await intprompt("Commit?", 60.0):
           await ctx.send("Confirmed")
        else:
            await ctx.send("Cancelled")

    @is_admin("GlaZy")
    @commands.command()
    async def pull(self, ctx):
        """Pull the latest commit from the repo"""
        await ctx.send("Pulling changes...")
        call(['git', 'pull'])
        await ctx.send("👋 Restarting bot!")
        await self.bot.close() 

    @commands.command()
    @is_admin("Test-Admin")
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def compile(self, ctx, builddir, url, *, makecommand=""):
        """Compiles a repo from source
        Provide the github repo link, the build directory and the build command.
        Use */ to specify that the build directory is the current one.
        Submodules are automatically handled, don't bother with that.
        """
                            
        if makecommand == "":
            makecommand = "make"

        await ctx.send(f"{self.bot.escape_text(builddir)} is the building directory\n\n` {url} ` is the github repo's link\n\n{self.bot.escape_text(makecommand)} is the building command")

        if url[-4:] != ".git":
            name = url.split('/')[-1]
        else:
            name = url[:-4].split('/')[-1]

        await self.bot.change_presence(status="dnd")

        tmp = await ctx.send(f"**Compiling {self.bot.escape_text(name)}...**")
        git_output = await self.bot.async_call_shell(
            f'rm -r -f tmp_compile && '
            f'mkdir tmp_compile && '
            f'cd tmp_compile && '
            f'git clone {url} && '
            f'cd $(basename $_ .git){builddir} && '
            f'git submodule init && ' # just in case it's needed
            f'git submodule update && '
            f'{makecommand} && '
            f'zip -r {name}.zip ./*'
        )
        with open(f"{self.bot.logs_dir}" + "compile_log.txt", "a+",encoding="utf-8") as f:
            print(git_output, sep="\n\n", file=f)

        hasted_output = await self.bot.haste(git_output)
        await tmp.delete()
        await ctx.send(f"{name}'s compile log:\n{hasted_output}")

        try:
            await ctx.channel.send(content=f"Build completed.", file=discord.File(f'{self.bot.home_path}/tmp_compile/{name}/{name}.zip'))
        except FileNotFoundError:
            await ctx.send(f'`{self.bot.home_path}/tmp_compile/{name}/{name}.zip` does not exist.')
        finally:
            await self.bot.change_presence(status="online")
            cleaning_output = await self.bot.async_call_shell(
                'rm -r -f tmp_compile'
            )


    @commands.command()
    async def daedalus(self, ctx, customurl="https://github.com/masterfeizz/DaedalusX64-3DS.git"):
        """Builds the latest commit of DaedalusX64\nYou can provide your own fork link if it's a custom build"""

        await self.bot.change_presence(status="dnd")

        tmp = await ctx.send(f"**Compiling DaedalusX64...**")
        git_output = await self.bot.async_call_shell(
            f'rm -r -f tmp_compile && '
            f'mkdir tmp_compile && '
            f'cd tmp_compile && '
            f'git clone {customurl} && '
            f'cd $(basename $_ .git) && '
            f'git submodule init && ' # just in case it's needed
            f'git submodule update && '
            f'mv ./Source/SysCTR/Resources/romfs/ ./Source/SysCTR/Resources/RomFS && '
            f'chmod +x ./build_daedalus.sh && '
            f'./build_daedalus.sh CTR_RELEASE && '
        )
        with open(f"{self.bot.logs_dir}" + "dx643dscompile_log.txt", "a+",encoding="utf-8") as f:
            print(git_output, sep="\n\n", file=f)

        hasted_output = await self.bot.haste(git_output)
        await tmp.delete()
        await ctx.send(f"DaedalusX64's compile log:\n{hasted_output}")
        
        try:
            await ctx.channel.send(content=f"Build completed.", file=discord.File(f'{self.bot.home_path}/tmp_compile/DaedalusX64-3DS/daedbuild/DaedalusX64.3dsx'))
            await ctx.channel.send(file=discord.File(f'{self.bot.home_path}/tmp_compile/DaedalusX64-3DS/daedbuild/DaedalusX64.cia'))
        except FileNotFoundError:
            await ctx.send(f'`{self.bot.home_path}/tmp_compile/DaedalusX64-3DS/DaedalusX64.3dsx & DaedalusX64.cia` do not exist.')
        finally:
            await self.bot.change_presence(status="online")
            cleaning_output = await self.bot.async_call_shell(
                'rm -r -f tmp_compile'
            )

def setup(bot):
    bot.add_cog(git(bot))
