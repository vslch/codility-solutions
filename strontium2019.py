#solution review:
#https://app.codility.com/demo/results/trainingMQ99AS-3KS/

from string import ascii_lowercase as letters
from itertools import groupby

def solution(words):
    
    P1 = {c : 0 for c in letters}
    P2 = {c : 0 for c in letters}
    S1 = {c : 0 for c in letters}
    S2 = {c : 0 for c in letters}
    EQ = {c : 0 for c in letters}
    MM = {c : 0 for c in letters}
    PS = {c : False for c in letters}
    
    for word in words:
            
        g = [
            (ltr, sum(1 for _ in group)) 
            for ltr, group in groupby(word)
        ]    
        
        if len(g) == 1:
            ltr, length = g[0]
            EQ[ltr] += length
            continue
            
            
        maxLtr, maxLength = max(g, key=lambda c: c[1])
        MM[maxLtr] = max(MM[maxLtr], maxLength)
        
        prefixLtr, prefixLength = g[0]
        suffixLtr, suffixLength = g[-1]
        isMaxPrefix = False
        isMaxSuffix = False
                    
        if prefixLength >= P1[prefixLtr]:
            P2[prefixLtr] = P1[prefixLtr]
            P1[prefixLtr] = prefixLength
            PS[prefixLtr] = False
            isMaxPrefix = True  
        elif prefixLength > P2[prefixLtr]:
            P2[prefixLtr] = prefixLength
            
        if suffixLength >= S1[suffixLtr]:
            S2[suffixLtr] = S1[suffixLtr]
            S1[suffixLtr] = suffixLength
            PS[suffixLtr] = False
            isMaxSuffix = True
        elif suffixLength > S2[suffixLtr]:
            S2[suffixLtr] = suffixLength
            
            
        if (isMaxPrefix and 
            isMaxSuffix and 
            prefixLtr == suffixLtr):
            
            PS[prefixLtr] = True
    
    res = 0        
            
    for ltr in letters:
        
        if PS[ltr]:
            v1 = P1[ltr] + S2[ltr]
            v2 = P2[ltr] + S1[ltr]
            z = max(v1, v2) + EQ[ltr]
        else:
            z = P1[ltr] + S1[ltr] + EQ[ltr]
        
        res = max(z, MM[ltr], res) 
        
    return res