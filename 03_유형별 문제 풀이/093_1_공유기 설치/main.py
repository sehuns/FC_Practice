#https://www.acmicpc.net/problem/2110
# 백준 2110 , 공유기 설치


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 범위가 10억 단위이므로, 이진탐색 N log N 알고리즘을 사용해야함. 
# 보통 숫자가 크면 이진탐색 고려해야함
# 이진탐색은 min과 max 값으로 탐색함


# 집의 위치정보를 받고 정렬 수행
# 가장 거리가 먼 집 까지의 거리 구하고, 중간 값을 반복적으로 찾고 확인함
# 첫번째에  놓고, 중간 값보다 큰 수가 나올때 다시 설치해보고 
# 공유기가 남으면, gap을 감소시킴





N, C = list(map(int, file.readline().replace('\n','').split()))
array = []
for _ in range(N):
    array.append(int(file.readline().replace('\n','')))
array = sorted(array)
start = array[1] - array[0] #start = 첫번쨰와 다음원소의 차이
end = array[-1] - array[0] # end = 마지막과 첫원소의 차이
result = 0


while(start <= end): # star와 end가 같거나, start가 더 커지기 전까지 
    mid = (start + end) // 2 # mid 는 Gap 을 의미함
    value = array[0] # 시작하는 값
    count = 1
    for i in range(1, len(array)): # 모든 원소를 대상으로 설치 가능한지 계산
        if array[i] >= value + mid:  # 
            value = array[i]
            count += 1
    if count >= C:  # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1  # 더 많은 경우의 수를 검색하기 위해 start를 올려준다? 
        result = mid # 가장 인접한 공유기 사이 거리를 result로 일단 저장하고 
    else:   # C 개 이상 설치 불가 경우
        end = mid - 1   

print(result)

#언어 자체는 알겠는데, 알고리즘을 짜는 과정이 이해가 안됨
# 다른 풀이 봐야할듯
# 백준에서 채점하면 틀리다고 나옴
