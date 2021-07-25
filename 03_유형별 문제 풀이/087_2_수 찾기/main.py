#https://www.acmicpc.net/problem/1920
# 수 찾기

#테스트용 입력
import os
f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
#import sys
#f = sys.stdin

while True:
    data = f.readline()
    if data == '' : break
    n = int(data)
    array = set(map(int, f.readline().split()))  # set 자료형 : 집합 표현, 중복 허용안함
    m = int(f.readline())
    x = list(map(int, f.readline().split()))
    
    for i in x:
        if i not in array:
            print('0')
        else:
            print('1')

    