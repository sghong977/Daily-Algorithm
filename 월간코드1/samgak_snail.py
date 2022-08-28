# 프로그래머스 삼각 달팽이 문제
# '이슈 4번' 설명 참고

from collections import deque

def solution(n):
    answer = []
    
    lists = []
    for i in range(n+1):
        lists.append([0]*i)
    
    done = deque()
    for i in range(1,n//2 + 1):
        done.append(i)
        done.append(n-i+1)
    if n % 2 == 1:
        done.append(n//2+1)
    
    #print("DONE", done)
    done.popleft()
    cur = 1
    cur_x = 1
    lists[1][cur_x-1] = 1    
    
    for i in range(2, int(n*(n+1)/2)+1):
        #print(cur, done[0])
        
        # 현재 y축이 목표지점이었다면?
        if cur == done[0]:
            # 다 채웠다면? -> 다음 목표 y로 가야지
            if 0 not in lists[cur]: 
                aa = done.popleft()
                
                # y가 증가해야하면? (2 -> 7 이런거)
                if done[0] < aa:
                    cur -= 1
                    cur_x -= 1
                    lists[cur][cur_x-1] = i  
                # y가 감소해야하면? (7->2 이런거)
                else:
                    cur += 1
                    lists[cur][cur_x-1] = i   
            # 다 못채웠다면? -> 일단 다 채우고 얘기하렴
            else:
                cur_x += 1
                lists[cur][cur_x-1] = i    
                
        # 이 경우, 증가시키면서 1 -> 4
        elif cur < done[0]:
            cur += 1
            lists[cur][cur_x-1] = i  
            
        elif cur > done[0]:
            if lists[cur-1][cur_x-2] == 0:
                cur -= 1
                cur_x -= 1
                lists[cur][cur_x-1] = i
            else:
                # 여기가 예외케이스였음 (n=9 설명참고)
                cur += 1
                lists[cur][cur_x-1] = i
                aa = done.popleft()
                
    #print(lists)
    
    for l in lists:
        answer += l
    #print(answer)
    return answer
