#https://www.acmicpc.net/problem/1766
# 백준 1766, 문제집


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 해결 아이디어
# 힙과 위상정렬 같이 다루는 것
# 위상정렬이란? 순서가 정해진 작업을 차례로 실행해야 할 때 순서를 결정해줌
# 복잡도 : 노드의 갯수, 간선의 갯수 


#위상정렬
# 1. 진입차수가 0인 정점을 큐에 삽입 (시작노드)
# 2. 큐에서 원소를 꺼내 해당 원소와 간선 제거
# 3. 제거 이후 진입 차수가 0이 된 정점을 큐에 삽입
# 4. 큐가 빌 때까지 2~3 반복 
# 모든 원소를 방문하기 전에 큐가 빈다면 -> 싸이클 존재
# 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상정렬의 결과 

import heapq
 
n, m = map(int, file.readline().replace('\n','').split())
array = [[] for i in range(n+1)] # 모든 노드에 대해 자기가 어떤 노드에 연결되있는지에 대해 담음
indegree = [0] * (n + 1) # 연결당한, 간선이 이어진 노드의 진입차수가 몇인지 ?

heap = []
result = []

for _ in range(m):
    x, y = map(int, file.readline().replace('\n','').split())
    array[x].append(y) # x가 y 로 이어진다 ?
    indegree[y] += 1

# 진행 
for i in range(1, n + 1):
    if indegree[i] == 0: # 1. 진입차수가 0인 노드를 큐에 넣기
        heapq.heappush(heap, i)
        
result = []

while heap: #힙이 빌 떄까지 반복
    data = heapq.heappop(heap) #힙에서 하나를 빼서 
    result.append(data) #result 에다 담고
    for y in array[data]: # 꺼낸 데이터에서 간선이 있는 정점들에 대해 확인해서
        indegree[y] -= 1 # 진입차수 값 뺴주고
        if indegree[y] == 0: #진입차수 값이 0인 애들을 다시 힙에 push 
            heapq.heappush(heap, y)
for i in result:
    print(i, end=' ')

#더 쉽게 구현할 수는 없을까? 