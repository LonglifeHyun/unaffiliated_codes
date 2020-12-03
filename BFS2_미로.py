def check_valid(cx, cy, N, M, maze, visited):
    if cx<0 or cx>=N: return False
    if cy<0 or cy>=M: return False
    if maze[cx][cy]==0: return False
    if visited[cx][cy]==True: return False
    return True

def BFS(cx, cy, N, M, visited, maze):
    q = []
    q.append([cx,cy]) # 첫 시작을 큐에 넣음
    nxt = []
    visited[cx][cy]=True

    cnt=1
    while len(q)!=0: # 더 이상 탐색할게 없을때까지
        for i in range(len(q)):
            nxt.append(q[i])
        q.clear()

        for i in range(len(nxt)):
            cx, cy = nxt[i][0], nxt[i][1]

            if cx==N-1 and cy==M-1:
                return cnt

            if check_valid(cx + 1, cy, N, M, maze, visited):  # 아래
                visited[cx + 1][cy] = True
                q.append([cx+1,cy])

            if check_valid(cx, cy + 1, N, M, maze, visited):  # 오른쪽
                visited[cx][cy + 1] = True
                q.append([cx,cy+1])

            if check_valid(cx - 1, cy, N, M, maze, visited):  # 위쪽
                visited[cx - 1][cy] = True
                q.append([cx-1,cy])

            if check_valid(cx, cy - 1, N, M, maze, visited):  # 왼쪽
                visited[cx][cy - 1] = True
                q.append([cx,cy-1])
        cnt+=1



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