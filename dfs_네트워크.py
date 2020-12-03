def is_visited(visited, pos):
    return visited[pos]


def bfs(relation, visited, cnt):
    q = []
    for i, com in enumerate(relation):
        # q.clear()
        if not is_visited(visited, i):
            cnt += 1
            for j in com:
                q.append(j)
            while (len(q) != 0):
                pos = q[0]
                del q[0]
                visited[pos] = True
                for k in relation[pos]:
                    if not is_visited(visited, k):
                        q.append(k)
    return cnt


def solution(n, computers):
    relation = [[] for i in range(n)]
    visited = [False for i in range(n)]
    cnt = 0

    for c_id, coms in enumerate(computers):
        for j, com in enumerate(coms):
            if c_id != j and com == 1:
                relation[c_id].append(j)

    answer = bfs(relation, visited, cnt)
    return answer