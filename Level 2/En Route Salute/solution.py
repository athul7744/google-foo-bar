def solution(s):
  
  h = {}
  #separating the indexes of minions moving right and left separately
  h['>'] = []
  h['<'] = []
  salutes = 0
  
  #storing the indexes
  for i,e in enumerate(s):
    if e == '>' or e == '<':
      h[e].append(i)
      
  #if right moving index is lesser than left moving index, increase salutes by 2
  for x in h['>']:
    for y in h['<']:
      if x < y:
        salutes += 2
        
  return salutes
