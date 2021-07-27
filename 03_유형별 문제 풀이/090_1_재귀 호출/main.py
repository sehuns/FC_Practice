#https://www.acmicpc.net/problem/10989
# 백준 10989, 수 정렬하기3


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin

#파이썬 기본 라이브러리로는 타임아웃될거임.
#수의 범위가 제한적인 계수 정렬 알고리즘(counting sort)
#index 적중 시 값을 1씩 증가시킴


n = int(file.readline().replace('\n',''))
array = [0] * 10001

for _ in range(n):
    x = int(file.readline().replace('\n',''))
    array[x] += 1
    


for i in range(10001): 
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
