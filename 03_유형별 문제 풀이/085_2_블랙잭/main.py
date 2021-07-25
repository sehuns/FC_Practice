#https://www.acmicpc.net/problem/2798
# 백준 2798 : 블랙잭



#테스트용 입력
#import os
#f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
import sys
f = sys.stdin

# 데이터가 남아있으면 반복동작
while True:
    data = f.readline() #list(map(int, f.readline().split()))
    if(data==""): break
    data1 = list(map(int, data.split())) # 입력받은 한 줄의 데이터를 각각 분리하여 정수형 리스트에 넣음
    data2 = list(map(int, f.readline().split()))
    #문제풀이
    num, target = data1             #첫째줄의 값을 각각 카드 갯수, 목표값
    cards = sorted(data2, reverse = True)# 카드 목록을 sorted 함수로 내림차순 정렬하여 변수에 저장
  
    sum, result = 0, 0
    for i in range (0, num):
        for j in range (i+1, num):
            for k in range (j+1, num):
                sum = cards[i] + cards[j] + cards[k]
                if sum <= target:
                    if sum > result: result = sum
    print(result)
    # 원래 내림차순 정렬하고 각 for문 진입시 target 보다 크면 해당 for문을 탈출하는것을 구현하려고 했으나
    # 생각대로 안됨
 

