"""题目 (3)：输入一个字符串，输出其中出现次数最多的字符及其出现的次数。
要求：使用字典。
"""

counts = {}
for ch in input("请输入字符串："):
    counts[ch] = counts.get(ch, 0) + 1
if counts:
    m = max(counts.values())
    chars = [c for c, v in counts.items() if v == m]
    print("出现最多的字符：", "、".join(repr(c) for c in chars), "次数：", m)
