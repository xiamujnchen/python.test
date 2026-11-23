"""题目 (1)：输入包含若干集合的列表，输出这些集合的并集。
要求：使用 reduce() 函数和 lambda 表达式完成。
"""

from ast import literal_eval
from functools import reduce


def parse_sets(text):
    """把输入解析为集合列表，例如 [{1, 2}, {2, 3}]。"""
    data = literal_eval(text)
    if not isinstance(data, list) or not all(isinstance(item, set) for item in data):
        raise ValueError("请输入集合列表，例如：[{1, 2}, {2, 3}]")
    return data


def union_of_sets(sets):
    """用 reduce() + lambda 依次合并所有集合；初始值为空集合，兼容空列表。"""
    return reduce(lambda a, b: a | b, sets, set())


def main():
    raw = input("请输入集合列表（如 [{1, 2}, {2, 3}]）：")
    result = union_of_sets(parse_sets(raw))
    print("并集：", result)


if __name__ == "__main__":
    main()
