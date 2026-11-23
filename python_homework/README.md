# Python 练习题（4 道题）

| 文件 | 题目要求 | 关键知识点 |
| --- | --- | --- |
| `task1_set_union.py` | 输入包含若干集合的列表，输出这些集合的并集 | `reduce()` + `lambda` |
| `task2_geometric_sum.py` | 输入等比数列首项、公比（不等于 1 且小于 36 的正整数）和自然数 n，输出前 n 项和 | 内置函数 `int()` |
| `task3_most_frequent_char.py` | 输入字符串，输出出现次数最多的字符及次数 | 字典 |
| `task4_char_frequency.py` | 输入任意长字符串，统计字母和数字频次，以字典保存并输出 | 字典 |

## 运行方式

```bash
python task1_set_union.py
python task2_geometric_sum.py
python task3_most_frequent_char.py
python task4_char_frequency.py
```

## 示例

**题 1**

```
输入：[{1, 2, 3}, {3, 4}, {5}]
输出：并集： {1, 2, 3, 4, 5}
```

**题 2**

```
首项：2
公比：3
项数：4
输出：前 4 项的和： 80
```

**题 3**

```
输入：abcaabb
输出：出现次数最多的字符： 'a'、'b'；出现次数：3
```

**题 4**

```
输入：abc A12!!
输出：{'1': 1, '2': 1, 'A': 1, 'a': 1, 'b': 1, 'c': 1}
```

说明：题 3 若有多个字符并列最多，会全部列出；题 4 只统计 ASCII 字母和数字，大小写区分。
