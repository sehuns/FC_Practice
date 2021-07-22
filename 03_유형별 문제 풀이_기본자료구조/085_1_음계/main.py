#https://www.acmicpc.net/problem/2920
# 백준 2920 : 음계



#테스트용 입력
import os
f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
#import sys
#f = sys.stdin

# 데이터가 남아있으면 반복동작
while True:
    data = f.readline() #list(map(int, f.readline().split()))
    if(data==""): break
    data = list(map(int, data.split())) # 입력받은 한 줄의 데이터를 각각 분리하여 정수형 리스트에 넣음

    #아래부터 문제풀이
    # 핵심 아이디어 : 리스트에서 원소를 차례대로 비교, 두 원소를 기준으로 오름/내림차순 여부 체크
    ascending = True 
    descending = True

    for i in range(1, 8):
        if data[i] > data[i - 1]: # 리스트의 값을 뽑아 비교하고, 조건에 부합할 시 플래그를 false로 바꿈
            descending = False
        elif data[i] < data[i - 1]:
            ascending = False
        
    if ascending:
        print('ascending')

    elif descending:
        print('descending')
        
    else:
        print('mixed')

