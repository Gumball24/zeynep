from monium.module import Module

from modules.ping.commands.ping import PingCommand


class PingModule(Module):
    id = "ping"
    name = "PingModule"
    version = (1, 0, 0)
    authors = ["Karahan"]

    async def on_ready(self):
        self.client.cmd.register_command(PingCommand(self))
