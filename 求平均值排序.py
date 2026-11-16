li = [float(x) for x in input("输入列表:").split(",") if x.strip()]
li.sort()
print("排序后的列表:", li)
print("最大值:", max(li), "最小值:", min(li))
print("平均值:", sum(li) / len(li))