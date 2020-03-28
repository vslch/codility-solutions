#certificate:
#https://app.codility.com/cert/view/certDDTWGW-XRW8D9MJ58P2WKJY/
#solution review:
#https://app.codility.com/demo/results/trainingCZ5W7E-829/

def solution(A):
    
    nrows = len(A)
    ncols = len(A[0])
    
    B = [[0] * ncols for _ in range(nrows)]
    B[0][0] = A[0][0]
    
    for i in range(1, ncols):
        B[0][i] = B[0][i - 1] * 10 + A[0][i]
        
    for i in range(1, nrows):
        B[i][0] = B[i - 1][0] * 10 + A[i][0]
        
    for j in range(1, ncols):
        for i in range(1, nrows):
            c1 = B[i][j - 1] * 10 + A[i][j]
            c2 = B[i - 1][j] * 10 + A[i][j]
            B[i][j] = max(c1, c2)
            
    return str(B[nrows - 1][ncols - 1])