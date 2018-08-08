import datetime

import discord
from monium.ext.command import Command


class PingCommand(Command):
    name = "ping"
    args = []

    async def run(self, message: discord.Message, **kwargs):
        latency = (datetime.datetime.utcnow() - message.timestamp).total_seconds() * 1000

        await self.client.send_message(f"Ping! ({latency}ms)")
