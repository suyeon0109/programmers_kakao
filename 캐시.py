def solution(n, cities):
    la = []
    time = 0
    for i in cities:
        i = i.lower()
        if i not in la:
            time += 5
            la.append(i)
            if len(la) > n:
                la.pop(0)
        else:
            time += 1
            la.remove(i)
            la.append(i)

    return time