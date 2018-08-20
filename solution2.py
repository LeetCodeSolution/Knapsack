import numpy as np

count = 5
weight = 20

# 高 count，宽 weight + 1
matrix = [[0 for _ in range(weight + 1)] for _ in range(count)]

weights = {
    0: 2,
    1: 3,
    2: 4,
    3: 5,
    4: 9
}

values = {
    0: 3,
    1: 4,
    2: 5,
    3: 8,
    4: 10
}

# 初始化
for j in range(weight + 1):
    if j >= weights[0]:
        matrix[0][j] = values[0]

for i in range(count):
    # 注意要 + 1，从 0 开始，到 weight 结束
    for j in range(weight + 1):
        # 如果放得下
        if j >= weights[i]:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weights[i]] + values[i])
        # 如果放不下
        else:
            matrix[i][j] = matrix[i - 1][j]

print('Matrix')
print(matrix)
print('Max')
print(np.max(np.asarray(matrix).flatten()))
