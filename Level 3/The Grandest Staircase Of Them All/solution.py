def solution(n):
    
    #Following a bottom up dynamic programming solution
    #Ex : for n = 6
    # we can have 2 staircase of base size 2
    #       *
    #       *
    # *     * *
    # * *   * *
    # and 1 staircase of base size 3 
    # *      
    # * * 
    # * * *
    # so the output should be 3
    
    #Firstly we create a memory space for the calculation of (n+2 x n+2) size
    #We use n+2 to accomodate our base cases
    #Initialize all with 0s
    #Here rows stand for bricks used and columns for step size
    mem = [[0 for x in range(0,n+2)]for x in range(0,n+2)]
    
    #Base cases
    #For 3 and 4 bricks we can have only 1 staircase at the max, less than that we will have 0
    mem[3][2] = mem[4][2] = 1
    
    #For every 2 increase in number of bricks, the base size will increase by 1
    #Ex: for 3 or 4 bricks we can have 1 staircase, for 5 or 6 bricks we can have 2 staircase and so on .. 
    for i in range(5, n+1):
        for j in range(2, i+1):
            
            #if column value [j] is 2, we will have 1 stair case more than [i-2][j], hence adding 1
            if j == 2:
                mem[i][j] = mem[i-j][j] + 1
            #else number of staircases equals, staircases at [i-j][j] + [i-j][j-1]
            #because if we have a base of size k, then n-k bricks are available to make staircases
            #on a base of size k, we can place either a staircase of size k or k-1
            #here k is represented as j
            else:
                mem[i][j] = mem[i-j][j] + mem[i-j][j-1]
    
    stairs = 0
    #finally we sum all the staircases of different sizes with n bricks
    for i in range(1,n+1):
        stairs += mem[n][i]
        
    return stairs
