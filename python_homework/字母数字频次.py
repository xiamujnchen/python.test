"""题目 (4)：输入任意长的字符串，统计该字符串中字母和数字的频次，
并将结果以字典保存和输出。
"""


def count_letters_and_digits(text):
    """只统计 ASCII 字母和数字；大小写区分，结果保存在字典中。"""
    freq = {}
    for ch in text:
        if ch.isascii() and (ch.isalpha() or ch.isdigit()):
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def main():
    text = input("请输入任意长的字符串：")
    freq = count_letters_and_digits(text)
    # 按字符排序后输出，结果仍是字典
    result = dict(sorted(freq.items()))
    print("字母和数字频次字典：", result)


if __name__ == "__main__":
    main()
