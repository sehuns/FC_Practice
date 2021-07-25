#https://www.acmicpc.net/problem/10930
# 백준 10930 SHA-256


#테스트용 입력
#import os
#f = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')



#제출용 입력
from os import closerange
import sys
f = sys.stdin

import hashlib

data = f.readline().replace('\n','')
encoded_data = data.encode()
print(hashlib.sha256(encoded_data).hexdigest())