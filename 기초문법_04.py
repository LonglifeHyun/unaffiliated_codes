# 파이썬 기초 04. 파이썬 튜플, 딕셔너리, 집합 퀴즈

def main():

    # ex49. 데이터 구조(튜플) // 다양한 타입의 원소, 생성 후 변경불가
    data = ('a','b','c','d','e')
    print(data[0], data[-1])

    # ex50. 튜플
    tupledata = ('dave', 'fun-coding', 'endless')
    """
    tupledata[0] = 'david'
    // tuple data cannot be changed!
    """
    tupledata = tupledata + ('david',)
    print(tupledata)

    # ex51. 튜플
    var1, var2 = 1, 2
    var1, var2 = var2, var1
    print(var1, var2)

    # ex52. 튜플
    tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
    print(tupledata[1:])

    # ex53. 튜플과 리스트
    tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
    print(type(tupledata))

    listdata = list(tupledata)
    print(listdata)
    print(type(listdata))
    listdata.append('fun-coding4')
    print(listdata)

    print("here: ", tuple(listdata))
    print("here2: ",listdata)   # 바뀌지 않았음.

    tupledata = tuple(listdata) # 이렇게 저장을 해줘야 함.
    print(tupledata)
    print(type(tupledata))

    # ex54. 튜플, 리스트, 딕셔너리
    a_tuple = ()
    b_list = []
    c_dictionary = {}

    """
    a_tuple = tuple()
    b_list = list()
    c_dictionary = dict()
    """

    print("a_tuple = ",a_tuple,", type = ",type(a_tuple))
    print("b_list = ",b_list,", type = ",type(b_list))
    print("c_dictionary = ",c_dictionary,", type = ",type(c_dictionary))


    # ex55. 딕셔너리
    eng_word = {"environment":'환경', "company":'회사', "government":'정부', "face":'얼굴'}
    print(eng_word)
    from pprint import pprint
    pprint(eng_word, width=20, indent=4)

    key_list, value_list = [], []
    for key, value in eng_word.items():
        key_list.append(key)
        value_list.append(value)
    print("key_list : ", key_list)
    print("value_list : ", value_list)

    """ OR """
    print(eng_word.keys())
    print(eng_word.values())

    key_list2 = [k for k in eng_word.keys()]
    value_list2 = [v for v in eng_word.values()]
    print("key_list2 : ", key_list2)
    print("value_list2 : ", value_list2)

    # ex56. 딕셔너리
    print("영어단어\t : 의미")
    for key, value in eng_word.items():
        if len(key)>10:
            print(key,' :',value)
        elif len(key)<7:
            print(key,'\t\t :',value)
        else:
            print(key,'\t :',value)

    # ex57. 딕셔너리
    eng_word2 = {"environment":('환경', 'X'), "company":('회사', 'O'), "government":('정부', 'X'), "face":('얼굴', 'X')}
    for key, val in eng_word2.items():
        if val[1] == 'X':
            print(key)

    # ex58. 딕셔너리
    print("hi")
    eng_word3 = {"environment":['환경', 'X'], "company":['회사', 'O'], "government":['정부', 'X'], "face":['얼굴', 'X']}
    input_word = "face" #input()
    #eng_word3[input_word] = [eng_word3[input_word][0], 'O']
    eng_word3[input_word][1] = 'O'
    pprint(eng_word3, indent=4)
    for key, val in eng_word3.items():
        if val[1] == 'X':
            print(key)

    # ex59. 딕셔너리
    dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
    dict2 = {'company': '회사', 'face':'얼굴'}
    dict3 = {'apple': '사과'}

    for k, v in dict2.items():
        dict_all[k] = v
    for k, v in dict3.items():
        dict_all[k] = v

    print("dict_all =",end="")
    pprint(dict_all, width=40, indent=8)


    # ex60. 딕셔너리
    actor_info = {'actor_details': {'생년월일': '1971-03-01',
                                    '성별': '남',
                                    '직업': '배우',
                                    '홈페이지': 'https://www.instagram.com/madongseok'},
                'actor_name': '마동석',
                'actor_rate': 59361,
                'date': '2017-10',
                'movie_list': ['범죄도시', '부라더', '부산행']}
    print("배우 이름\t\t: ",actor_info['actor_name'])
    print("홈페이지\t\t: ",actor_info['actor_details']['홈페이지'])
    print("출연 영화 갯수  : ",len(actor_info['movie_list']))

    # ex 61. 집합
    number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]
    num_set = set(number_list)
    print(num_set)
    print(type(num_set))

    # +) defaultdict
    from collections import defaultdict
    #문제: 인풋데이터 중에서 'apple'의 개수 세기.
    input_data = ['apple', 'banana', 'grape', 'apple', 'watermelon', 'banana', 'apple', 'kiwi', 'grape', 'apple', 'strawberry', 'apple']

    #defaultdict 안쓰고 그냥 for 문으로 할 때
    count=0
    for data in input_data:
        if data=='apple':
            count+=1
    print(count)

    #defaultdict 쓰면
    dict = defaultdict(int)
    for data in input_data:
        dict[data]+=1
    print(dict['apple'])

if __name__ == '__main__':
    main()
