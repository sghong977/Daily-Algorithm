# 월간코드챌린지1 쿼드압축
# 그냥... 전역변수 써서 탐색함. 끝.

import numpy as np

zero_one = [0,0]

def check_same(start, length, arr):
    global zero_one, visited
    x,y = start
    val = arr[x][y]
    
    if length == 1:
        visited[x][y] = 1
        zero_one[val] += 1
        return
    
    flag = False
    for i in range(x, x+length):
        for j in range(y, y+length):
            if arr[i][j] != val:
                new_len = length//2
                check_same((x,y), new_len, arr)
                check_same((x+new_len,y), new_len, arr)
                check_same((x,y+new_len), new_len, arr)
                check_same((x+new_len, y+new_len), new_len, arr)
                flag = True
                return
    if flag == False:
        visited[x:x+length][y:y+length] = 1
        zero_one[val] += 1

def solution(arr):
    global zero_one
    global visited
    
    visited = np.zeros((len(arr), len(arr)))
    check_same((0,0), len(arr), arr)
    answer = zero_one
    
    return answer
