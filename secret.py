import discord
import io
import aiohttp

        
# https://discordpy.readthedocs.io/en/latest/api.html#embed


games = []
romhacks_image = []
romhacks_files = []
romhacks = []

# Entries:

Red =  discord.Embed(title='Pokemon Red',
        description = f"Hello, we are on page 1").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/Red.png")

Blue =  discord.Embed(title='Pokemon Blue',
        description = f"Hello, we are on page 2").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/Blue.png")

Yellow =  discord.Embed(title='Pokemon Yellow',
        description = f"Hello, we are on page 3").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/Yellow.png")

Gold =  discord.Embed(title='Pokemon Gold',
        description = f"Hello, we are on page 4").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/Gold.png")

Silver =  discord.Embed(title='Pokemon Silver',
        description = f"Hello, we are on page 5").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/Silver.png")

Crystal =  discord.Embed(title='Pokemon Crystal',
        description = f"Hello, we are on page 6").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/Crystal.png")

FireRed =  discord.Embed(title='Pokemon FireRed',
        description = f"Hello, we are on page 7").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-Bot-DB/master/FireRed.png")

LeafGreen =  discord.Embed(title='Pokemon LeafGreen',
        description= f"Hello, we are on page 8").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-Bot-DB/master/LeafGreen.png")

Ruby =  discord.Embed(title='Pokemon Ruby',
        description= f"Hello, we are on page 9").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-Bot-DB/master/Ruby.png")

Sapphire =  discord.Embed(title='Pokemon Sapphire',
        description=f"Hello, we are on page 10").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-Bot-DB/master/Sapphire.png")

Emerald =  discord.Embed(title='Pokemon Emerald',
        description=f"Hello, we are on page 11").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-Bot-DB/master/Emerald.png")



# Entries_image:
romhack1_image = "https://i.imgur.com/TgdOPkG.png"
romhack2_image = "https://cdn.discordapp.com/attachments/559035031172153354/673564418356936760/PokecordSpawn.jpg"


#Entries_romhacks:
"""FireRed"""
Gaia =  discord.Embed(title='Pokemon Gaia',
        description = f"Hello, we are on page 1").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/FireRed/Gaia.jpeg")




#Entries_files:
"""FireRed"""
Gaia_file = "/home/glazed/DatapuntoBot/utils/romhacks_files/Pokemon Gaia.ips" #utils/romhacks_files/Pokemon_VietCristal.ips"

romhack2_file = "/home/glazed/DatapuntoBot/git_clone_PKSM_log.txt"

romhack3_file = "/home/glazed/DatapuntoBot/git_make_log.txt"

romhack4_file = "/home/glazed/DatapuntoBot/git_make_log.txt"

romhack5_file = "/home/glazed/DatapuntoBot/git_rev-parse_log.txt"

# Entries append:
games.append(Red)

games.append(Blue)

games.append(Yellow)

games.append(Gold)

games.append(Silver)

games.append(Crystal)

games.append(FireRed)

games.append(LeafGreen)

games.append(Ruby)

games.append(Sapphire)

games.append(Emerald)

# Entries_image append: (Useless for now)
romhacks_image.append(romhack1_image)
romhacks_image.append(romhack2_image)


#Entries_romhacks append:
"""Red"""

"""Blue"""

"""Yellow"""

"""Gold"""

"""Silver"""

"""Crystal"""

"""FireRed"""
romhacks.append(Gaia)

"""LeafGreen"""

"""Ruby"""

"""Sapphire"""

"""Emerald"""

#Entries_files append:
romhacks_files.append(Gaia_file)
romhacks_files.append(romhack2_file)
romhacks_files.append(romhack3_file)
romhacks_files.append(romhack4_file)
romhacks_files.append(romhack5_file)