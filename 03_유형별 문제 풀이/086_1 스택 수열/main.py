#https://www.acmicpc.net/problem/1874
# 백준 1874 : 스택 수열



#테스트용 입력
import os
f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
#import sys
#f = sys.stdin

# 데이터가 남아있으면 반복동작
while True:
    data1 = f.readline()    # 한 줄씩 읽음
    if(data1==""): break    # null 값이 읽히면 프로그램 중단
    num = int(data1)        # 숫자화 하여 데이터의 갯수를 나타내는 num 변수로 받음 
    stack = []              # 스텍 리스트 
    result = []             # 결과 문자열 저장을 위한 리스트
    datas = []              # 입력받은 숫자를 저장하는 리스트
    count = 1               # 연산하는 위치를 나타내는 변수
    descent_flag = True     # 오름차순 플래그 저장 변수
    for i in range (0, num):        # 숫자 갯수만큼 한 줄씩 입력받아 문자열에 저장
        datas.append(f.readline()) 
    datas = list(map(int, datas))   # 값을 정수형으로 변환해줌
    for i in datas:                 # 리스트 값을 하나씩 뽑아서 실행
        while count <= i:           # 카운트를 리스트 값과 비교해서 카운트값이 같아질 때까지
            stack.append(count)     # 스택, 결과 추가, 카운트 +1
            count += 1      
            result.append('+')
        if stack[-1] == i:          # 스택 맨 뒷값과 리스트 값이 일치하면 팝
            stack.pop()
            result.append('-')
        else:                       # 어디에도 해당하지 않으면 NO 출력, 오름차순 플래그 false 후 for문 종료
            print('NO')
            descent_flag = False
            break
    if descent_flag : 
        for i in result:
            print(i)
