def solution(s):
    o=[]
    if(len(s) % 2 == 1):
      s += "_"
    
    while s:
      o.append(s[0:2])
      s = s[2:]
    
    return o

q=solution("hullo")
print(q)