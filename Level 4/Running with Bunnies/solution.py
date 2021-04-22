#The time data which is provided can be used to draw a graph between all the bunnies, the entrance and the exit.
#The approach to solve this problem invloves two parts. Firstly the graph is searched for negative cycles.
#If there are negative cycles, then the negative cycle can be run enough times to generate enough time to save all the bunnies.
#Here the Floyd Warshall Algorithm is used to detect negative cycles and the shortest paths to all nodes from every node
#If there are no negative cycles, then all the states in the problem space are searched to find out the best solution based on time limit.
#For searching the state space, Depth First Search is used to go through every possible state and find the maximum amount of bunnies that can be saved.
#This problem is a variation of the travelling salesman problem which is NP hard. It has no quick solution and complexity increases as number of nodes are increased.
from copy import deepcopy

#storing the maxSavedBunnies as a global variable for access by the DFS Algorithm
maxSavedBunnies = set()

#Function to find negative cycles and shortest paths using Floyd-Warshall Algorithm
def negativeCycles(times):
    
    #Finding the shortest path
    for i in range(0,len(times)):
        for j in range(0,len(times)):
            for k in range(0,len(times)):
                
                if times[i][k] + times[k][j] < times[i][j]:
                    times[i][j] = times[i][k] + times[k][j]
    
    #If cost to go to same node is negative then a negative cycle exists
    #Returns shortest paths and if negative cycles exist
    for i in range(0,len(times)):
        if times[i][i] < 0:
            return True, times 
    return False, times

#Function to find max saved bunnies
def dfsSolution(currBunny, time, times, visited, savedBunnies):
    
    global maxSavedBunnies
    
    #Stopping search if time is beyond -999 or search reached the end of graph and time < 0 or if we have saved all the bunnies
    if time < -999 or (currBunny == len(times)-1 and time < 0) or len(times)-2 == len(maxSavedBunnies):
        return
    
    #If the end of the graph is reached and time >= 0 and
    #If length of saved bunnies in current path is greater than maximum, current value is set to maximum
    #Else if lengths are same, and IDs of bunnies in current path is lower than maximum, current value is set to maximum
    if time >= 0 and currBunny == len(times) - 1:
        if len(savedBunnies) > len(maxSavedBunnies):
            maxSavedBunnies = deepcopy(savedBunnies)
        elif len(savedBunnies) == len(maxSavedBunnies) and sum(savedBunnies) < sum(maxSavedBunnies):
            maxSavedBunnies = deepcopy(savedBunnies)
        return
    
    #Not visiting already saved bunny
    if visited[currBunny]:
        return
    
    #Marking current bunny as visited 
    visited[currBunny] = True
    
    #Adding current bunny to saved list
    #Subtracting 1 since bunny IDs start from 0 but index of first bunny node is 1
    savedBunnies.add(currBunny-1)
    
    #Moving to next bunny in graph and subtracting time taken from remaining time
    for nextBunny in range(1,len(times)):
        if currBunny != nextBunny:
            dfsSolution(nextBunny, time - times[currBunny][nextBunny], times, visited, savedBunnies)
    
    #Removing bunny from saved list and marking as not visited
    savedBunnies.remove(currBunny-1)
    visited[currBunny] = False
    
#Main solution function
def solution(times, time_limit):
    
    #Checking if negative cycles exist
    negCycles, sTimes = negativeCycles(times)
    #If negative cycles exist returning a list of all bunny IDs
    if negCycles:
        return [x for x in range(0,len(times)-2)]
    
    #Creating visited list for bunnies, entrance and exit 
    visited = [False for _ in range(len(times))]
    savedBunnies = set()
    
    #Starting from 1 to indicate first bunny, since 0 is entrance, till (length-1), since (length-1) is exit node
    #Also subtracting appropriate time from time_limit to travel to first bunny from entrance 
    for i in range(1,len(times)-1):
        dfsSolution(i, time_limit - times[0][i], times, visited, savedBunnies)
    
    #Return sorted list of bunny IDs
    return sorted(maxSavedBunnies)
