def DFS(computers, check_nodes, cur_node):
    for target in range(len(computers[cur_node])):
        if cur_node==target: continue
        if computers[cur_node][target]==1:
            if check_nodes[target] != True:
                check_nodes[target] = True
                DFS(computers, check_nodes, target)



def check_all(check_nodes):
    for check in check_nodes:
        if check == False:
            return False
    return True


def find_unvisited_node(check_nodes):
    for i in range(len(check_nodes)):
        if check_nodes[i] == False:
            return i


def solution(n, computers):
    answer = 0

    check_nodes = [False for i in range(n)]

    while check_all(check_nodes) == False:
        target = find_unvisited_node(check_nodes)
        check_nodes[target]=True
        DFS(computers, check_nodes, target)
        answer += 1

    return answer