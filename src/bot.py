import discord
import tokens


class UCSD24StatsBot(discord.Client):

    def __init__(self, guild_id : int):
        super().__init__()
        self.guild_id = guild_id
        self.task = self.loop.create_task(self.view_stats())
        self.server_members = []
        self.server_roles = []

    async def view_stats(self):
        await self.wait_until_ready()
        self.server_members = self.get_guild(self.guild_id).members
        self.server_roles = self.get_guild(self.guild_id).roles
        await self.logout()


