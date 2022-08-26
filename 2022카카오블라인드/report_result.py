# Issue 3번에 풀이과정 적어둠

def solution(id_list, report, k):
    report_cnt = [0]*len(id_list)
    name2id = dict()
    for i in range(len(id_list)):
        name2id[id_list[i]] = i
    adj_list=[]
    for i in range(len(id_list)):
        adj_list.append([])
             
    # before loop, dup reduce in report
    # 여기 엣지 중복제거 과정에서 시간초과가 날수 있으니 유의하자
    result = []
    #for value in report:
    #    if value not in result:
    #        result.append(value)
            
    result = list(set(report))
    
    for r in result:
        fr, to = r.split(' ')
        report_cnt[name2id[to]] += 1
        adj_list[name2id[fr]] += [name2id[to]]
    
    # check if report_cnt >1
    answer = []
    for i in adj_list:
        cnt = 0
        for j in i:
            if report_cnt[j] > (k-1):
                cnt += 1
        answer.append(cnt)
    return answer
