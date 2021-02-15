import logging
import os
import asyncio
import aiohttp

__LOGGER = logging.getLogger(__name__)

async def open_watch(url, frequency_seconds, actions, timeout_seconds=10):

    try:
        timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        async with aiohttp.ClientSession() as session:
            __LOGGER.info(f'Opening watch on {url}')
            while True:
                try:
                    async with session.get(url) as response:

                        status = response.status
                        __LOGGER.debug(f'{url} : {status}')

                        if not status == 200:

                            alert_message = f'Alert: {url} returned response code {status}'
                            for action in actions:
                                await action.execute(alert_message)

                except aiohttp.ServerTimeoutError as e:
                    alert_message = f'Alert: Connection to {url} timed out after {timeout_seconds} seconds'
                    for action in actions:
                        await action.execute(alert_message)

                except aiohttp.ClientConnectionError as e:
                    alert_message = f'Alert: Unable to connect to {url} : {str(e)}'
                    for action in actions:
                        await action.execute(alert_message)

                except aiohttp.ClientResponseError as e:

                    alert_message = f'Alert: {url} returned response code {e.status}'
                    for action in actions:
                        await action.execute(alert_message)

                await asyncio.sleep(frequency_seconds)

    except KeyboardInterrupt:
        __LOGGER.info(f'Closing watch on {url}')
