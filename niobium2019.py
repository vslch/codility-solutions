#certificate:
#https://app.codility.com/cert/view/cert9ME5JC-67Y8EW9M9NXMSZ3A/
#solution review:
#https://app.codility.com/demo/results/training5WNB3R-AFA/

def solution(A):
    
    makeInt = lambda s: int(s, 2)
        
    maxValue = makeInt("1" * len(A[0]))
    minValue = 0
    
    s1 = [
        makeInt("".join(str(v) for v in row)) 
        for row in A
    ]
    s2 = set(x ^ maxValue for x in s1)
    v = set(s1) | s2
    
    res = 0
    
    for y in v:
        z1 = map(lambda x: x ^ y, s1)
        z2 = sum(
            1 for x in z1 
            if x == maxValue or x == minValue
        )
        res = max(z2, res)
        
    return res