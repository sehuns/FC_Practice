#https://www.acmicpc.net/problem/1966
# 백준 1966 프린터 큐


#테스트용 입력
import os
f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
#import sys
#f = sys.stdin

test_case = int(f.readline())

while test_case:
    test_case -= 1

    data = f.readline() # 데이터 받기
    data = data.replace('\n', '') # 개행문자 제거
# 스택을 두개 만들고 커서를 중간에 둔다? 
    stack_left = []
    stack_right = []
    for i in data:
        if i == '-':                # - : 왼쪽스택이 있으면 한 자리 지움
            if stack_left:
                stack_left.pop()
        elif i == '<':              #왼쪽 화살표 만나면 왼쪽 하나 뽑아서 오른쪽에 추가함
            if stack_left:
                stack_right.append(stack_left.pop())
        elif i == '>':
            if stack_right:
                stack_left.append(stack_right.pop())
        else:
            stack_left.append(i)    # 기호가 아니면 스택에 추가함
    stack_left.extend(reversed(stack_right)) #오른쪽 스택은 순서가 반대로 되어야 하기 때문에 reverse 사용
    print(''.join(stack_left))      #문자열 형태로 출력함

