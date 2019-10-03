#Sends parallel GET requests

import asyncio
import concurrent.futures
import requests

async def main():
    workers = int(input("Enter the max number of workers: "))
    get_requests = int(input("Enter the number of GET requests you want to send: "))
    print("Sending GET...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                requests.get,
                'https://indiaforchange.org/'
            )
            #Change number in range according to the requests you want to send
            for i in range(get_requests)
        ]
        for response in await asyncio.gather(*futures):
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
