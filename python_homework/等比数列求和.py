"""题目 (2)：输入等比数列的首项、公比（不等于 1 且小于 36 的正整数）和自然数 n，
输出这个数列前 n 项的和。关键步骤使用内置函数 int()。
"""

# 前 n 项和公式：S = a1 * (q ** n - 1) / (q - 1)


def geometric_sum(a1, q, n):
    """返回等比数列前 n 项和，整数运算避免大数浮点误差。"""
    numerator = a1 * (q ** n - 1)
    # 关键步骤：用 int() 完成取整；先做整数除法，保证大数不丢失精度
    return int(numerator // (q - 1))


def main():
    a1 = int(input("请输入首项 a1："))
    q = int(input("请输入公比 q（正整数，q != 1 且 q < 36）："))
    n = int(input("请输入项数 n（自然数）："))

    if q <= 0 or q >= 36 or q == 1:
        raise ValueError("公比必须是不等于 1 且小于 36 的正整数")
    if n < 0:
        raise ValueError("项数 n 必须是自然数")

    print("前 %d 项的和：" % n, geometric_sum(a1, q, n))


if __name__ == "__main__":
    main()
