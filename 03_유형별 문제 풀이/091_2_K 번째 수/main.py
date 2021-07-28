#https://www.acmicpc.net/problem/11004
# 백준 11004, K번째 수


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin





N, K = map(int, file.readline().replace('\n','').split())

array = sorted(list(map(int, file.readline().replace('\n', '').split())))

print(array[K-1])


