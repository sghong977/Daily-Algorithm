# 2022.08.19
# 이진 변환 반복하기

def solution(s):
    count = 0
    zeros = 0
    tmp = s
    
    while(True):
        if len(tmp) < 2:
            break
        # do
        count += 1
        zeros += tmp.count('0')
        tmp = len(str(tmp).replace('0', ''))
        tmp = str(bin(tmp))[2:]
    
    answer = [count, zeros]
    return answer
