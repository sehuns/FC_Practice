#https://www.acmicpc.net/problem/4195
# 백준 4195, 친구 네트워크

# 해시를 활용한 union find 알고리즘 (집합 표현) 합집합 찾기
# 딕셔너리 자료형 사용 

#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')






#제출용 입력
#import sys
#file = sys.stdin

def find(x):
    if x == parent[x]:      # 부모를 재귀적으로 찾음
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y] #네트워크의 크기 값을 더함



test_case = int(file.readline())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(file.readline())
    for _ in range(f):
        x, y = file.readline().replace('\n','').split(' ')
        
        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])

# 추후 복습필요