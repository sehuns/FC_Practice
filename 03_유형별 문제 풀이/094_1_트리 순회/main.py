#https://www.acmicpc.net/problem/1991
# 백준 1991, 트리 순회


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin


# 기본적인 유형, 자주 나옴
# 전위 순회, 중위 순회, 후위 순회


# 파이썬에서 클래스를 사용하는 법은 C에서 struct 사용하는거랑 비슷함.
# 자료형을 하나 만든다

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    print(node.data, end='') #자기자신 출력 후 왼쪽 오른쪽 방문하고
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != '.': #왼쪽 방문하고
        in_order(tree[node.left_node])
    print(node.data, end='') # 루트 처리하고
    if node.right_node != '.':
        in_order(tree[node.right_node])# 오른쪽 방문

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')



n = int(file.readline().replace('\n',''))


tree = {} # 딕셔너리 사용함
for i in range(n):
    data, left_node, right_node = file.readline().replace('\n','').split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])





