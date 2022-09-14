# LV 2.
# N개의 최소공배수
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12953

"""
푸는데 30분 걸렸음.
코딩테스트가 익숙하지 않아서 그런 듯

1. 100 이하의 소수를 구해야했다. (루트 N까지 나누기 검사해서 체크함)
2. 배열 안에 있는 숫자를 소인수분해 해야했다. 미리 구해둔 소수 리스트를 가지고 체크했다.
3. 소인수분해 배열을 가지고 최대공약수를 계속 업데이트하도록 했다.
"""

import math
def solution(arr):
    answer = 0
    lcm = 1
    primes = [2, 3]
    for num in range(4, 101):
        # check is prime and add to "primes"
        tmp = True
        for c in range(2, math.floor(math.sqrt(num))+1):
            if num % c == 0:
                tmp = False
                break
        if tmp:
            primes.append(num)
    lcms = [0] * len(primes)
    
    for num in arr:
        # get component
        cnt = [0] * len(primes)
        tmp = num
        for i in range(len(primes)):
            if tmp == 1: break
            # if component
            while tmp % primes[i] == 0:
                tmp = tmp // primes[i]
                cnt[i] += 1
        for i in range(len(lcms)):
            lcms[i] = max(cnt[i], lcms[i])

    for i in range(len(lcms)):
        if lcms[i] > 0:
            lcm *= (primes[i] ** lcms[i])
    return lcm
