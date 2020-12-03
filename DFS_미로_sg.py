Answer=9999999
path=[]

def check_valid(cx, cy, N, M, maze, visited):
    if cx<0 or cx>=N: return False
    if cy<0 or cy>=M: return False
    if maze[cx][cy]==0: return False
    if visited[cx][cy]==True: return False
    return True

def DFS(cx, cy, N, M, visited, maze, sum):
    global Answer
    if cx==N-1 and cy==M-1:
        # print(path)
        if sum < Answer: Answer=sum

    if check_valid(cx+1,cy,N,M,maze,visited): # 아래
        # path.append([cx+1,cy])
        visited[cx+1][cy] = True
        DFS(cx+1,cy,N,M,visited,maze,sum+1)
        visited[cx+1][cy] = False
        # path.pop()

    if check_valid(cx,cy+1,N,M,maze,visited): # 오른쪽
        # path.append([cx, cy+1])
        visited[cx][cy+1] = True
        DFS(cx,cy+1,N,M,visited,maze,sum+1)
        visited[cx][cy+1] = False
        # path.pop()

    if check_valid(cx-1,cy,N,M,maze,visited): # 위쪽
        # path.append([cx-1, cy])
        visited[cx-1][cy] = True
        DFS(cx-1,cy,N,M,visited,maze,sum+1)
        visited[cx-1][cy] = False
        # path.pop()

    if check_valid(cx,cy-1,N,M,maze,visited): # 왼쪽
        # path.append([cx, cy-1])
        visited[cx][cy-1] = True
        DFS(cx,cy-1,N,M,visited,maze,sum+1)
        visited[cx][cy-1] = False
        # path.pop()

def solution():
    ins = [int(i) for i in input().split()]
    N, M = ins[0], ins[1]

    maze = [[] for i in range(N)]
    visited = [[False]*M for i in range(N) ]

    for i in range(N):
        temp_str = input()
        for j in temp_str:
            maze[i].append(int(j))

    path.append([0, 0])
    visited[0][0] = True
    DFS(0,0,N,M,visited,maze,1)

    print(Answer)
solution()