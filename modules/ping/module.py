from monium.module import Module

from modules.ping.commands.PingCommand import PingCommand


class PingModule(Module):
    id = "ping"
    name = "Ping Module"
    version = (1, 0, 0)
    authors = ["Karahan"]

    def init(self):
        self.client.cmd.register_command(PingCommand())
