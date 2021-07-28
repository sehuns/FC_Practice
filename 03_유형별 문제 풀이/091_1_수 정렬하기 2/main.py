#https://www.acmicpc.net/problem/2751
# 백준 2751, 수 정렬하기 2


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin



# 데이터 갯수가 최대 100만개이다. 
# 시간복잡도가 N log N 의 정렬 알고리즘을 사용해야 한다.
# 파이썬은 1초에 2천만~5천


# 병합 정렬 - 재귀, 분할 정복
# 앞 원소부터 차례대로 채워넣음, 3개의 변수 사용
# python3 으로 하면 시간초과, pypy3 정답처리
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2  # 배열의 중간을 뽑아서
    left = merge_sort(array[:mid])   #각각 재귀 .. 
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):  # 각 배열의 끝에 위치할 떄까지 연산
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    #한 쪽이 끝난 경우 남은 리스트를 정렬
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array






test_case = int(file.readline().replace('\n',''))

array = []
for _ in range(test_case):
    array.append(int(file.readline().replace('\n','')))
    
array = merge_sort(array)
for data in array:
    print(data)


# 내장함수 sorted 이용해도 됨. 