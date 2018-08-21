import discord
from monium.ext.command import Command


class PingCommand(Command):
    name = "ping"

    async def run(self, message: discord.Message, **kwargs):
        await self.client.send_message("ping!", message.channel)
