l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2

print(l1 == l2)
print(l2 == l3)

print(l1 is l2)
print(l2 is l3)

def func(d):
    d['a'] = 10
    d['b'] = 20
    d = {'a': 1, 'b': 2}
# d i not defined
# func(d)
# print(d)