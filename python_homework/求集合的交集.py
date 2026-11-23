set1 = set(eval(input("请输入第一个集合，例如{1,2,3}:")))
set2 = set(eval(input("请输入第二个集合，例如{3,4,5}:")))

jiaoji = set1 & set2    # 交集
bingji = set1 | set2    # 并集
chaji = set1 - set2     # 差集（set1有，set2没有）

print("交集：", jiaoji)
print("并集：", bingji)
print("差集(set1-set2):", chaji)