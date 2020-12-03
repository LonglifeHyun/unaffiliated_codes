min_answer = 100000

def is_valid(pos,n,m,maze,visited):
    p_r, p_c = pos[0], pos[1]

    if not(0 < p_r or p_r < n):
        return False
    if not(0 < p_c or p_c < m):
        return False
    if maze[p_r][p_c] == 0:
        return False
    if visited[p_r][p_c] == True:
        return False

    return True

def bfs(pos, maze, cnt,n,m,visited):
    p_r, p_c = pos[0], pos[1]

    q = [[p_r,p_c,cnt]]
    visited[p_r][p_c] = True

    while len(q) != 0:
        p_r,p_c,cnt = q[0][0], q[0][1], q[0][2]
        del q[0]

        if p_r==n-1 and p_c=m-1:
            return cnt

        if is_valid([p_r+1,p_c],n,m,maze,visited):
            visited[p_r+1][p_c] = True
            q.append([p_r+1,p_c,cnt+1])

        elif is_valid()


def solution():
    in_data = [int(val) for val in input().split()]
    n, m = in_data[0], in_data[1]
    maze = []
    for i in range(n):
        maze.append([int(j) for j in list(input())])

    print(maze)

    pos = [0,0]
    cnt = 1

    visited = [[False for j in range(m)] for i in range(n)]
    print(visited)

    bfs(pos,maze,cnt,n,m,visited)

solution()