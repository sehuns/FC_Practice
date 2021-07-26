#https://www.acmicpc.net/problem/2750
# 백준 2750, 수 정렬하기


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 선택 정렬 알고리즘 ()



n = int(file.readline())
array = []
for i in range(0, n):
    array.append(int(file.readline().replace('\n','')))

array.sort()
for i in array:
    print(i)