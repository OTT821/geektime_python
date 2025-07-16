d = {'mike': 10, 'lucy': 2, 'ben': 30}

#根据键进行由高到底的排序
d1 = sorted(d.keys(), key=lambda k : k)
print(d1)
#根据值进行由高到底的排序
d2 = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(d2)