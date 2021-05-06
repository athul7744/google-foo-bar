from math import sqrt, floor

#To solve this problem the value of root(2) upto a 100 decimal places has to be found
#It is impossible to iterate 10^100 times and calculate the exact value. An alternative method has to be found.
#A sequence like Σ floor(sqrt(2)*n) from 1 to n is called a Beatty Sequence
#Using another theorem called Rayleighs Theorem, a summation of a Beatty Sequence can be converted into a recurrence relation.
#A recurrence relation breaks a complex formula into a simpler formula. This reduces the number of steps required to calculate large values
#For instance, taking n as 10^100, the recurrence relation calculates the sum in approximately 262 steps instead of 10^100 steps using a for loop.
#This massively reduces the time required to caluclate the sum of this Beatty Sequence.

#This is the value of (root(2)-1)^100. This is required in the recurrence relation. It is hardcoded since it does not change for every iteration.
sqrt_val = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def summation(n):
    
    global sqrt_val
    
    #root case
    if n == 0:
        return 0
    
    #This is the recurrence relation
    #S(√2,n)= nn′ + n(n+1)/2 − n′(n′+1)/2 − S(√2,n′)
    #where n′ = floor((√2 - 1)*n)
    n1 = (sqrt_val*n)//10**100
    
    #Calling the recurrence relation recursively until n′ becomes 0
    return n1*n + (n*(n+1))/2 - (n1*(n1+1))/2 - summation(n1)

def solution(s):
    #Returning the output as String
    return str(int(summation(int(s))))
