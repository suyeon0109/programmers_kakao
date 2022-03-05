def solution(dart):
    la = []
    for i in range(len(dart)):
        if dart[i] == 'D' or dart[i] == 'S' or dart[i] == 'T':
            j = 2
            while 48 <= ord(dart[i-j]) <= 57:
                j += 1
            if dart[i] == 'S':
                a = 1
            elif dart[i] == 'D':
                a = 2
            else:
                a = 3
            la.append(int(dart[i-j+1:i]) ** a)
        
        elif dart[i] == '*':
            la[-1] *= 2
            if len(la) >=2 :
                la[-2] *= 2
        elif dart[i] == '#':
            la[-1] = -la[-1]
    
    return sum(la)