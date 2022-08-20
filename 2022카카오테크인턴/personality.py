# 성격유형 검사

def solution(survey, choices):
    # RT, CF, JM, AN
    rcjn = {'R':0, 'C':0, 'J':0, 'A':0}
    flips = {'R':'T', 'C':'F', 'J':'M', 'A':'N'}
    
    for i in range(len(survey)):
        if survey[i][0] < survey[i][1]:
            rcjn[survey[i][0]] -= choices[i]-4
        else:
            rcjn[survey[i][1]] += choices[i]-4

    answer = ''
    for k in rcjn:
        if rcjn[k] >= 0:
            answer += k
        else:
            answer += flips[k]
            
    return answer
