#https://www.acmicpc.net/problem/5397
# 백준 5397 키로거


#테스트용 입력
import os
f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
#import sys
#f = sys.stdin

test_case = int(f.readline())

while test_case:
    test_case -= 1

    n, m = list(map(int, f.readline().split())) # 큐 갯수, 몇 번쨰인지 궁금한 숫자 ,, 
    queue = list(map(int, f.readline().split())) # 문서의 우선순위 리스트
    queue = [(i, idx) for idx, i in enumerate(queue)]
    # 각각 튜플형태로 바꿔주는 방법. [2,1,4,3] -> [(2,0), (1,1), (4,2), (3,3)]


    count = 0
    
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]: #큐 맨 앞 원소의 중요도가 가장 크다면 (맨 앞에있다면)
            count += 1 #카운트 증가
            if queue[0][1] == m: # 그 값이 찾고있던 값이라면
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))  #맨 앞 값을 뒤로 넣어줌






