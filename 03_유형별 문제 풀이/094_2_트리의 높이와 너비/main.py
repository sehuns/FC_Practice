#https://www.acmicpc.net/problem/2259
# 백준 2250, 트리 높이와 너비


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 해결 아이디어
# 중위 순회는 X축 기준 왼쪽부터 방문한다는 특징
# level 값을 저장하도록 함

#노드 정의, 노드 1번이 항상 루트가 아니기때문에, parent값 설정 추가
class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, level):
    global level_depth, x  # global 변수 level 깊이와 x축 값
    level_depth = max(level_depth, level) # 글로벌 변수와 전달받은 level 중 큰 값을 level_depth
    if node.left_node != -1: # 왼쪽 노드부터 방문 
        in_order(tree[node.left_node], level + 1) #방문하면서 레벨 + 1
    
    #연산하는 부분
    level_min[level] = min(level_min[level], x) # 현재 레벨에서 가장 작고 큰값을 찾아서 나중에 구하기 위함
    level_max[level] = max(level_max[level], x)
    x += 1 #왼쪽부터 방문하기때문에 x 좌표 + 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level +1)
    

 
n = int(file.readline().replace('\n',''))


tree = {} # 딕셔너리 사용함

#초기값 정의
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1



for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1) #일단 비어있다고 초기화하고
    level_min.append(n) # 레벨이 노드의 갯수만큼 존재할 수 있게 하기 위해? 
    level_max.append(0)

# 트리 입력
for _ in range(n):
    number, left_node, right_node = map(int, file.readline().replace('\n','').split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1: #자식노드가 있을 때 자식노드의 부모노드 값으로 자신을 지정함
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number
    
# 부모노드 찾기
for i in range(1, n + 1):
    if tree[i].parent == -1: #부모노드가 -1인 (초기값인)
        root = i



in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1

#모든 레벨에 대해 넓이 값을 구해서 가장 넓을 때 레벨 값을 기록하고
# 체크하는 부분
for i in range(2, level_depth + 1):

    #문제에서 주어진 내용
    # 레벨의 너비는 그 레벨에 할당된 노드 중 
    # 가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 
    # 열 번호를 뺀 값 더하기 1로 정의한다.
    width = level_max[i] - level_min[i] + 1 
    if result_width < width:
        result_level = i
        result_width = width
#가장 넓은 레벨과 그 떄의 너비 출력
print(result_level, result_width)


