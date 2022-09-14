# 프로그래머스 정수삼각형 LV.3
# 카테고리가 DP라고 되어있어서 스포당했다 이런.
# 진짜 그냥 코딩하면 되는 문제라 레벨3인지 의문

def solution(triangle):
    prev_dp = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]
    
    for row in triangle:
        if len(row) < 3:
            continue
        cur_dp = [0] * len(row)
        for i in range(len(cur_dp)):
            if i == 0:
                cur_dp[i] = prev_dp[0] + row[0]
            elif i == (len(cur_dp)-1):
                cur_dp[i] = prev_dp[-1] + row[-1]
            else:
                cur_dp[i] = max(prev_dp[i-1], prev_dp[i]) + row[i]
        prev_dp = cur_dp
            
    answer = max(prev_dp)
    return answer
