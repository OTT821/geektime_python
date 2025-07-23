import time
import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

# %time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
start = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end = time.time()
print('耗时: {:.2f} 秒'.format(end - start))