#https://www.acmicpc.net/problem/1074
# 백준 1074, Z


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin

#Z 모양 구성하는 4가지 방향에 대해 차례대로 재귀적 호출

def solve(n, x, y):
    global result
    if n == 2:  #함수의 크기가 2x2 에 적중할 때만 연산 진행
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result+= 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    #각각 4가지 위치에 대해 재귀적 호출
    #글로벌 변수 result 이용해서 검사할 때마다 1씩 더하는 방법으로 몇번째인지 카운트
    solve(n/2, x, y)
    solve(n/2, x, y+n/2)
    solve(n/2, x+n/2, y)
    solve(n/2, x+n/2, y+n/2)


result = 0
N, X, Y = map(int, file.readline().replace('\n','').split())
solve(2 ** N, 0, 0) #의 N제곱, 0,0 부터 시작


# 풀이대로 하면 시간초과 남. 다시해야함.
