#https://www.acmicpc.net/problem/1939
# 백준 1939, 중량제한


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 난이도 중상
#이진탐색 + 추가 탐색
# 반복적으로 중량을 설정하며 이동이 가능한 경우를 찾는다. BFS
#중량설정범위는 최소중량부터 최대중량까지, 
# 시작은 최소중량부터, 최적 중량 찾기위해 중간값일때부터 확인? 
# 가능하면 더 무거운 중량 계산 위해 최소중량 += 중간중량
# 불가능하면 중량 감소

from collections import deque


N, M = list(map(int, file.readline().replace('\n','').split()))
adj = [[] for _ in range(N+1)]

# 경로가 있는지 탐색하는 전형적이고 기본적인 알고리즘 소스코드 부분
def bfs(C):
    queue = deque([start_node])
    visited = [False] * (N + 1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= C:
                visited[y] = True
                queue.append(y)

    return visited[end_node]

start = 1000000000
end = 1

#연결된 각각 간선 정보 받아서 초기화해줌
for _ in range(M):
    x, y, weight = map(int, file.readline().replace('\n','').split())
    adj[x].append((y, weight)) 
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, file.readline().replace('\n','').split())

result = start
#이진탐색
while(start <= end):
    mid = (start + end) // 2 # mid는 현재 중량
    if bfs(mid): #이동이 가능하면 중량 증가
        result = mid
        start = mid + 1

    else:
        end = mid - 1 # 이동 불가하면 중량 감소
print(result)

#복습필요