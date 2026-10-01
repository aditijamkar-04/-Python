# total substring with all possible length
# all possible substring
def substring(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            print(s[i:j])
            
            
    
s="abababababababababaabababababa"
print(substring(s))