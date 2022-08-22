# 1트 (2022.08.22)
# 정답이 틀림. 깃이슈 참고

from collections import deque

def solution(a):
    left_min1, left_min2, right_min1, right_min2 = deque(),deque(),deque(),deque()
    for i in range(len(a)):
        ##### left min
        if i == 0:
            left_min2.append(1000001)
            left_min2.append(1000001) #?
            left_min1.append(1000001)
            left_min1.append(a[i])
        elif i == (len(a)-1):
            continue
        # add
        elif a[i] < left_min1[-1]:
            left_min2.append(left_min1[-1])
            left_min1.append(a[i])
        elif a[i] < left_min2[-1]:
            left_min1.append(left_min1[-1])
            left_min2.append(a[i])
        else:
            left_min1.append(left_min1[-1])
            left_min2.append(left_min2[-1])            
    
        ###### right min
        j = len(a) - i -1
        if i == 0:
            right_min2.append(1000001)
            right_min2.appendleft(1000001) #?
            right_min1.append(1000001)
            right_min1.appendleft(a[j])
        elif a[j] < right_min1[0]:
            right_min2.appendleft(right_min1[0])
            right_min1.appendleft(a[j])
        elif a[j] < right_min2[0]:
            right_min1.appendleft(right_min1[0])
            right_min2.appendleft(a[j])
        else:
            right_min1.appendleft(right_min1[0])
            right_min2.appendleft(right_min2[0])            
    # check
    if len(a) < 3:
        return len(a)
    answer = 2
    left_min1.popleft()
    left_min2.popleft()
    right_min1.popleft()
    right_min2.popleft()
    #print(a)
    #print(left_min1, left_min2)
    #print(right_min1, right_min2)
    for i in range(1,len(a)-1):
        #print(a[i], left_min1[i], right_min1[i])
        if a[i] < left_min1[0]:
            if a[i] < right_min2[0]:
                answer += 1
        elif a[i] < right_min1[0]:
            if a[i] < left_min2[0]:
                answer += 1            
        left_min1.popleft()
        left_min2.popleft()
        right_min1.popleft()
        right_min2.popleft()
                
    return answer
