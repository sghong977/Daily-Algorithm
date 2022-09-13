# lv2 minmax
def solution(s):
    answer = ''
    nums = s.split(' ')
    nums = [int(i) for i in nums]
    answer = str(min(nums)) + ' ' + str(max(nums))
    return answer
