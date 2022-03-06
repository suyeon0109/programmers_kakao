def solution(n, t, m, table):

    for j in range(len(table)):
        table[j] = (int(table[j][:2]),int(table[j][3:]))
    table.sort()

    all = 0
    s = (9,0)
    bus = 1
    while bus <= n:
        cnt = 0
        for i in table[:]:

            if i[0] < s[0]:
                cnt += 1
                all += 1
                last = i
                table.remove(i)
            elif i[0] == s[0]:
                if i[1] <= s[1]:
                    cnt += 1
                    all += 1
                    last = i
                    table.remove(i)
            if cnt == m:
                break

        if s[1]+t >= 60:
            s = (s[0] + 1, s[1]+ t - 60)
        else:
            s = (s[0] , s[1]+t)
        bus += 1
    
    if cnt == m:
        if last[1] == 0:
            return str(last[0]-1).zfill(2) + ':59'
        else:
            return str(last[0]).zfill(2) + ':' + str(last[1]-1).zfill(2)
    else:
        return str(9 + t*(n-1)//60).zfill(2) + ':' + str(t*(n-1)%60).zfill(2)

print(solution(2,10,2, ["09:10", "09:09", "08:00"]))