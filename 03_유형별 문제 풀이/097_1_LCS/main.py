#https://www.acmicpc.net/problem/9251
# 백준 9251, LCS


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



# 난이도 : 하
# 동적프로그래밍, LIS (Longist Increasing Subs/??)
# 30분


""" 해결 아이디어
가장 긴 공통 부분수열의 대표적인 문제
N^2

D[i][j] = X[0...i]와 Y[0...j] 의 공통 부분수열의 길이를 조금씩 늘려가며 최대길이 계산 

테이블로 확인
초기화
 - 공집합 포함해서 초기화 진행

 진행
  - 일치하는 문자를 만났을 때, 대각선 왼쪽 위의 값에 + 1 한 숫자 저장

값이 같을 때는 왼쪽위의 값에 + 1
그렇지 않을때는 위, 왼쪽의 값 중 더 큰 값을 넣는다.


"""





"""
제출용 입력
import sys
file = sys.stdin
"""




x = file.readline().replace('\n','')
y = file.readline().replace('\n','')

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
 
for i in range(1, len(x) + 1):
  for j in range(1, len(y) + 1): # 한 행씩 내려가면서
    if x[i - 1] == y[j - 1]: #동일하다면 대각선 왼쪽 값 + 1
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j]) #그렇지 않다면 왼쪽과 위에 숫자 중 더 큰 값으로 ..

print(dp[len(x)][len(y)])
