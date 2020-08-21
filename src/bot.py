import discord
import tokens


class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.task = self.loop.create_task(self.view_stats())
        self.server_members = []

    async def view_stats(self):
        await self.wait_until_ready()
        # if not self.is_closed():
        # print(self.guilds[0].id)
        self.server_members = self.get_guild(688557666779529271).members
        print(self.server_members)

client = MyClient()
client.run(tokens.token)
