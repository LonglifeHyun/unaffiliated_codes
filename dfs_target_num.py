def dfs(numbers, pos, total, target, cnt):
    if pos == len(numbers):
        if total == target:
            cnt += 1
        return cnt

    # +
    total += numbers[pos]
    cnt = dfs(numbers, pos + 1, total, target, cnt)
    total -= numbers[pos]
    # -
    total -= numbers[pos]
    cnt = dfs(numbers, pos + 1, total, target, cnt)
    total += numbers[pos]

    return cnt


def solution(numbers, target):
    total = 0
    cnt = 0
    answer = dfs(numbers, 0, total, target, cnt)
    print(answer)
    return answer