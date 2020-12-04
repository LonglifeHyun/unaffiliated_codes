def move_dong(dice):
    dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]

def move_seo(dice):
    dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]

def move_book(dice):
    dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

def move_nam(dice):
    dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

def find_top(map_num, pos, dice):
    if map_num[pos[0]][pos[1]] == 0:
        map_num[pos[0]][pos[1]] = dice[2]
    else:
        dice[2] = map_num[pos[0]][pos[1]]
        map_num[pos[0]][pos[1]] = 0
    return dice[0]

def main():
    in_data = [int(val) for val in input().split()]
    n, m, x, y, k = in_data[0], in_data[1], in_data[2], in_data[3], in_data[4]

    map_num = []
    for i in range(n):
        map_num.append([int(col) for col in input().split()])

    order = [int(dd) for dd in input().split()]

    #print("map_num", map_num)
    #print("order:", order)

    answer = []

    dice = [0 for i in range(6)]
    # sides : [0]top, [1]front, [2]bottom, [3]back, [4]left, [5]right

    pos = [x,y]

    for i, direct in enumerate(order):
        #print("i : ",i,"pos : ",pos[0],", ",pos[1])
        if direct == 1:
            if pos[1]+1 < m:     # in range
                pos[1] += 1
                move_dong(dice)
                answer.append(find_top(map_num, pos, dice))

        elif direct == 2:
            if pos[1]-1 >= 0:    # in range
                pos[1] -= 1
                move_seo(dice)
                answer.append(find_top(map_num, pos, dice))

        elif direct == 3:
            if pos[0]-1 >= 0:    # in range
                pos[0] -= 1
                move_book(dice)
                answer.append(find_top(map_num, pos, dice))

        else:
            if pos[0]+1 < n:     # in range
                pos[0] += 1
                move_nam(dice)
                answer.append(find_top(map_num, pos, dice))

        #print(dice)

    for ans in answer:
        print(ans)

if __name__ == "__main__":
    main()