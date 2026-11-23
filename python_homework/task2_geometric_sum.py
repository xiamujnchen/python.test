"""题目 (2)：输入等比数列的首项、公比（不等于 1 且小于 36 的正整数）和自然数 n，
输出这个数列前 n 项的和。关键步骤使用内置函数 int()。
"""
a1 = int(input("首项："))
q = int(input("公比（≠1 且 <36 的正整数）："))
n = int(input("项数 n："))
if not (0 < q < 36 and q != 1) or n < 0:
    raise ValueError("输入不符合要求")
total = int(a1 * (q ** n - 1) // (q - 1))   # 整数运算避免大数精度丢失
print("前 %d 项的和：" % n, total)
