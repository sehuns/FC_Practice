#https://www.acmicpc.net/problem/1543
# 백준 1543, 문서 검색


#테스트용 입력
import os
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')


#제출용 입력
#import sys
#file = sys.stdin






while True:
    document = file.readline().replace('\n', '')
    if document=='': break
    word = file.readline().replace('\n', '')
    
    index = 0
    result = 0

    while len(document) - index >= len(word): # 문서 길이에서 인덱스를 뺀 것이 단어 길이보다 클 때만
        if document[index:index + len(word)] == word: #문자열에서 인덱스부터 인덱스 + 단어 길이까지 뽑은게 단어와 일치하면
            result += 1 # 결과 1 더하고
            index += len(word) #인덱스를 단어 길이만큼 올림
        else:
            index += 1 # 인덱스 1씩 증가
    print(result)