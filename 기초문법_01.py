# 파이썬 기초 01. 파이썬 입출력, 형 변환

def main():
    # ex1. 출력 - 문자열 출력
    print("Hello World!")

    # ex2. 출력2 - 특수문자 출력
    print("I don't like C language")
    print('I don\'t like C language')

    # ex3. 출력3 - 포맷지정 출력
    print("%.1f" %(3.141592))
    print("%.1f" %3.141592)
    print(("%.1f") %3.141592)
    print("This is %.1f hi" %(3.141592))

    # ex4. 형 변환
    print(int('720'))
    print("%s's type is %s" %('720', type('720')))
    print("%d's type is %s" %(int('720'), type(int('720'))))
    print(str(100))

    # ex5. 연산
    num1 = 2
    num2 = 4
    print("%d + %d == %d" %(num1, num2, num1+num2))
    print("%d * %d == %d" %(num1, num2, num1*num2))
    print("%d / %d == %.1f" %(num1, num2, num1//num2))
    print("%d / %d == %.1f" %(num1, num2, num1/num2))
    print("String add : '%s'+ '%s' == %s" %(str(num1), str(num2), str(num1)+str(num2)))

    # ex6. 연산 - 거듭제곱
    print(6**2)

    # ex7. 입력과 출력
    """print(int(input())+int(input()))"""

    # ex8. 입력과 출력2
    """
    n1 = int(input())
    n2 = int(input())
    print(n1+n2)
    print(n1*n2)
    print(n1/n2)
    print(n1//n2)
    """

    # ex9. 입력과 출력3
    """
    n1 = int(input())
    n2 = int(input())
    print(n1+n2)
    print(n1*n2)
    print(n1/n2)
    print(n1//n2)
    print(n1%n2)
    """

    # ex10. 입력과 출력4
    """
    n1 = int(input())
    n2 = int(input())
    print('%d + %d = %d' %(n1, n2, n1+n2))
    print('%d * %d = %d' %(n1, n2, n1*n2))
    print('%d / %d = %d' %(n1, n2, n1/n2))
    print('%d // %d = %d' %(n1, n2, n1//n2))
    print('%d %% %d = %d' %(n1, n2, n1%n2))
    """

    # ex11. 입력과 출력5
    n1 = int(input())
    n2 = int(input())
    print('%d + %d = %d' %(n1, n2, n1+n2))
    print('%d * %d = %d' %(n1, n2, n1*n2))
    print('%d / %d = %.1f' %(n1, n2, n1/n2))
    print('%d // %d = %d' %(n1, n2, n1//n2))
    print('%d %% %d = %d' %(n1, n2, n1%n2))

if __name__ == '__main__':
    main()
