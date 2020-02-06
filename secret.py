import discord
import io
import aiohttp

        
# https://discordpy.readthedocs.io/en/latest/api.html#embed


games = []
romhacks_image = []
romhacks_files = []
romhacks = []

# Games_Romhacks
Red_romhacks = []
Blue_romhacks = []
Yellow_romhacks = []
Gold_romhacks = []
Silver_romhacks = []
Crystal_romhacks = []
FireRed_romhacks = []
LeafGreen_romhacks = []
Ruby_romhacks = []
Sapphire_romhacks = []
Emerald_romhacks = []

# Games_Romhacks
Red_romhacks_files = []
Blue_romhacks_files = []
Yellow_romhacks_files = []
Gold_romhacks_files = []
Silver_romhacks_files = []
Crystal_romhacks_files = []
FireRed_romhacks_files = []
LeafGreen_romhacks_files = []
Ruby_romhacks_files = []
Sapphire_romhacks_files = []
Emerald_romhacks_files = []



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
"""Gold"""
Prism =  discord.Embed(title='Pokemon Prism',
        description = f"Hello, we are on page 1").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/FireRed/Gaia.jpeg")

"""FireRed"""
Gaia =  discord.Embed(title='Pokemon Gaia',
        description = f"Hello, we are on page 1").set_thumbnail(url="https://raw.githubusercontent.com/Datagame-Community/Datapunto-DB/master/FireRed/Gaia.jpeg")




#Entries_files:
"""Gold"""
Prism_file = "utils/romhacks_files/Gold/Pokemon Prism.gbc"
"""FireRed"""
Gaia_file = "utils/romhacks_files/FireRed/Pokemon Gaia.gba" #utils/romhacks_files/Pokemon_VietCristal.ips"

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
Gold_romhacks.append(Prism)
"""Silver"""

"""Crystal"""

"""FireRed"""
FireRed_romhacks.append(Gaia)

"""LeafGreen"""

"""Ruby"""

"""Sapphire"""

"""Emerald"""


#Entries_romhacks_files append:
"""Red"""

"""Blue"""

"""Yellow"""

"""Gold"""
Gold_romhacks_files.append(Prism_file)
"""Silver"""

"""Crystal"""

"""FireRed"""
FireRed_romhacks_files.append(Gaia_file)

"""LeafGreen"""

"""Ruby"""

"""Sapphire"""

"""Emerald"""


# Shitty test
romhacks_files.append(Red_romhacks_files)
romhacks_files.append(Blue_romhacks_files)
romhacks_files.append(Yellow_romhacks_files)
romhacks_files.append(Gold_romhacks_files)
romhacks_files.append(Silver_romhacks_files)
romhacks_files.append(Crystal_romhacks_files)
romhacks_files.append(FireRed_romhacks_files)
romhacks_files.append(LeafGreen_romhacks_files)
romhacks_files.append(Ruby_romhacks_files)
romhacks_files.append(Sapphire_romhacks_files)
romhacks_files.append(Emerald_romhacks_files)
