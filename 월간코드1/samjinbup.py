#3진법 뒤집기

def solution(n):
    tmp = n
    flip = list()
    while(True):
        q = tmp // 3
        a = tmp % 3
        flip.append(a)
        if tmp < 3:
            break
        tmp = q
    answer = 0
    for i in range(len(flip)):
        answer *= 3
        answer += flip[i]
    return answer

 
