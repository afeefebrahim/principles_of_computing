"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result =len(line)   
    s =0            
    for i in range(len(line)):
        if i+1 <len(line) and line[i] == line[i+1]:
           line[i] =line[i] +line[i]
           line[i+1] =0 
    print line   
    for i in line:
        if 0 in i:
           print i
           line.remove(0)
       
    n = result -len(line)
    for i in range(n):
        line.append(0) 
    
    return line

print merge([2,2,0,2,0,2,0,2,0,2,0,2])  

