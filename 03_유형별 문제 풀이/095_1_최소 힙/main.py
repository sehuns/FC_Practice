#https://www.acmicpc.net/problem/1927
# 백준 1927, 최소 힙


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 힙 자료구조에 대한 이해를 묻는 기초문제
# 작은 원소가 부모로 들어가는 구조

import heapq
 
n = int(file.readline().replace('\n',''))
heap = []
result = []



for _ in range(n):
    data = int(file.readline().replace('\n', ''))
    
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap)) #heappop : 꺼낸다, push 넣는다
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)

