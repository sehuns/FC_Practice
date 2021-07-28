#https://www.acmicpc.net/problem/1668
# 백준 1668, 트로피 진열


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin



# 오름차순으로 정렬되어있는지 확인하는 함수
def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]: # 현재 보고있는것보다 큰 것만 남김 (작아서 안보이는건 무시)
            result += 1
            now = array[i]
    return result






N= int(file.readline().replace('\n',''))

tropies = []
for _ in range(N):
    tropies.append(int(file.readline().replace('\n','')))

print(ascending(tropies))
tropies.reverse()
print(ascending(tropies))

