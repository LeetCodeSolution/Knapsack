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


def solution(k, w):
    if k == 0:
        if w >= weights[k]:
            return values[k]
        else:
            return 0
    else:
        # 如果盛不下
        if w < weights[k]:
            return solution(k - 1, w)
    # 如果盛得下
    return max(solution(k - 1, w - weights[k]) + values[k],
               solution(k - 1, w))


result = solution(4, 20)
print(result)
