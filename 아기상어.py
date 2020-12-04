def cal_dis(s_pos, f_pos):
    return (abs(s_pos[0]-f_pos[0]))**2 + (abs(s_pos[1]-f_pos[1]))**2

def is_valid()
    return

def shark_move(space,shark,visited,tm_cnt,food_pos,is_sz_changed):


def shark_hunt(space,shark,visited,tm_cnt):
    is_there_food = False
    is_sz_changed = False

    food = []
    for i in range(n):
        for j in range(n):
            if space[i][j][0] < shark[0]:   # size compare
                is_there_food = True
                food.append(space[i][j])    # fish
    food.sort(key=lambda x:x[1])

    if not is_there_food:
        return tm_cnt

    while( len(food) != 0 ):
        food_pos = food[0]
        del food[0]
        shark_move(space,shark,visited,tm_cnt,food_pos,is_sz_changed)

    if is_sz_changed :
        tm_cnt = shark_hunt(space,[shark[0]+1,shark[1]],visited,tm_cnt)
    return tm_cnt

def main():
    n = int(input())
    space = []          # space = [fish sz, distance] *n *n
    s_sz = 2
    shark = [s_sz]      # fish, shark = [size, pos(i,j)]
    # 0 : none   1~6 : fish sz   9 : shark
    for i in range(n):
        r_in = [[int(j)] for j in input().split()]
        space.append(r_in)
        for j, info in enumerate(r_in):
            if info[0] == 9:
                s_pos = [i,j]
                #print(s_pos)
                shark.append(s_pos)

    is_there_food = False
    for i in range(n):
        for j in range(n):
            if space[i][j][0] > 0:
                if space[i][j][0] != 9:
                    is_there_food = True
                f_pos = [i,j]
                space[i][j].append(cal_dis(shark[1],f_pos))
    #print(shark)
    for i in space:
        print(i)

    visited = [[False for j in range(n)] for i in range(n)]

    tm_cnt = 0
    if is_there_food:
        shark_hunt(space,shark,visited,tm_cnt)
    print("answer: ",tm_cnt)

main()