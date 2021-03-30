def solution(n):
  
    #Coverting the string to integer
    n = abs(int(n))
    val = 0
    
    #Reducing the number until it becomes less than 1
    while n>1:
        #If the number is even, the best approach is to divide by 2 to reduce it as fast as possible
        if n % 2 == 0:
            n = n >> 1
            val += 1
        #If a number is odd, then we can either reduce or increase it to make it even so that we can divide by 2 in the next step
        #But branching in both cases to find the solution is not always optimal, we can find an optimal solution in constant time
        #If a number has remainder of 1 on dividing by 4 of if number is 3, the best option is to subract 1
        #Else the best option is to add 1
        #This can be observed by taking the last 3 bits of the odd number (001,101,011,111) - all possible combinations
        #By adding or subracting 1 and dividing accordingly we can notice that the values converge faster when we follow the rules above.
        elif n == 3 or n % 4 == 1:
            n = n - 1
            val += 1
        else:
            n = n + 1
            val += 1
    #Returning number of operations done
    return val
