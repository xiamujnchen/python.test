"""题目 (4)：输入任意长的字符串，统计该字符串中字母和数字的频次，
并将结果以字典保存和输出。
"""
freq = {}
for ch in input("请输入字符串："):
    if ch.isascii() and (ch.isalpha() or ch.isdigit()):
        freq[ch] = freq.get(ch, 0) + 1
result = dict(sorted(freq.items()))
print("字母和数字频次字典：", result)
