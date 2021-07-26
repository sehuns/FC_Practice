#https://www.acmicpc.net/problem/10814
# 백준 10814, 나이순 정렬


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


n = int(file.readline().replace('\n',''))
array = []

for _ in range(n):
    age, name = file.readline().split()
    array.append((int(age), name))
    
array = sorted(array, key=lambda x: x[0]) # 리스트 요소중 0번쨰 요소를 기준으로 정렬

for i in array:
    print(i[0], i[1])