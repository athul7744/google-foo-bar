def solution(xs):
    
    #if only 1 element is present, return it
    if len(xs) == 1:
        return str(xs[0])
    
    #array of non-zero positive and negative numbers
    pos = []
    neg = []
    
    for e in xs:
        if e>0:
            pos.append(e)
        elif e<0:
            neg.append(e)
    
    #removing negative number with smallest absolute value, if len(neg) is odd 
    if len(neg)%2 !=0:
        neg.remove(max(neg))    
    
    #if only zeroes were present in xs, return 0
    #else if only 1 negative number was pesent and rest were 0s, return 0
    if len(pos) ==0 and len(neg) ==0:
        return '0'
    
    #return product of all valid numbers
    return str(reduce(lambda a,b : a*b,pos+neg,1))
