import importlib
import logging
import os
import sys
from pathlib import Path

from Aniebots import *
from Aniebots.config import *
from Aniebots.helpers import *
from Aniebots.utils import *

# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from Meowbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import Meowbot.utils

        path = Path(f"Meowbot/plugins/{shortname}.py")
        name = "Aniehots.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Aniebots - Successfully imported " + shortname)
    else:
        import Aniebots.utils

        path = Path(f"Aniebots/plugins/{shortname}.py")
        name = "Meowbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = Aniebots.utils
        mod.Config = Config
        mod.borg = bot
        mod.Meowbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_mew = delete_mew
        mod.eod = delete_mew
        mod.Var = Config
        mod.admin_cmd = mew_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = Aniebots.utils
        sys.modules["userbot"] = Aniebots 
        # support for paperplaneextended
        sys.modules["userbot.events"] = Meowbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["Aniebots.plugins." + shortname] = mod
        LOGS.info("⚡ 🄰🄽🄸🄴-🅄🅂🄴🅁🄱🄾🅃 ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"Aniebots.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


# Aniebot
