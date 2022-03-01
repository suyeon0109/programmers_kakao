def solution(str1, str2):
    la = []
    lb = []
    lc = []
    for i in range(len(str1)-1):
        for j in str1[i:i+2]:
            if 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
                pass
            else:
                break
        else: 
            la.append(str1[i:i+2])

    for i in range(len(str2)-1):
        for j in str2[i:i+2]:
            if 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
                pass
            else:
                break
        else: 
            lb.append(str2[i:i+2])
            
    if not la and not lb:
        return 65536
    
    for k in range(len(la)):
        la[k] = la[k].lower()
    for k in range(len(lb)):
        lb[k] = lb[k].lower()

    for q in la[:]:
        if q in lb:
            lc.append(q)
            lb.remove(q)
    ld = la+lb

    answer = int(len(lc)/len(ld)*65536)
    return answer

print(solution('aa1+aa2', 'AA12'))