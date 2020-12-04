from itertools import combinations

def can_be_pw(yet_pws):
    vowels = ['a','e','i','o','u']

    pws = []
    for pw in yet_pws:
        v_cnt, c_cnt = 0, 0
        for ch in pw:
            if ch in vowels:
                v_cnt += 1
            else:
                c_cnt += 1
        if 0 < v_cnt and 1 < c_cnt :
            tmp = "".join(sorted(pw))
            pws.append(tmp)
    return sorted(pws)

def main():
    in_data = [int(val) for val in input().split()]
    l, c = in_data[0], in_data[1]
    chars = input().split()

    tmp_pw = list(combinations(chars,l))
    pws = can_be_pw(tmp_pw)
    for pw in pws:
        print(pw)



if __name__ == '__main__':
    main()

