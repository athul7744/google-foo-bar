from math import gcd

def infinity(a,b):
      
    #From several combination of numbers we can observe that if the sum of the bananas equal powers of 2 they will never loop till infinity,
    #They will always be divided equally.
    #This leaves us with numbers other than the powers of 2. Odd numbers can never be divided into 2 parts, so all odd sums will loop to infinity
    #For even numbers we can observe that if the quotient returned when the sum is divided by the greatest common divisor of both numbers is a power of 2,
    #They will not loop to infinity
    rem = int((a+b)/gcd(a,b))
    
    #For finding if a number is a power of 2, we can use the properties of binary representations. A power of 2 will have only one bit set as 1.
    #So doing binary AND operation on the number and (number - 1) will be all 0s.
    return bool(rem & (rem-1))
    
def removeFromGraph(bGraph,ind):
    
    #This function is used to remove the occurences of a certain index from the banana graph.
    #This is done to represent that this trainer has been processed and is not available for pairing.
    for i in range(len(bGraph)):
        try:
            bGraph[i].remove(ind)
        except:
            pass
    #We set the trainers children as [-1] to indicate it is not present in the graph anymore
    bGraph[ind] = [-1]
    

def solution(banana_list):
    
    #Creating a banana graph structure to hold the relationships between all the trainers and possible pairings with other trainers
    bGraph = [[] for x in range(len(banana_list))]
    
    for i,x in enumerate(banana_list):
        for j,y in enumerate(banana_list):
            if infinity(x,y):
                #For each trainer the indexes of other trainers with whom they can be paired are stored in a list
                #Finally the list of all trainers and trainers with whom they can be paired with are created
                bGraph[i].append(j)
    
    #Number of trainers to be processed
    toProcess = len(banana_list)
    #Count of unpaired trainers
    unPairedCount = 0
    
    #Now the trainers have to be matched to ensure maximum pairing between them. This is a maximum matching problem.
    #It can be solved with several algorithms like Blossoms algorithm etc. Here a simple method to match the trainers is followed. It is as follows : 
    #First the trainer with minimum number of possible pairings is found
    #If number of possible pairings are 0, the trainer is marked as processed and removed from graph. Unpaired count is increased by 1
    #Else loop through the possible pairings to find the trainer with second least possible pairings available.
    #Then these 2 trainers are paired. They are marked as processed and removed from graph.
    #Continue likewise pairing the trainer with least possible pairings with the next trainer with least possible pairings,
    #From the list of first trainer's possible pairings.
    #Until no trainers are left to process
    while toProcess > 0:
        
        #Setting index of trainer with minimum possible pairings as 0 for ease of comparison
        min_ind = 0
        for i in range(len(banana_list)):
            
            #If possible pairings of current trainer is lesser than min_index trainer or if min_index trainer has already been processed
            #And current trainer has not been processed yet
            #Set index of trainer as min_ind
            if i != 0 and ((len(bGraph[min_ind]) > len(bGraph[i]) or bGraph[min_ind] == [-1] ) and bGraph[i]!= [-1]):
                min_ind = i
        
        #If the possible pairings of selected trainer is 0 and trainer has not been processed already 
        if len(bGraph[min_ind]) == 0 and bGraph[min_ind] != [-1] :
            #The trainer is removed from graph, unpaired count is increased by 1 and toProcess has been reduced by 1
            removeFromGraph(bGraph,min_ind)
            toProcess -= 1
            unPairedCount += 1
            
        else:    
            #Setting index of second trainer as 0 for ease of comparison
            sec_ind = bGraph[min_ind][0]
            #Looping through the possible pairings of trainer with least possible pairings
            for i in range(len(bGraph[min_ind])):
                
                #Checking if trainer has not been processed already
                if i!=0 and bGraph[min_ind][i] != -1:
                    
                    #If number of possible pairings of current trainer is lesser than sec_ind trainer, setting sec_ind as current trainer
                    if len(bGraph[sec_ind]) > len(bGraph[bGraph[min_ind][i]]):
                        sec_ind = bGraph[min_ind][i]            
            
            #If selected second trainer has not been processed already
            if(bGraph[sec_ind] != [-1]):
                #The selected trainers can now be paired
                #Both trainers are removed from graph
                #toProcess is reduced by 2 
                removeFromGraph(bGraph,min_ind)
                removeFromGraph(bGraph,sec_ind)
                toProcess -= 2
    
    #Finally return the count of unpaired trainers
    return unPairedCount
        
