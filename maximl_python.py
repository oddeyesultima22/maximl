chars = 256
def dis_char(str, n): 
    count = [0] * chars 
    for i in range(n): 
        count[ord(str[i])] += 1
    dist = 0
    for i in range(chars): 
        if (count[i] != 0): 
            dist += 1    
    return dist 
  
def substr_char(str): 
    n = len(str) 
    dist = dis_char(str, n) 
    minlen = n
    for i in range(n): 
        for j in range(n): 
            sstr = str[i:j] 
            sstr_len = len(sstr) 
            sstr_char = dis_char(sstr,  sstr_len) 
            if (sstr_len < minlen and dist == sstr_char): 
                minlen = sstr_len 
    return minlen 

str = input()
l = substr_char(str); 
print(l)
