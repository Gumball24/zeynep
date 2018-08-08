from monium.module import Module

from .commands.ping_command import PingCommand


class PingModule(Module):
    id = "ping"
    name = "Ping Module"
    version = (1, 0, 0)
    authors = ["Karahan"]

    def init(self):
        self.logger.info("Ping!")

    async def on_ready(self):
       # self.client.cmd.register_command(PingCommand(self))
