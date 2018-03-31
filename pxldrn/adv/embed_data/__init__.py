import discord
from pxldrn.adv import sysinfo

def system_info():
    sysembed = discord.Embed(
        title="System Info",
        description="Hier siehst du alle System-Infos",
        color=0x128f24
    )
    sysembed.add_field(
        name="CPU Temperatur",
        value=sysinfo.getCPUtemp()
    )
    sysembed.add_field(
        name="CPU Nutzung",
        value=sysinfo.getCPUuse()
    )
    sysembed.add_field(
        name="RAM Auslastung",
        value="Belegt: {0} KB\nFrei: {1} KB\nGesamt: {2} KB".format(sysinfo.getRAMinfo()[1], sysinfo.getRAMinfo()[2], sysinfo.getRAMinfo()[0])
    )
    return sysembed


def py_help():
    pyemb = discord.Embed(
        title="Python lernen.",
        color=0xf8dc2e,
        description="Es scheint so, dass jemand hier zu viele Fragen über Python und vielleicht"
                    " auch discord.py stellt."
    )
    pyemb.set_author(name="Pixeldrohne")
    pyemb.set_footer(text='"Intelligenz ist die Fähigkeit, sich dem Wandel anzupassen." - Stephen Hawking')
    pyemb.set_thumbnail(url="https://www.python.org/static/opengraph-icon-200x200.png")
    pyemb.add_field(name="Tutorials:", value="https://www.python-kurs.eu/index.php\n"
                                             "http://py-tutorial-de.readthedocs.io/de/python-3.3/\n"
                                             "http://praxistipps.chip.de/python-tutorial-auf-deu"
                                             "tsch-fuer-einsteiger_93386")
    pyemb.add_field(name="Bücher:", value="https://www.rheinwerk-verlag.de/einstieg-in-python_4374/\n"
                                          "https://www.rheinwerk-verlag.de/programmieren-lernen-mit-python_3674/\n")
    pyemb.add_field(name="Videos:", value="https://www.youtube.com/watch?v=bt_Wcp3qemM\n"
                                          "https://www.youtube.com/watch?v=dG0kxa0XoXc\n"
                                          "https://www.youtube.com/watch?v=ikuyDZNsbNk")
    pyemb.add_field(name="discord.py", value="https://www.youtube.com/channel/UCisqgTzV--rB_WByK-wuY6g\n"
                                             "https://discordpy.readthedocs.io/en/latest/api.html#client")
    return pyemb


def about():
    abemb = discord.Embed(
        color=0xad1457,
        title="Über",
        description="Sorry, hier gibt es noch nichts zu sehen.")
    return abemb


def server_invite():
    embed = discord.Embed(
        title="Invite zum Heimat-/Testserver",
        description="http://discord.gg/sgDQjeH",
        color=0x8a2be2
    )
    return embed


def bot_invite():
    iembed = discord.Embed(
        title="Einfach dem Link folgen um den Bot einzuladen.",
        description="http://pixeldrohne.mystic-alchemy.com",
        color=0x8a2be2
    )
    return iembed