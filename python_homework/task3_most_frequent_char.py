"""题目 (3)：输入一个字符串，输出其中出现次数最多的字符及其出现的次数。
要求：使用字典。
"""


def most_frequent_chars(text):
    """返回 (出现次数最多的字符列表, 次数)；若有多个并列，全部返回。"""
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    if not counts:
        return [], 0

    max_count = max(counts.values())
    chars = [ch for ch, count in counts.items() if count == max_count]
    return chars, max_count


def main():
    text = input("请输入一个字符串：")
    chars, count = most_frequent_chars(text)
    if not chars:
        print("输入为空字符串")
    else:
        print("出现次数最多的字符：", "、".join(repr(c) for c in chars))
        print("出现次数：", count)


if __name__ == "__main__":
    main()
