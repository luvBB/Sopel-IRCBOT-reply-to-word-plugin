from __future__ import absolute_import, division, print_function, unicode_literals

from sopel.plugin import find

@find(r"who's my love\?")
def finder(bot, trigger):
    if trigger.nick == "JigSaw":
        bot.say(r"It's droops16... you idiot!")

@find(r"JigSaw")
def finder1(bot, trigger):
    if trigger.nick == "droops16":
        bot.say(r"Ce JigSaw visezi? Poate voiai sa spui my love, my BB, my life, etc...")

@find(r"noapte buna")
def finder2(bot, trigger):
    if trigger.nick == "droops16":
        bot.say(r"Noapte buna si tie! :D")

@find(r"buna dimineata")
def finder3(bot, trigger):
    if trigger.nick == "droops16":
        bot.say(r"Buna dimineata soare!")
