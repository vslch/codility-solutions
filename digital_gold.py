#certificate:
#https://app.codility.com/cert/view/certUHUM8C-V4SSEFSXHD2NEE9C/
#solution review:
#https://app.codility.com/demo/results/training653BCM-Y8E/

def count(L, Q):
    
    H = [0] * L
    son1 = 0
    son2 = len(Q)
    r = 0
    
    for i in Q:
        H[i] += 1
    
    for v in H:
        son1 += v
        son2 -= v
        if son1 == son2:
            r += 1
            
    return r

solution = lambda N, M, X, Y: count(N, X) + count(M, Y)