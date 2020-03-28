#certificate:
#https://app.codility.com/cert/view/certQXAAEN-GWJBD7EFAG78EQ8R/
#solution review:
#https://app.codility.com/demo/results/trainingFTYE9Q-T38/

def solution(K, M, A):
    
    N = len(A) // 2
    C = [0] * (M + 1)
    isLeader = lambda v: v > N
    
    for i, v in enumerate(A):
        if i < K:
            C[v] += 1
        else:
            C[v - 1] += 1
            
    L = set(
        i for i, v in enumerate(C, 1)
        if  isLeader(v)
    )
    
    for v1, v2 in zip(A, A[K:]):
        C[v1] -= 1
        C[v2] += 1
        C[v2 - 1] -= 1
        C[v1 - 1] += 1
        
        if isLeader(C[v2]):
            L.add(v2 + 1)
            
        if isLeader(C[v1 - 1]):
            L.add(v1)
        
    return sorted(L)