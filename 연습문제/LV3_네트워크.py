"""
프로그래머스 BFS/DFS 카테고리의 LV3.네트워크

아 그냥 visited 전부 1 될때까지 BFS/DFS 돌려가지고 개수 세라는거잖아.
근데 처음 풀때 문제 잘못봤어서 이상한 코드 짰던 기록 이슈에 하나 남겨둠
"""
from collections import deque
def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    # 네트워크 최대 개수는 n
    for root in range(n):
        if visited[root] == 1:
            continue
        # 방문 시작!
        answer += 1
        
        tree = deque()
        tree.append(root)
        while len(tree) != 0:
            node = tree.popleft()
            visited[node] = 1
            
            # 인접행렬 보고 다음 방문할거 넣어줌
            for i in range(n):
                if visited[i] == 1: continue
                if computers[node][i] == 1:
                    tree.append(i)
        # 전부 방문을 했으면 끝
        if 0 not in visited:
            break
    
    
    return answer
