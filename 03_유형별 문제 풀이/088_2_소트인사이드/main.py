#https://www.acmicpc.net/problem/1427
# 백준 1427, 소트인사이드


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


array = str(file.readline().replace('\n','')) # 입력받은 숫자를 문자열로 반환
for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')