import time
import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')

# %time asyncio.run(main())
start = time.time()
asyncio.run(main())
end = time.time()
print('耗时: {:.2f} 秒'.format(end - start))