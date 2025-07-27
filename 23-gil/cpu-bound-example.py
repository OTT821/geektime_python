import time
def CountDown(n):
    while n > 0:
        n -= 1

n = 100000000

# start = time.time()
# CountDown(n)
# end = time.time()
# print('耗时: {:.2f} 秒'.format(end - start))



from threading import Thread
t1 = Thread(target=CountDown, args=[n // 2])
t2 = Thread(target=CountDown, args=[n // 2])

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('耗时: {:.2f} 秒'.format(end - start))