def avoiding_str_repeatation(s):
    s1=s[0]
    for i in range(1,len(s)):
        curr=s[i]
        prev=s[i-1]
        if prev!=curr:
            s1+=curr
    return s1
    
s="aaabbcccdeeef"
print(avoiding_str_repeatation(s))