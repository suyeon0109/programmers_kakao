def solution(m, n, board):
    la = [[] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for t in range(m-1,-1,-1):
            la[i].append(board[t][i])

    while 1:
        lb = []
        for j in range(n-1):
            for k in range(len(la[j])-1):
                if la[j][k] == la[j][k+1]:
                    try:
                        if la[j][k] == la[j+1][k] == la[j+1][k+1]:
                            lb.append((j,k))
                            lb.append((j,k+1))
                            lb.append((j+1,k))
                            lb.append((j+1,k+1))
                    except:
                        pass
        cnt += len(set(lb))

        for x,y in set(lb):
            la[x][y] = 0

        for s in la:
            while 0 in s:
                s.remove(0)

        if len(set(lb)) == 0:
            break

    return cnt