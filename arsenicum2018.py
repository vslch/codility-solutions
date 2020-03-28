#solution review:
#https://app.codility.com/demo/results/trainingZ6KHYN-UR8/

from collections import namedtuple

Node = namedtuple(
    'Node', 
    [
        'left',
        'right',
        'length',
        'prev', 
        'idx'
    ]
)

def initQueue(words):
    
    queue = []
    
    for i, w in enumerate(words):
        
        lenw = len(w)
        
        for j in range(lenw + 1):
            
            z1, z2 = w[:j], w[j:]
            
            if z1 == z1[::-1]:
                n = Node(
                    left   = '',
                    right  = z2,
                    length = lenw,
                    prev   = None,
                    idx    = i
                )
                queue.append(n)
                
            if z2 == z2[::-1]:
                n = Node(
                    left   = z1,
                    right  = '',
                    length = lenw,
                    prev   = None,
                    idx    = i
                )
                queue.append(n)
                
    return queue

MAXLEN = 600000     

def solution(S):
    
    words = S.split()
    S1, S2 = set(), set()
    
    for word in words:
        l = len(word)
        S1 |= set(word[i::-1] for i in range(l))
        S2 |= set(word[-1:i:-1] for i in range(-2, -l - 2, -1))
    
    P1 = {
        s: [(i, w) for i, w in enumerate(words) 
            if w.startswith(s) or s.startswith(w)] 
        for s in S1
    }
    
    P2 = {
        s: [(i, w) for i, w in enumerate(words) 
            if w.endswith(s) or s.endswith(w)] 
        for s in S2
    }
    
    queue = initQueue(words)
    seen = set()
    found = False
    
    while len(queue) > 0:
        
        n = queue.pop()
        
        if n.right == '' and n.left == '':
            found = True
            break
            
        if (n.left, n.right) in seen:
            continue
        else:
            seen.add((n.left, n.right))
            
        if n.right == '' and n.left[::-1] in P1:
            for i, v in P1[n.left[::-1]]:
                newLength = n.length + len(v)
                if newLength <= MAXLEN:
                    l1, l2 = len(v), len(n.left)
                    if l1 > l2:
                        u = Node(
                            left   = '',
                            right  = v[l2:],
                            length = newLength,
                            prev   = n,
                            idx    = i
                        )
                        queue.insert(0, u)
                    else:
                        u = Node(
                            left   = n.left[:l2 - l1],
                            right  = '',
                            length = newLength,
                            prev   = n,
                            idx    = i
                        )
                        queue.insert(0, u)
                        
        elif n.right[::-1] in P2:
            for i, v in P2[n.right[::-1]]:
                newLength = n.length + len(v)
                if newLength <= MAXLEN:
                    l1, l2 = len(v), len(n.right)
                    if l1 > l2:
                        u = Node(
                            left   = v[:l1 - l2],
                            right  = '',
                            length = newLength,
                            prev   = n,
                            idx    = i
                        )
                        queue.insert(0, u)
                    else:
                        u = Node(
                            left   = '',
                            right  = n.right[l1:],
                            length = newLength,
                            prev   = n,
                            idx    = i
                        )
                        queue.insert(0, u)
                
    if not found:
        return 'NO'
    
    path = []
    
    while n is not None:
        path.append(n)
        n = n.prev
        
    path = path[::-1]
    palindrome = words[path[0].idx]
    
    for n in path[1:]:
        if n.prev.right == '':
            palindrome += " " + words[n.idx]
        else:
            palindrome = words[n.idx] + " " + palindrome
            
    return palindrome