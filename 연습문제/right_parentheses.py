# 레벨 2
# 스택
def solution(s):
    answer = True
    tmp = 0
    for par in s:
        if par == ')':
            tmp -= 1
        else:
            tmp += 1
        if tmp < 0:
            answer = False
            break
    if tmp != 0:
        answer = False
            
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
