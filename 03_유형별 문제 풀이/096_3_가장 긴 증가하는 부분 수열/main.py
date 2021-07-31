#https://www.acmicpc.net/problem/11053
# 백준 11053, 가장 긴 증가하는 부분 수열


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



# 난이도 : 하
# 동적프로그래밍, LIS (Longist Increasing Subs/??)
# 30분
""" 해결 아이디어
기초가 되는 꼭 알아야 함

수열의 크기가 N일때, 기본적 동적프로그래밍 알고리즘으로 O(N^2) 해결 가능

점화식
D[i] = array[i] 를 마지막으로 가지는 부분 수열의 최대 길이


처음엔 모든 원소에 대해 길이를 1로 초기화 해주고 
두번째 원소부터 확인해준다. i 인덱스 비교하고 j를 맨 왼쪽부터 비교한다? 
원소가 클 때 그 부분수열의 값에 1 더하고, 올라와 있는 값과 비교해서 더 큰 값을 남김


"""





"""
제출용 입력
import sys
file = sys.stdin
"""




n = int(file.readline().replace('\n',''))
array = list(map(int, file.readline().replace('\n','').split()))

dp = [1] * n

#n ^2 으로 문제풀이함.
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]: # 더 크다면 반복적으로 갱신함.
      dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))