#solution review:
#https://app.codility.com/demo/results/trainingTSNCQY-V7J/

def solution(A, B, F):
    C = sorted(
		(x - y for x, y in zip(A, B)), 
		reverse=True
	)
    return sum(C[:F]) + sum(B)