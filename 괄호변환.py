def seperating(w):
    l_cnt, r_cnt = 0, 0
    u, v = "", ""

    for i, c in enumerate(w):
        if l_cnt != 0 and l_cnt == r_cnt:
            v = w[i:]
            break
        if c == "(":
            u += c
            l_cnt += 1
        else:
            u += c
            r_cnt += 1

    return u, v

def is_right(s):
    solo_list = []

    for i, c in enumerate(s):
        if c == "(":
            solo_list.append(c)
        else:
            if i==0 or len(solo_list) == 0:
                return False
            else:
                solo_list.pop()
    return True

def processing(w):
    if w == "":
        return ""

    u, v = seperating(w)

    if is_right(u):
        return u+processing(v)
    else:
        tmp = "("
        tmp += processing(v)
        tmp += ")"

        u_list = list(u)
        del u_list[0]
        u_list.pop()
        # u_list.reverse()

        for i, c in enumerate(u_list):
            if c == "(":
                u_list[i] = ")"
            else:
                u_list[i] = "("

        u = "".join(u_list)
        tmp += u

        return tmp

def solution(p):
    answer = processing(p)
    return answer

def main():
    print(solution(input()))

if __name__ == '__main__':
    main()
