#https://www.acmicpc.net/problem/7490
# 백준 7490, 0 만들기


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


#문제에서 주어진 N의 범위가 좁기때문에, 완전탐색으로 해결 가능
# 핵심 아이디어 : 수 리스트와 연산자 리스트를 분리해 경우의 수 계산
# 연산자리스트는 항상 3^n-1 만큼 존재함 

import copy


#재귀적으로 모든 연산자에 대한 리스트를 구하는 함수
#재귀적 호출하면서 연산자를 추가해줌
def recursive(array, n): # array는 호출될 때마다 매개변수로 들어가서 함수 호출됨, 경우의 수를 다 진행
    if len(array) == n:  # array 가 N 만큼의 길이를 가지면 멈춤
        operators_list.append(copy.deepcopy(array))  # 동일한 array를 공유하기때문에, 그대로 진행하면 팝 되고 난 빈 어레이만 남는다. 
                                                    # 파이썬 deepcopy 함수 사용해 해결
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()




test_case = int(file.readline().replace('\n',''))

for _ in range(test_case):
    operators_list = []                 # 연산자 리스트 
    n = int(file.readline().replace('\n',''))
    recursive([], n-1)

    integers = [i for i in range(1, n+1)] # n 만큼 숫자가 있는 리스트 생성

    for operators in operators_list :     # 연산자 리스트에서 하나씩 뺴서 
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operators[i]   #숫자와 연산자를 조합시킴
        string += str(integers[-1])
        # 파이썬 eval 함수 : 문자열 형태의 수식을 계산해줌
        if eval(string.replace(" ", "")) == 0: # 공백 제거한 후 연산값이 0이면 출력
            print(string)

    print()