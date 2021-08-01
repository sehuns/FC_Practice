#https://www.acmicpc.net/problem/1495
# 백준 1495, 기타리스트


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



# 난이도 : 중
# 동적프로그래밍
# 40분 


""" 해결 아이디어
차례대로 왼쪽부터 오른쪽으로 계산, 동적프로그래밍으로 해결

곡의 개수가 N, 볼륨의 최대값은 M

O(NM) 


모든 볼륨에 대해서 연주 가능 여부를 매번 곡이 바뀔때마다 계산하기

d[i][j+1] = i 번쨰 노래일 때 j 크기의 볼륨으로 연주 가능한지 여부
매번 검사한다

점화식
D[i][j-V[i]] = True if     D[i-1][j] = True 이전 곡을 연주했을 떄 true 라면
D[i][j+v[i]] = True if D[i-1][j] = True

이전 볼륨에 대해서 볼륨만큼 뺴고 트루로 바꿔준다? 뭔소리야

N = 3, S = 5, M = 10 일때 예시 

곡번호 1 볼륨 5
5번 T -> 5에서 5만큼 뺀 T에 T , 5만큼 더한 10 위치에 T

곡번호 2 볼륨 3
이전 곡에서 T인 위치에서 3만큼 차이나는 곳에 T로 바꿈 

....
점화식 자체가 이해가 안됨



"""





"""
제출용 입력
import sys
file = sys.stdin
"""


n, s, m = map(int, file.readline().replace('\n','').split())

array = list(map(int, file.readline().replace('\n','').split()))


dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(1, n + 1):
  for j in range(m + 1):
    if dp[i - 1][j] == 0:
      continue
    if j - array[i - 1] >= 0:
      dp[i][j - array[i - 1]] = 1
    if j + array[i - 1] <= m:
      dp[i][j + array[i - 1]] = 1

result = -1
for i in range(m, -1, -1):
  if dp[n][i] == 1:
    result = i
    break

print(result)