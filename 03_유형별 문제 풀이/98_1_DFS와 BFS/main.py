#https://www.acmicpc.net/problem/1260
# 백준 1260, DFS BFS


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



# C++로 푼 적 있음...
"""

제출용 입력
import sys
file = sys.stdin

"""

from collections import deque

def dfs(v): # dfs는 재귀적으로 구현 (스택)
    print(v, end=' ')
    visited[v] = True #방문하면 True로 바꾸고 
    for e in adj[v]:
        if not(visited[e]): #방문 안한거 만나면 재귀호출, 아니면 그냥 끝남
            dfs(e)

def bfs(v): # bfs는 반드시 큐가 필요함. 
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)



n, m, v = map(int,file.readline().replace('\n','').split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, file.readline().replace('\n','').split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)


