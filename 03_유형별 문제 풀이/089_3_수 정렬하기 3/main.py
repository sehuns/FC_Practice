#https://www.acmicpc.net/problem/2747
# 백준 2747, 피보나치


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


n = int(file.readline().replace('\n',''))

#재귀함수
'''
이거로 풀면 타임아웃된다.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
'''

a, b = 0, 1
while n>0:
    a, b = b, a+b
    n -= 1
print(a)





