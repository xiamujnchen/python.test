from ast import literal_eval
from functools import reduce

raw = input("请输入集合列表（如 [{1, 2}, {2, 3}]）：")
sets = literal_eval(raw)
result = reduce(lambda a, b: a | b, sets, set())
print("并集：", result)
