#https://www.acmicpc.net/problem/2655
# 백준 2655, 가장 높은 탑 쌓기


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



# 난이도 : 상
# 동적프로그래밍, LIS
# 50분


""" 해결 아이디어
벽돌의 번호를 출력해야 하므로, 계산된 테이블을 역추적해야함

1. 벽돌을 ㄱ무게 기준 정렬
2. D[i] = 인덱스가 i인 벽돌을 가장 아래에 두었을 때의 최대 높이
3. 각 벽돌에 대해 확인하며 D[i] 갱신
4. 모든 0 <= j < i 에 대해 D[i]] = max (D[i],D[j] + height[i]) if area[i] > area[j])
                                    현재 보고있는 벽돌이 넓이가 더 넓다면 높이를 업데이트


점화식 자체가 이해안됨

"""





"""
제출용 입력
import sys
file = sys.stdin
"""


n = int(file.readline().replace('\n',''))
array = []

array.append((0,0,0,0))

for i in range(1, n + 1):
  area, height, weight = map(int, file.readline().replace('\n','').split())
  array.append((i, area, height, weight))


# 무게를 기준으로 정렬
array.sort(key=lambda data:data[3])

dp = [0] * (n+1)

#매 벽돌마다 비교해서 테이블 바꿔줌
for i in range(1, n + 1):
  for j in range(0, i):
    if array[i][1] > array[j][1]: # 넓을때만
      dp[i] = max(dp[i], dp[j] + array[i][2])
max_value = max(dp) #역추적
index = n
result = []


#어떻게 벽돌 쌓아야되는지
while index != 0:
  if max_value == dp[index]:
    result.append(array[index][0])
    max_value -= array[index][2]

  index -= 1

result.reverse()
print(len(result))
[print(i) for i in result] #벽돌번호 출력
