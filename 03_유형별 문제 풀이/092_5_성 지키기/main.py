#https://www.acmicpc.net/problem/11004
# 백준 11004, K번째 수


#테스트용 입력
#import os
#file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
import sys
file = sys.stdin


# 행과 열 기준으로 비어있는 것만 찾으면 된다?


N, M = map(int, file.readline().replace('\n','').split())
array = []
for _ in range(N):
    array.append(file.readline().replace('\n',''))
    

row = [0] * N
column = [0] * M

for i in range(N):
    for j in range(M):
        if array[i][j] == 'X': # X 표시되어있는 위치와 상응하는 공간을 1로 치환
            row[i] = 1
            column[j] = 1

#각 행렬에 경비병 없는지 확인
row_count = 0
for i in range(N):
    if row[i] == 0: 
        row_count += 1
column_count = 0
for j in range(M):
    if column[j] == 0:
        column_count += 1
print(max(row_count, column_count))