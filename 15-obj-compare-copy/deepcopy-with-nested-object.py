# import copy
# x = [1]
# x.append(x)
# print(x)
# y = copy.deepcopy(x)
#
# # 以下命令的输出是？
# print(x == y)

a = 1
b = a
a = a + 1
print(a)
print(b)