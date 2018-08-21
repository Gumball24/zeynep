import random
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

    responses = ["merhaba", "as", "selam", "aleyküm selam"]

    async def on_message(self, message: discord.Message):
        if re.fullmatch(
                "((k+ı+z+l+a+r+|b+e+y+l+e+r+|z+e+y+n+e+p+) )?(s+a+|s+e+l+a+m+(ü+|u+)n+ a+l+e+y+k+(ü+|u+)m+|m+e+r+h+a+b+a+|s+e+l+a+m+|h+i+|h+e+l+l+o+|n+a+b+e+r+)( (k+ı+z+l+a+r+|b+e+y+l+e+r+|z+e+y+n+e+p+))?(!+|\.+)?",
                message.content, re.IGNORECASE):
            await self.client.send_message(message.channel, random.choice(self.responses))
