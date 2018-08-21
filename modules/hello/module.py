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

    async def on_ready(self):
        for server in self.client.servers:
            self.client.get_configuration(server.id).set_if_not_exist(
                "zeynep.subject.self",
                ["zeynep", "zeynep hanım"]
            )
            self.client.get_configuration(server.id).set_if_not_exist(
                "zeynep.message.hello",
                ["merhaba", "selam"]
            )
            self.client.get_configuration(server.id).set_if_not_exist(
                "zeynep.response.hello",
                ["merhaba", "selam"]
            )
            self.client.get_configuration(server.id).set_if_not_exist(
                "zeynep.regex.hello",
                "(%self% )?%message%( %self%)?"
            )
            self.client.get_configuration(server.id).save()

    async def on_message(self, message: discord.Message):
        regex = self.client.get_configuration(message.server.id).get("zeynep.regex.hello") \
            .replace("%self%", "|".join(self.client.get_configuration(message.server.id).get("zeynep.subject.self"))) \
            .replace("%message%",
                     "|".join(self.client.get_configuration(message.server.id).get("zeynep.message.hello")))

        if re.fullmatch(regex, message.content):
            await self.client.send_message(message.channel, random.choice(
                self.client.get_configuration(message.server.id).get("zeynep.response.hello")))
