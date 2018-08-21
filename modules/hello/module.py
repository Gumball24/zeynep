import re

import discord
from monium.module import Module


class HelloModule(Module):
    id = "hello"
    name = "Hello Module"
    version = (1, 0, 0)
    authors = ["Karahan"]

    def init(self):
        self.logger.info("Module enabled.")

    async def on_message(self, message: discord.Message):
        if re.match(
                "((kızlar|beyler|zeynep) )\?(sa|selamun aleyküm|merhaba|selam|hi|hello|naber|)( (kızlar|beyler|zeynep))\?",
                message.content):
            await self.client.send_message(message.channel, "as")
