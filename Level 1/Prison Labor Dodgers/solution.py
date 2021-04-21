def solution(a,b):
  
  #to find the extra element in one of the lists
  c = set(a)
  d = set(b)
  
  if len(c) > len(d):
    return list(c-d)[0]
  else:
    return list(d-c)[0]
