# 프로그래머스 야근지수 LV.3
# 이슈에 적어둠 (closed)
from heapq import heapify, heappop, heappush

# max값 구해서 pop 하는거랑 정렬이 빠른 것... 힙?
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]
    heapify(works)  # 앗 이걸 안했다
    for i in range(n):
        aa = heappop(works)    # largest work
        if aa >= 0:
            return 0
        heappush(works, aa + 1)
    
    answer = 0
    for i in works:
        answer += i ** 2
    
    return answer
