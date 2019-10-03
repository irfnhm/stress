#Sends parallel GET requests

import asyncio
import concurrent.futures
import requests

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                requests.get,
                'https://indiaforchange.org/'
            )
            #Change number in range according to the requests you want to send
            for i in range(20)
        ]
        for response in await asyncio.gather(*futures):
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
