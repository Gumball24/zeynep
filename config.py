""""""
"""
88888b.d88b.   .d88b.  88888b.  888 888  888 88888b.d88b.
888 "888 "88b d88""88b 888 "88b 888 888  888 888 "888 "88b
888  888  888 888  888 888  888 888 888  888 888  888  888
888  888  888 Y88..88P 888  888 888 Y88b 888 888  888  888
888  888  888  "Y88P"  888  888 888  "Y88888 888  888  888
                                ...Framework Configuration
"""

import logging
import os

TOKEN = os.environ["TOKEN"]
""" Bot token from https://discordapp.com/developers/applications/me """

MONIUM_LOGLEVEL = logging.INFO
""" Monium logging level """

MODULE_LOGLEVEL = logging.INFO
""" Module logging level """

OTHER_LOGLEVEL = logging.INFO
""" Other library logging level """

MODULE_PATH = ["modules"]
"""
Import paths for modules

Don't change unless you know what you're doing
"""

DATA_PATH = "data/"
"""
Module data folder

This is where the configuration(s) and other module stuff will go to
"""

MULTIPLE_SERVER_SUPPORT = False
""" Will the bot get used in multiple servers? """

DEFAULT_COMMAND_PREFIX = "!"
""" Default Command Prefix """

DEFAULT_LANGUAGE = "en"
""" Default Language """
