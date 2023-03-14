a = {"123": 1, "56":8, "7": [1,2,3]}
print(a["123"])
print(a["56"])
a["123"] = -1
print(a["123"])
a["89"] = 0 # 在字典里面，插入新的key-value， ("89", 0)
print(a["89"])

# {key1: value1, key2:value2, ...}
# key之间不能重复，value可以重复。都不要求类型相同
# 字典相当于(key, value)的列表， [[k1, v1], [k2, v2], ...]，k不能重复
print(len(a))
print(list(a)) # 转换a的key的列表
print(list(a.keys()))
print(tuple(a.values()))

# 字典的迭代

for w in a:
    print(w, "->", a[w])

# for k, v in enumerate(a):
#     print(k, v)