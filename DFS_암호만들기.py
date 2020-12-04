def is_valid(pw):
    vowels = ['a', 'e', 'i', 'o', 'u']
    v_cnt, c_cnt = 0, 0
    for cc in pw:
        if cc in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if 0 < v_cnt and 1 < c_cnt :
        return True
    return False

def dfs(l,chars,pws,pw,pos):
    if len(pw)==l:
        if is_valid(pw):
            pp = "".join(pw)
            pws.append(pp)
            return

    if pos == len(chars):
        return

    for i in range(pos,len(chars)):
        pw.append(chars[i])
        dfs(l,chars,pws,pw,i+1)
        pw.pop()



def main():
    in_data = [int(val) for val in input().split()]

    l, c = in_data[0], in_data[1]
    chars = input().split()
    chars.sort()

    pws = []
    pw = []
    pos = 0
    dfs(l,chars,pws,pw,pos)

    for p in pws:
        print(p)

if __name__ == '__main__':
    main()

