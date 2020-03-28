#solution review:
#https://app.codility.com/demo/results/trainingCCAKXH-92B/

def solution(N, Q, B, C):
    
    X = sorted(
        (bucket, color, idx) for idx, (bucket, color) 
        in enumerate(zip(B, C))
    )
    
    isStart = True
    prevBucket = None
    prevColor = None
    counter = 0
    result = -1
    
    for bucket, color, index in X:
        
        cond1 = isStart == False
        cond2 = prevBucket != bucket or prevColor != color
        
        if cond1 and cond2:
            counter = 0
        
        counter += 1
        
        if counter == Q:
            if result == -1:
                result = index
            else:
                result = min(index, result)
        
        if isStart:
            isStart = False
                
        prevBucket = bucket
        prevColor = color
            
    return result