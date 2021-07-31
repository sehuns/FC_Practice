#https://www.acmicpc.net/problem/1715
# 백준 1715, 카드 정렬하기


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 해결 아이디어
# 가장 크기가 작은 숫자 묶음을 먼저 합쳤을 때 가장 횟수가 적다!


import heapq
 
n = int(file.readline().replace('\n',''))
heap = []



for _ in range(n):
    data = int(file.readline().replace('\n', ''))
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1: # 원소가 하나만 남을 떄까지 반복
    one = heapq.heappop(heap)
    two = heapq.heappop(heap) # 두 개의 원소를 꺼내서 더하고 결과를 푸시
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result) 