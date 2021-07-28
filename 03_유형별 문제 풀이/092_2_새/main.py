#https://www.acmicpc.net/problem/1568
# 백준 1568, 새


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin





N = int(file.readline().replace('\n',''))
result = 0
bird = 1

while N != 0: # 모든 새가 날아갈 때까지
    if bird > N: #새가 더 크면 새를 1로 만든다
        bird = 1
    N -= bird # 현재 새 만큼 뺀다
    bird += 1 # 새 1씩 증가
    result += 1 # 초 1씩 증가
print(result)

