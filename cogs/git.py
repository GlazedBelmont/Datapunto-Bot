import asyncio
import discord
from subprocess import call
from discord.ext import commands

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
        
    @commands.command()
    async def pull(self, ctx):
        await ctx.send("Pulling changes...")
        call(['git', 'pull'])
        await ctx.send("👋 Restarting bot!")
        await self.bot.close() 
        
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def devkitarm(self, ctx, auto=False):
        tmp = await ctx.send('doing the shit...')

        echo_devkitarm = await self.bot.async_call_shell("echo $PATH && which python3")
        with open("echo_devkitarm_log.txt", "a+",encoding="utf-8") as f:
            print(echo_devkitarm, sep="\n\n", file=f)
        await tmp.delete()
        await ctx.channel.send(f"```peepee\n\n{echo_devkitarm}```")

        
        

def setup(bot):
    bot.add_cog(git(bot))
