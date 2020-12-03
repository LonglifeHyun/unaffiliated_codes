
def min_route(will_go,visit,pos,maze):
    if pos[0] == n-1 and pos[1] == m-1:
        return

    visit.append(pos)
    print(visit)




def main():
    in_data = [int(sz) for sz in input().split()]
    n, m = in_data[0], in_data[1]

    maze = []
    for i in range(n):
        maze.append([int(j) for j in list(input())])

    print(maze)
    pos = [0,0]


    will_go, visit = [], []
    min_route(will_go,visit,pos,maze)




if __name__ == "__main__":
    main()