#solution review:
#https://app.codility.com/demo/results/training33HKZW-U7A/

from collections import namedtuple

T = namedtuple(
    'T', 
    [
        'isZero',
        'count2',
        'count5'
    ]
)

def countFactors(n, v):
    
    if n == 0:
        return 0
        
    c = 0
    
    while n % v == 0:
        c += 1
        n //= v
        
    return c   

def makeT(n):
    
    if n == 0:
        t = T(
            isZero = True,
            count2 = 0,
            count5 = 0
        )
    else:
        t = T(
            isZero = False,
            count2 = countFactors(n, 2),
            count5 = countFactors(n, 5)
        )
        
    return t
    
def zeroesT(t):
    return 1 if t.isZero else min(t.count2, t.count5)
    
def multT(t1, t2):
    
    if t1.isZero or t2.isZero:
        t = T(
            isZero = True,
            count2 = 0,
            count5 = 0
        )
    else:
        t = T(
            isZero = False,
            count2 = t1.count2 + t2.count2,
            count5 = t1.count5 + t2.count5
        )
        
    return t

def solution(A):
    
    N = len(A[0])
    
    B = [[0] * N for i in range(N)]
    B[0][0] = makeT(A[0][0])
    
    for i in range(1, N):
        t1 = B[0][i - 1]
        t2 = makeT(A[0][i])
        B[0][i] = multT(t1, t2)
        
    for i in range(1, N):
        t1 = B[i - 1][0]
        t2 = makeT(A[i][0])
        B[i][0] = multT(t1, t2)
        
    for i in range(1, N):
        for j in range(1, N):
            t0 = makeT(A[i][j])
            t1 = multT(t0, B[i][j - 1])
            t2 = multT(t0, B[i - 1][j])
            B[i][j] = min(t1, t2, key=zeroesT)
            
    return zeroesT(B[N - 1][N - 1])