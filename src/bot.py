import discord


class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.task = self.loop.create_task(self.view_stats())

    async def view_stats(self):
        await self.wait_until_ready()
        # if not self.is_closed():
        # print(self.guilds[0].id)
        bob : discord.member = self.get_guild(688557666779529271).members[0]
        print(bob.roles)

client = MyClient()
client.run()
