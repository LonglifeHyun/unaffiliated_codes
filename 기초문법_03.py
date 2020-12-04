# 파이썬 기초 03. 파이썬 반복문, 조건문, 리스트 퀴즈

def main():

    # ex31. 반복문
    sum = 0
    for i in range(11):
        sum += i
    print(sum)

    # ex32. 반목문
    """n = int(input())"""
    n = 4
    for i in range(1,10):
        print(n,"x",i,"=",n*i)

    # ex33. 반복문과 문자열 다루기(split)
    """
    for name in input().split(','):
        print(name)
    """

    # ex34. 반복문과 문자열 다루기(split) , enumerate
    """ string = input().split('],[') """
    string = "[Dave],[David],[Andy],[Arthor]".split('],[')
    for i, name in enumerate(string):
        if i==0:
            print(name[1:])
        elif i==len(string)-1:
            print(name[:-1])
        else:
            print(name)
    """ OR """
    for name in string:
        print(name.strip('[]')) # 이게 더 좋네

    # ex35. 반복문과 조건문
    for digit in range(3,31,3):
        print(digit)

    # ex36. 반목문(while)
    sum, i = 0, 1
    while i<=100:
        sum += i
        i += 1
    print(sum)

    # ex37. 반복문(while)
    """
    pw = "4312"
    while(input()!=pw):
        print("비밀번호가 틀렸습니다.")
    print("비밀번호가 맞습니다.")
    """

    # ex38. 데이터 구조와 반복문 (리스트), comprehension
    num_list = [0, -11, 31, 22, -11, 33, -44, -55]
    pos_num_list = [num for num in num_list if num > 0]
    print(pos_num_list)

    # ex39. 데이터 구조와 반복문 (리스트)
    list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
    for data in list_data:
        print(data, len(data))

    # ex40. 데이터 구조와 반복문 (리스트), reverse, reversed
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in reversed(data):
        print(num)
    print(data)
    print(data.reverse())
    print(data)

    # ex41. 데이터 구조(리스트), 반복문, 문자열 다루기
    filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
    for filename in filelist:
        print(filename.strip('.docx'))

    # ex42. 데이터 구조(리스트), 반복문, 문자열 다루기
    filelist = ['exercise01.docx', 'exercise02.csv', 'exercise03.txt', 'exercise04.hwp']
    for file in filelist:
        if file.find('.txt') != -1:
            print(file)
    """ OR """
    print([files for files in filelist if files.find('.txt')!= -1])

    # ex43. 문자열 다루기와 조건문
    prices = "100달러"
    exch_rate = 1112
    print(int(prices.strip("달러"))*exch_rate,"원")

    #ex44. 문자열 다루기와 조건문
    money = "100 위안".split() #input().split()
    if money[1] == "달러":
        exch_rate = 1112
    elif money[1] == "위안":
        exch_rate = 171
    print(int(money[0])*exch_rate,"원")

    # ex45. 문자열 다루기, 조건문, 데이터 구조 (dictionary)
    exch_rate = {"달러":1112, "위안":171, "엔":1010}

    money = "100 엔".split() #input().split()
    print(int(money[0])*exch_rate[money[1]],"원")

    # ex46. 이중반복문
    for i in range(2,10):
        for j in range(1,10):
            print(i,"X",j,"=",i*j)

    # ex47. 이중반복문과 조건문
    for i in range(2,10):
        for j in range(1,10):
            if (i*j) % 2 == 0:
                print(i,"X",j,"=",i*j)

    # ex48. 이중 반복문과 데이터구조(리스트)
    dongs = ["6209동", "6208동", "6207동"]
    hos = ["101호", "102호", "103호", "104호"]

    for dong in dongs:
        for ho in hos:
            print(dong, ho)




if __name__ == '__main__':
    main()
