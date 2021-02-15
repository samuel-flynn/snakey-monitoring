import logging

class discord_alert_action:

    def  __init__(self, client, guild_name, channel_name):
        self.client = client
        self.guild_name = guild_name
        self.channel_name = channel_name

    async def execute(self, alert_message):
        
        await self.client.send(self.guild_name, self.channel_name, alert_message)