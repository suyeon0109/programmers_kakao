def solution(lines):
    for i in range(len(lines)):
        a = round(float(lines[i][17:23]),3) + int(lines[i][14:16])*60 + int(lines[i][11:13])*60*60
        b = round(float(lines[i][24:-1]),3)
        lines[i] = (round(a-b+0.001,3), a)
    
    cnt_m = 0

    for j in range(len(lines)):
        for k in range(2):
            cnt = 0
            for p in range(len(lines)):
                if lines[j][k] <= lines[p][0] < lines[j][k]+1 or lines[j][k] <= lines[p][1] < lines[j][k]+1 or lines[p][0] < lines[j][k] < lines[p][1] or lines[p][0] < lines[j][k]+1 < lines[p][1]:
                    cnt += 1
            if cnt > cnt_m:
                cnt_m = cnt

    return cnt_m