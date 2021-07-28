#https://www.acmicpc.net/problem/1302
# 백준 1302, 베스트셀러


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin





N = int(file.readline().replace('\n',''))

books = dict()
for _ in range(N):
    book = str(file.readline().replace('\n',''))
    if book not in books: # 책이 없으면 
        books[book] = 1 # 그 책 이름 숫자 1
    else:
        books[book] += 1 # 책 있으면 1 더함
target = max(books.values()) # max 함수는 가장 큰 값을 가져오는 함수
array = []

for book, number in books.items(): #아이템을 확인하면서 
    if number == target: # 위에서 구한 가장 숫자가 높은 값과 일치하는것에 적중하면
        array.append(book) # 어레이에 추가 ..? 
    
print(sorted(array)[0])