def check_valid(cx, cy, N, M, maze, visited):
    if cx<0 or cx>=N: return False
    if cy<0 or cy>=M: return False
    if maze[cx][cy]==0: return False
    if visited[cx][cy]==True: return False
    return True

def BFS(cx, cy, N, M, visited, maze):
    q = []
    q.append([cx,cy,1]) # 첫 시작을 큐에 넣음
    visited[cx][cy]=True

    while len(q)!=0: # 더 이상 탐색할게 없을때까지
        cx,cy,path_len = q[0][0],q[0][1],q[0][2]  # 큐에서 탐색할 대상을 꺼내고
        del q[0] # 그걸 지움

        if cx==N-1 and cy==M-1:
            return path_len

        if check_valid(cx + 1, cy, N, M, maze, visited):  # 아래
            visited[cx + 1][cy] = True
            q.append([cx+1,cy,path_len+1])

        if check_valid(cx, cy + 1, N, M, maze, visited):  # 오른쪽
            visited[cx][cy + 1] = True
            q.append([cx,cy+1,path_len+1])

        if check_valid(cx - 1, cy, N, M, maze, visited):  # 위쪽
            visited[cx - 1][cy] = True
            q.append([cx-1,cy,path_len+1])

        if check_valid(cx, cy - 1, N, M, maze, visited):  # 왼쪽
            visited[cx][cy - 1] = True
            q.append([cx,cy-1,path_len+1])


def solution():
    ins = [int(i) for i in input().split()]
    N, M = ins[0], ins[1]

    maze = [[] for i in range(N)]
    visited = [[False]*M for i in range(N) ]

    for i in range(N):
        temp_str = input()
        for j in temp_str:
            maze[i].append(int(j))

    print(BFS(0,0,N,M,visited,maze))
solution()