def solution(maps):
    
    #Using BFS to solve the maze
    #initializing queue with first node : (0,0)
    #format : {x-coordinate,y-coordinate,break_wall}
    queue = [(0,0,False)]
    #adding first node to visited (along with wall break details)
    visited = {(0,0,False)}
    length = 0
    
    while queue:
        length += 1
        for i in range(len(queue),0,-1):
            
            #getting the element on top of queue
            i,j,break_wall = queue.pop(0)
            #if final node return length
            if i == len(maps)-1 and j == len(maps[0])-1:
                return length
            
            #checking the 4 directions
            for x,y in zip([0,0,1,-1],[1,-1,0,0]):
                next_i = i + x
                next_j = j + y
        
                if 0 <= next_i < len(maps) and 0 <= next_j < len(maps[0]):
                    break_walls = break_wall
                    if maps[next_i][next_j] == 1:
                        if break_wall == False:
                          #breaking wall if previously not broken  
                          break_walls = True
                        else:
                            #not adding children of this node because no further walls can be broken
                            continue
                     
                    #coordinates of next child appended to queue if not already visited
                    next_node = (next_i,next_j,break_walls)
                    if next_node not in visited:
                        queue.append(next_node)
                        visited |= {next_node}
