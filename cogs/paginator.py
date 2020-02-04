# I just want to specify that I did not originally make this file, OneEyedKnight did and I modified it to my needs.
#
# - GlaZed_Belmont


# LIST
#
# 1 = Red = 0
# 2 = Blue = 1
# 3 = Yellow = 2
# 4 = Gold = 3
# 5 = Silver = 4
# 6 = Crystal = 5
# 7 = FireRed = 6
# 8 = LeafGreen = 7
# 9 = Ruby = 8
# 10 = Sapphire = 9
# 11 = Emerald = 10
#
#



import discord
import asyncio

from secret import games, romhacks_image, romhacks_files, romhacks

class Paginator:
    def __init__(self, ctx, embed=True):
        self.bot = ctx.bot
        self.ctx = ctx
        self.entries = games
        entries = games
#        self.image_url = image_url
        self.embed = embed
        self.max_pages = len(entries)-1
        self.msg = ctx.message
        self.paginating = True
        self.user_ = ctx.author
        self.channel = ctx.channel
        self.current = 0
        self.romhacks_files = romhacks_files
        self.sub_confirm = 0
#        self.current_romhack_file = self.current
        self.max_files = len(romhacks_files)-1
        self.clean = 0
        
        self.reactions = [('\N{BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR}', self.first_page),
                          ('\N{BLACK LEFT-POINTING TRIANGLE}', self.backward),
                          ('\N{BLACK RIGHT-POINTING TRIANGLE}', self.forward),
                          ('\N{BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR}', self.last_page),
                          ('\N{INPUT SYMBOL FOR NUMBERS}', self.selector),
                          ('\N{BLACK SQUARE FOR STOP}', self.stop),
                          ('\N{INFORMATION SOURCE}', self.info),
                          ('\N{BALLOT BOX WITH CHECK}', self.confirm)]

    async def setup(self):
        if self.embed is False:
            try:
                self.msg = await self.channel.send(self.entries[0])
            except AttributeError:
                await self.channel.send(self.entries)
        else:
            try:
                self.msg = await self.channel.send(embed=self.entries[0])
            except (AttributeError, TypeError):
                await self.channel.send(embed=self.entries)

        if len(self.entries) == 1:
            return

        for (r, _) in self.reactions:
            await self.msg.add_reaction(r)

    async def alter(self, page: int): # page is self.current
        try:
            if self.sub_confirm == 1:
                await self.msg.add_reaction('\N{LEFTWARDS ARROW WITH HOOK}')

            await self.msg.edit(embed=self.entries[page])
            if self.clean == 1 and self.sub_confirm == 0:
                await self.msg.clear_reactions()
                for (r, _) in self.reactions:
                    await self.msg.add_reaction(r)
                    self.clean -= 1
        except (AttributeError, TypeError):
            await self.msg.edit(content=self.entries[page])

    async def first_page(self):
        self.current = 0
#        self.current_romhack_file = 0
        await self.alter(self.current)

    async def backward(self):
        if self.current == 0:
            self.current = self.max_pages
            await self.alter(self.current)
        else:
            self.current -= 1
#            self.current_romhack_file -= 1
            await self.alter(self.current)

    async def forward(self):
        if self.current == self.max_pages:
            self.current = 0
            await self.alter(self.current)
        else:
            self.current += 1
            await self.alter(self.current)

    async def last_page(self):
        self.current = self.max_pages
#        self.current_romhack_file = self.max_files
        await self.alter(self.current)

    async def selector(self):
        def check(m):
            if m.author == self.user_:
                return True
            if m.message == self.msg:
                return True
            if int(m.content) > 1 <= self.max_pages+1:
                return True
            return False

        delete = await self.channel.send(f"Which page do you want to turn to? **1-{self.max_pages+1}?**")
        try:
            number = int((await self.bot.wait_for('message', check=check, timeout=60)).content)
        except asyncio.TimeoutError:
            return await self.ctx.send("You ran out of time.")
        else:    
            self.current = number - 1
#            self.current_romhack_file = number - 1
            await self.alter(self.current)
            await delete.delete()
            

    async def stop(self):
        try:
            await self.msg.clear_reactions()
        except discord.Forbidden:
            await self.msg.delete()

        self.paginating = False

    async def info(self):
        if self.entries == games:
            embed = discord.Embed()
            embed.set_author(name='Instructions')
            embed.description = "Hi! Please choose the game that you'd like!"

            embed.add_field(name="First Page ⏮", value="This reaction takes you to Pokemon Red.", inline=False)
            embed.add_field(name="Previous Page ◀", value="This reaction takes you to the previous game. "
                                                      "If you use this reaction while on Pokemon Red it will take"
                                                      "you to Pokemon Emerald.", inline=False)
            embed.add_field(name="Next Page ▶", value="This reaction takes you to the next game. "
                                                  "If you use this reaction while on Pokemon Emerald it will to take"
                                                  "you to Pokemon Red.", inline=False)
            embed.add_field(name="Last Page ⏭", value="This reaction takes you to Pokemon Emerald", inline=False)
            embed.add_field(name="Selector 🔢", value="This reaction allows you to choose what game to go to", inline=False)
            embed.add_field(name="Information ℹ", value="This reaction takes you to this page.")
            embed.add_field(name="Stop ⏹️", value="This reaction stops everything.")
            embed.add_field(name="Confirm ☑️", value="This reaction allows you to confirm your choice\nand see the romhacks for this game")
        else:
            embed = discord.Embed()
            embed.set_author(name='Instructions')
            embed.description = "Hi! Please choose the romhack that you'd like!" 

            embed.add_field(name="First Page ⏮", value="This reaction takes you to the first romhack.", inline=False)
            embed.add_field(name="Previous Page ◀", value="This reaction takes you to the previous romhack. "
                                                      "If you use this reaction while in the first romhack it will take"
                                                      "you to the last romhack.", inline=False)
            embed.add_field(name="Next Page ▶", value="This reaction takes you to the next romhack. "
                                                  "If you use this reaction while in the last romhack it will to take"
                                                  "you to the first romhack.", inline=False)
            embed.add_field(name="Last Page ⏭", value="This reaction takes you to the last romhack", inline=False)
            embed.add_field(name="Selector 🔢", value="This reaction allows you to choose what romhack to go to", inline=False)
            embed.add_field(name="Information ℹ", value="This reaction takes you to this page.")
            embed.add_field(name="Stop ⏹️", value="This reaction stops everything.")
        await self.msg.edit(embed=embed)

    def _check(self, reaction, user):
        if user.id != self.user_.id:
            return False

        if reaction.message.id != self.msg.id:
            return False

        for (emoji, func) in self.reactions:
            if reaction.emoji == emoji:
                self.execute = func
                return True
        return False

    async def confirm(self):
        if self.sub_confirm == 0:
            self.sub_confirm += 1
            await self.channel.send(f"You've chosen {self.current}")
            if self.current == 0: # Red
                self.entries =
            elif self.current == 1: # Blue
                self.entries
            elif self.current == 2: # Yellow
                self.entries
            elif self.current == 3: # Gold
                self.entries
            elif self.current == 4: # Silver
                self.entries
            elif self.current == 5: # Crystal 
                self.entries
            elif self.current == 6: # FireRed
                self.entries
            elif self.current == 7: # LeafGreen
                self.entries
            elif self.current == 8: # Ruby
                self.entries
            elif self.current == 9: # Sapphire
                self.entries
            elif self.current == 10: # Emerald
                self.entries
#            self.entries = romhacks # changes soon!!!!
            self.reactions.append(('\N{LEFTWARDS ARROW WITH HOOK}', self.go_back))
            self.current = 0
            await self.alter(self.current)
        else:
            
            try:
                await self.msg.clear_reactions()
                await self.channel.send(f"Confirmed\nHere you go!")
                file = discord.File(self.romhacks_files[self.current])
                await self.channel.send(file=file)
                return True
            except discord.Forbidden:
                await self.msg.delete()
        
    async def go_back(self):
        if self.sub_confirm == 1:
            self.sub_confirm -= 1
            self.entries = games
            self.reactions.remove(('\N{LEFTWARDS ARROW WITH HOOK}', self.go_back))
            self.current = 0
            self.clean += 1
            await self.alter(self.current)
        else:

            try:
                await self.channel.send("ok so this is not supposed to happen at ALL")
            except discord.Forbidden:
                await self.msg.delete()


#    async def switch(self):
#        try:
#            await self.msg.clear_reactions()
#            await self.channel.send("Confirmed")
#            await self.channel.send(self.current_image)
#            return True
#        except discord.Forbidden:
#            await self.msg.delete()




    async def paginate(self):
        perms = self.ctx.me.guild_permissions.manage_messages
        await self.setup()
        while self.paginating:
            if perms:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', check=self._check, timeout=120)
                except asyncio.TimeoutError:
                    return await self.stop()

                try:
                    await self.msg.remove_reaction(reaction, user)
                except discord.HTTPException:
                    pass

                await self.execute()
            else:
                done, pending = await asyncio.wait(
                    [self.bot.wait_for('reaction_add', check=self._check, timeout=120),
                     self.bot.wait_for('reaction_remove', check=self._check, timeout=120)],
                    return_when=asyncio.FIRST_COMPLETED)
                try:
                    done.pop().result()
                except asyncio.TimeoutError:
                    return self.stop

                for future in pending:
                    future.cancel()
                await self.execute()
