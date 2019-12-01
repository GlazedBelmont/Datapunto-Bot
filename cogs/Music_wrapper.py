def setup(bot):
    bot.load_extension("cogs.MusicPart.music")
    bot.load_extension("cogs.MusicPart.updater")

def teardown(bot):
    bot.unload_extension("cogs.MusicPart.music")
    bot.unload_extension("cogs.MusicPart.updater")
