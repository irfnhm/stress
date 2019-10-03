#Sends parallel GET requests

import os
import asyncio
import concurrent.futures
import requests

async def main():
    print('Note: while you start sending multiple GET requests, it is recommended to monitor your site health status.')
    url = input('Host: ')

    #Ping is optional. Use it if you wanna see if the host is up before stressing
    #response = os.system("ping -c 1 " + url)
    #if response == 0:
    #  print (url, 'is up.')
    #else:
    #  print (url, 'is down.')
    #  exit()
    #Ping section ends here

    workers = int(input('Number of workers/threads: '))
    get_requests = int(input('Number of GET requests ( > 1): '))
    print('Sending', get_requests, 'GET requests...')
    print('Please wait until the test is finished.')
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                requests.get,
                url
            )
            for i in range(get_requests)
        ]
        for response in await asyncio.gather(*futures):
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
