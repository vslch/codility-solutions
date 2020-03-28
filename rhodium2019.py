#certificate:
#https://app.codility.com/cert/view/certW7KC4Z-NESN8FGT77AWFKCT/
#solution review:
#https://app.codility.com/demo/results/trainingPH8R25-P8H/

def solution(T):
    
    N = len(T)
    M = [[0] * N for _ in T]
    
    for i, v in enumerate(T):
        if i == v:
            continue
        r = min(i, v)
        c = max(i, v)
        M[r][c] = 1
       
    for i in range(N):
        for j in range(1, N):
            M[i][j] += M[i][j - 1]
    
    for i in range(N - 2, -1, -1):
        for j in range(N):
            M[i][j] += M[i + 1][j]
    
    c = N
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            if M[i][j] == j - i:
                c += 1

    return c