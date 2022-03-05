def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        if len(arr1[i]) < n:
            arr1[i] = '0'*(n-len(arr1[i])) + arr1[i]
        if len(arr2[i]) < n:
            arr2[i] = '0'*(n-len(arr2[i])) + arr2[i]

        m = ''

        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                m += '#'
            else:
                m += ' '
        
        answer.append(m)
    return answer
