# 파이썬 기초 02. 파이썬 변수, 조건문, 리스트, 문자열 퀴즈

def main():

    # ex12. 기본 자료형
    v1 = 10
    v2 = 2.2
    v3 = "fun-coding"
    print(type(v1))
    print(type(v2))
    print(type(v3))

    # ex13. 기본 자료형
    code = '000660\n00000102\t12312312'
    print (code)

    # ex14. 조건문
    """
    n1 = int(input())
    n2 = int(input())
    print(max(n1,n2))
    if n1 > n2:
        print(n1)
    elif n1 < n2:
        print(n2)
    else:
        print("same")

    # ex15. 조건문
    if n1%2 == 0:
        print("even")
    else:
        print("odd")

    # ex16. 조건문
    n3 = int(input())
    print(max(n1,n2,n3))
    """

    # ex17. 조건문
    """ 노가다라 넘어감 """


    # ex18. 데이터 구조(리스트)
    #id_num = input()
    id_num = "880001-1231231"
    print(id_num[0]+id_num[1])
    print(id_num[0:2])

    # ex19. 데이터 구조(리스트)
    id_num_list = id_num.split('-')
    print(id_num_list[1][0])

    # ex20. 데이터 구조(리스트)
    if id_num_list[1][0] == str(1):
        print("M")
    else:
        print("F")

    # ex21. 문자열 다루기(strip)
    mystr = "...a man ...goes into the room..."
    print(mystr.replace("...",""))
    print(mystr.lstrip("..."))
    print(mystr.rstrip("..."))
    print(mystr.strip("..."))

    # ex22. 문자열 다루기(strip)
    code = '         000660\n            '
    print(code.strip(' \n'))

    # ex23. 문자열 다루기(count)
    python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
    print(python_desc.count("Python"))

    # ex24. 문자열 다루기(count)
    python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
    print(python_desc.count('p'))


    # ex25. 문자열 다루기(문자열 인덱싱)
    letters = "python"
    print(letters[1]+'\n'+letters[3])

    # ex26. 문자열 다루기(문자열 인덱싱)
    #letters = input()
    letters = "laskdnfklnasd"
    if letters.count('n') != 0:
        print("0")
    else:
        print("-1")
    """OR"""
    if letters.find('n') != -1:
        print("0")
    else:
        print("-1")

    # ex27. 문자열 다루기(문자열 인덱싱)
    """ ex26과 동일 """

    # ex28. 문자열 다루기(문자열 인덱싱)
    id_num = "808001-111231"
    id_num_list = id_num.split('-')
    if 0 <= int(id_num_list[1][1:3]) and int(id_num_list[1][1:3]) < 9 :
        print("서울")
    elif 9 <= int(id_num_list[1][1:3]) and int(id_num_list[1][1:3]) < 13 :
        print("부산")

    # ex29. 문자열 다루기(split)
    letters = "Dave,David,Andy,2222,322223,LLL"
    letters_list = letters.split(',')
    for i in letters_list[0:2]:
        print(i,end=',')
    print(letters_list[2])

    # ex30. 문자열 다루기(split)
    filename = 'exer01.docx'
    filename_list = filename.split('.')
    print(filename_list[0])




if __name__ == '__main__':
    main()
