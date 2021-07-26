#https://www.acmicpc.net/problem/11650
# 백준 11650, 좌표 정렬


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


n = int(file.readline().replace('\n',''))
array = []

for _ in range(n):
    x, y = list(map(int, file.readline().split()))
    array.append((x, y))
    
array = sorted(array, key=lambda x: x[1]) # 리스트 요소중 1번쨰 요소를 기준으로 정렬
array = sorted(array, key=lambda x: x[0]) # 리스트 요소중 0번쨰 요소를 기준으로 정렬
# 혹은 그냥 sorted(array) 로 해도 동일함.

for i in array:
    print(i[0], i[1])