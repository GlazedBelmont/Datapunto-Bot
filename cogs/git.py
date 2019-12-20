import asyncio
import discord
import re
from subprocess import call
from discord.ext import commands
from cogs.checks import on_reaction_add

class git(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None

#    @commands.guild_only()
#    @commands.command()
#    async def gm9(self, ctx, auto=False):
#        tmp = await ctx.send('Compiling...')
#        git_output_gm9 = await self.bot.async_call_shell("git clone https://github.com/d0k3/GodMode9.git && cd GodMode9 && make release && cd output && zip -r Godmode9.zip ./*.firm")
#        await tmp.delete()
#        await ctx.channel.send(content=f"Build completed.", file=discord.File('/home/glazed/DatapuntoBot/GodMode9/output/Godmode9.zip'))
#        await self.bot.async_call_shell(f"rm -rf GodMode9")

#    @commands.guild_only()
#    @commands.command()
#    async def delete(self, ctx, *, args):
#        if args == "godmode9":
#            folder = 'GodMode9'
#            tmp = await ctx.send("oh yea boi")
#            git_output_clear = await self.bot.async_call_shell(f"rm -rf {folder}")
#            await tmp.edit(content=f"{folder} was deleted")
            
#        elif args != "godmode9":
#            await ctx.send("just shut up")
    
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
        
        await tmp.delete()
        await ctx.channel.send(content=f"Build completed.", file=discord.File(f'/home/glazed/DatapuntoBot/PKSM/out/PKSM_Latest.zip'))
        await self.bot.async_call_shell(f"rm -rf PKSM")
        


    @commands.command()
    @commands.guild_only()
    @commands.has_role(575834911425167414)
    async def commit(self, ctx, message =""):
        """Commit the latest changes to the repo"""
        tmp = await ctx.send('Commiting...')
        emote = '\N{HOURGLASS}'
        await ctx.message.add_reaction('\N{HOURGLASS}')
        if await on_reaction_add(reaction, user) is True:
            await ctx.send("nice")
        else:
            await tmp.edit(content=f'oh well, it didnt work')



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
    @commands.has_role(617476156148547619)
#   @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def compile(self, ctx, builddir, url, *, makecommand):
        """Compiles a repo from source\nProvide the .git link, the build directory and the build command"""
                               
        if builddir is None:
            builddir = "*/"
            await ctx.send("a")
            return
        if url is None:
            await ctx.send("No URL")
    #        url = None
        if not re.search(".git", url, re.IGNORECASE):
            await ctx.send("Please provide a .git link please")

        if makecommand is None:
            makecommand = make
            await ctx.send("aa")
            return
        await ctx.send(f"{builddir} is the building directory\n\n{url} is the github repo's link\n\n{makecommand} is the building command")    
        git_output = await self.bot.async_call_shell(
            f'git clone {url} && '
            f'cd $(basename $_ .git){builddir} && '
             'pwd'
        #    'basename `git rev-parse --show-toplevel`'
        )
        with open("compile_log.txt", "a+",encoding="utf-8") as f:
            print(git_output, sep="\n\n", file=f)


        await ctx.send(f'{git_output}')

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
