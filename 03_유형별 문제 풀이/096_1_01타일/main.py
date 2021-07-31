#https://www.acmicpc.net/problem/1904
# 백준 1904, 01타일


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin



""" 해결 아이디어
사용할 수 있는 타일의 종류는 2개, 모든 경우의 수 
시간복잡도 N 정도로 해결 가능해야함
전형적인 동적프로그래밍 문제
한 번 계산한 값은 다시 계산하지 않는다!
메모이제이션

동적프로그래밍 문제를 위해선 점화식을 세울 수 있어야함 (인접한 항들 사이의 관계식)

길이가 i인 수열을 형성하는 방법은 2개뿐,, 
D[i] = D[i - 1] + D[i - 2] 피보나치 수열과 거의 유사함. 

"""

# 점화식을 잘 세우는게 포인트

n =  int(file.readline().replace('\n',''))

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i-2]+dp[i-1]) % 15746 # 값이 너무 커지는걸 방지하는 숫자. 없어도 되기는함..

print(dp[n])