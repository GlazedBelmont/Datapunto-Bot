# I just want to specify that I did not originally make this file, OneEyedKnight did and I modified it to my needs.
#
# - GlaZed_Belmont


# LIST

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
import os
import zipfile
import re

from zipfile import ZipFile

#from secret import games, romhacks_image, romhacks_files, romhacks, Red_romhacks, Blue_romhacks, Yellow_romhacks, Gold_romhacks, Silver_romhacks, Crystal_romhacks, FireRed_romhacks, LeafGreen_romhacks, Ruby_romhacks, Sapphire_romhacks, Emerald_romhacks
from secret import *


class Paginator:
    def __init__(self, ctx, debug=True, embed=True): # Omit entries so we can define them here
        self.debug = debug
        self.bot = ctx.bot
        self.ctx = ctx
        self.entries = games # Basically the initial pool of elements
        entries = games
#        self.image_url = image_url
        self.embed = embed
        self.max_pages = len(entries)-1
        self.msg = ctx.message
        self.paginating = True
        self.user_ = ctx.author # Who can use the prompt
        self.channel = ctx.channel # Where to post it
        self.current = 0 # Make sure we are at the first choice
        self.romhacks_files = romhacks_files # Just in case
        self.sub_confirm = 0 # Set to 0 since we are initially on first bank
#        self.current_romhack_file = self.current
        self.max_files = len(romhacks_files)-1
        self.bank = 0
        self.clean = 0 # 0 will keep reactions, 1 will clear them
        self.games_names = ['Red', 'Blue', 'Yellow', 'Gold', 'Silver',
                            'Crystal', 'FireRed', 'LeafGreen', 'Ruby',
                            'Sapphire', 'Emerald']
        self.tmp = ""

        
        self.reactions = [('\N{BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR}', self.first_page),
                          ('\N{BLACK LEFT-POINTING TRIANGLE}', self.backward),
                          ('\N{BLACK RIGHT-POINTING TRIANGLE}', self.forward),
                          ('\N{BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR}', self.last_page),
                          ('\N{INPUT SYMBOL FOR NUMBERS}', self.selector),
                          ('\N{BLACK SQUARE FOR STOP}', self.stop),
                          ('\N{INFORMATION SOURCE}', self.info),
                          ('\N{BALLOT BOX WITH CHECK}', self.confirm)]

    async def setup(self):
        if self.embed is False: # Will send text
            try:
                self.msg = await self.channel.send(self.entries[0])
            except AttributeError:
                await self.channel.send(self.entries)
        else: # Will send embeds 
            try:
                self.msg = await self.channel.send(embed=self.entries[0]) # the choice 0 of self.entries
                if self.debug is True:
                    await self.channel.send("**__DEBUG IS ON__**")
            except (AttributeError, TypeError):
                await self.channel.send(embed=self.entries)

        if len(self.entries) == 1: # Will not add reactions if we only have 1 entries
            return

        for (r, _) in self.reactions: # r is reactions, _ is their function
            await self.msg.add_reaction(r)

    async def alter(self, page: int): # page is self.current
        try:
            if self.sub_confirm == 1:
                await self.msg.add_reaction('\N{LEFTWARDS ARROW WITH HOOK}')

            await self.msg.edit(embed=self.entries[page]) # Change the current option
            
            if self.clean == 1 and self.sub_confirm == 0: # if you came back from a romhacks page
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
        if self.current == self.max_pages: # Return to first choice if we hit the last one
            self.current = 0
            await self.alter(self.current)
        else: 
            self.current += 1
            await self.alter(self.current) # Simply execute the alter function to change the option

    async def last_page(self):
        self.current = self.max_pages # Set the value to the last option
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
            number = int((await self.bot.wait_for('message', check=check, timeout=60)).content) # Wait for reaction
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
        else: # basically if self.entries != games, aka if they are romhacks.
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
        if user.id != self.user_.id: # if the user who reacted is the user who initiated the prompt
            return False

        if reaction.message.id != self.msg.id: # if the post who got a reaction is the prompt
            return False

        for (emoji, func) in self.reactions:
            if reaction.emoji == emoji: # if a emoji in self.reactions was used
                self.execute = func # set its action to self.execute
                return True
        return False # if the emoji isnt in self.reactions

    async def confirm(self):
        if self.sub_confirm == 0: # if you were on the games prompt
            self.sub_confirm += 1
            self.bank = self.current # Stores which game you chose, kinda weird but don't worry about it, since there was no efficient way to do it instead.
            self.tmp = await self.channel.send(f"You've chosen Pokemon {self.games_names[self.current]}")

            if self.current == 0: # Red
                self.entries = Red_romhacks
            elif self.current == 1: # Blue
                self.entries = Blue_romhacks
            elif self.current == 2: # Yellow
                self.entries = Yellow_romhacks
            elif self.current == 3: # Gold
                self.entries = Gold_romhacks
            elif self.current == 4: # Silver
                self.entries = Silver_romhacks
            elif self.current == 5: # Crystal 
                self.entries = Crystal_romhacks
            elif self.current == 6: # FireRed
                self.entries = FireRed_romhacks
            elif self.current == 7: # LeafGreen
                self.entries = LeafGreen_romhacks
            elif self.current == 8: # Ruby
                self.entries = Ruby_romhacks
            elif self.current == 9: # Sapphire
                self.entries = Sapphire_romhacks
            elif self.current == 10: # Emerald
                self.entries = Emerald_romhacks
#            self.entries = romhacks # changes soon!!!!
            self.reactions.append(('\N{LEFTWARDS ARROW WITH HOOK}', self.go_back))
            self.current = 0
            await self.alter(self.current)
        else: # if you chose a romhack
            
            try:
                selected_hack = self.romhacks_files[self.bank][self.current]
                name = selected_hack.split('/')[3]

                if name.split('.')[1] == "gb":
                    extension = 3 # .gb
                else:
                    extension = 4 # .gbc or .gba
                
                path = selected_hack[:-extension]
                    
                await self.tmp.edit(content=f"\nYou have chosen {name[:-extension]}")
                await self.msg.clear_reactions()
                
                file = discord.File(selected_hack) # that part will need to be changed so it sends the correct romhack file from the correct game, Done! :D

                def convert_bytes(num):
                    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                        if num < 1024.0:
                            return "%3.1f %s" % (num, x)
                        num /= 1024.0

                filesize = os.path.getsize(selected_hack)
                conversion = convert_bytes(filesize)

                if self.debug is True:
                    await self.channel.send(f'``{filesize} bytes\n{conversion}``') # For debug purposes
                

                if filesize < 8400000:
                    await self.channel.send(f"Confirmed\nHere you go!")
                    await self.channel.send(file=file)
                    return True

                else:
                    await self.channel.send(f"The file is {filesize - 8400000} bytes too big, the file will be zipped")
                
                if self.debug is True:
                    await self.channel.send(path)

                    ZipFile(f"{path}.zip", 'w', zipfile.ZIP_BZIP2, 9).write(selected_hack)
                    file = discord.File(f"{path}.zip")

                    if os.path.getsize(f"{path}.zip") > 8400000:
                        await self.channel.send(f"The file is {convert_bytes(os.path.getsize(f'{path}.zip') - 8400000)} too big, an alternative will be implemented soon")
                    else:    
                        await self.channel.send(f"Confirmed\nHere you go!")
                        await self.channel.send(file=file)
                        return True
                    
                    await self.go_back()

            except discord.Forbidden:
                await self.msg.delete()
        
    async def go_back(self):
        if self.sub_confirm == 1: # checks if you were on a romhacks page
            self.sub_confirm -= 1
            self.entries = games
            self.reactions.remove(('\N{LEFTWARDS ARROW WITH HOOK}', self.go_back))
            self.current = 0
            self.clean += 1 # that way self.alter will clear reactions so the part below is impossible
            await self.tmp.delete()
            await self.alter(self.current)
        else: # Shouldn't happen because the button isnt supposed to appear on the games prompt'

            try:
                await self.channel.send("ok so this is not supposed to happen at ALL")
            except discord.Forbidden:
                await self.msg.delete()


#    async def switch(self):    # Not going to be used because thumbnails turned out to work
#        try:
#            await self.msg.clear_reactions()
#            await self.channel.send("Confirmed")
#            await self.channel.send(self.current_image)
#            return True
#        except discord.Forbidden:
#            await self.msg.delete()




    async def paginate(self):
        perms = self.ctx.me.guild_permissions.manage_messages # so the check for perms below will work
        await self.setup() # Setup the prompt
        while self.paginating:
            if perms: # Do we have perms?
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', check=self._check, timeout=120)
                except asyncio.TimeoutError:
                    return await self.stop()

                try:
                    await self.msg.remove_reaction(reaction, user) # remove the inputted reaction
                except discord.HTTPException:
                    pass

                await self.execute() # Execute what the inputted reaction does
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
