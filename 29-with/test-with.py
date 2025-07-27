import time

# start = time.time()
# f = open('test.txt', 'w')
# for x in range(10000000):
#     f.write('hello')
# end = time.time()
# print('耗时: {:.2f} 秒'.format(end - start))

start = time.time()
with open('test.txt', 'w') as f:
    for x in range(10000000):
        f.write('hello')
end = time.time()
print('耗时: {:.2f} 秒'.format(end - start))