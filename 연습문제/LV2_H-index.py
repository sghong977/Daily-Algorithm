"""
그냥 정렬문제임.
"""
def solution(citations):
    answer = 0
    citations.sort()
    citations.reverse()
    for i in range(len(citations)):
        if citations[i] >= (i+1):
            answer += 1
        else:
            break
    return answer
