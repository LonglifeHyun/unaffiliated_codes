def is_similar(ww, w):
    dif_cnt = 0
    for i in range(len(w)):
        if w[i] != ww[i]:
            dif_cnt += 1
        if dif_cnt > 1:
            return False
    return True


def find_similar(words, w):
    ones = []
    for ww in words:
        if is_similar(ww, w):
            ones.append(ww)
    return ones


def find_w_idx(w, words):
    for i, ww in enumerate(words):
        if ww == w:
            return i


def bfs(w_pos, target, words, visit, cnt):
    q = []
    q.append([w_pos, cnt])

    while (len(q) != 0):
        w = q[0][0]
        w_cnt = q[0][1]
        # print(w_cnt)
        del q[0]
        idx = find_w_idx(w, words)
        # print(w," idx :", idx)
        if idx != None:
            visit[idx] = True

        if w == target:
            return w_cnt

        ones = find_similar(words, w)
        w_cnt += 1
        for one in ones:
            idx = find_w_idx(one, words)
            if visit[idx] == False:
                q.append([one, w_cnt])


def processing(begin, target, words, visit):
    if target not in words:
        return 0
    cnt = 0
    return bfs(begin, target, words, visit, cnt)


def solution(begin, target, words):
    visit = [False for i in words]
    answer = processing(begin, target, words, visit)
    return answer