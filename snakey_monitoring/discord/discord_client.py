import discord
import logging
import asyncio
import logging

class discord_client:
    __LOGGER = logging.getLogger(__name__)

    def  __init__(self, token):
        self.client = discord.Client()
        self.ready = False
        self.token = token
    
    async def start(self):

        @self.client.event
        async def on_ready():
            self.__LOGGER.info('Discord connection ready.')
            self.ready = True
        
        try:
            await self.client.start(self.token)
        except KeyboardInterrupt:
            pass
        finally:
            self.__LOGGER.info('Closing discord connection.')
            await self.client.close()
    
    async def send(self, guild_name, channel_name, message):
        
        while not self.ready:
            await asyncio.sleep(1)
        
        guild_id = self.__get_matching_guild(guild_name)
        channel_id = self.__get_matching_channel(guild_id, channel_name)
        
        
        await channel_id.send(message)

    async def close(self):
        self.client.close()

    def __get_matching_guild(self, guild_name):
        guild_to_use = next((guild for guild in self.client.guilds if guild.name == guild_name), None)
        if not guild_to_use:
            raise EnvironmentError(f'Discord client is not on a server with name {guild_name}')
        return guild_to_use

    def __get_matching_channel(self, guild, channel_name):
        channel_to_use = next((channel for channel in guild.channels if channel.name == channel_name), None)
        if not channel_to_use:
            raise EnvironmentError(f'No channel named {channel_name} present on server {guild.name}')
        return channel_to_use
