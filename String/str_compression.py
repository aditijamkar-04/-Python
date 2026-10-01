# str compression
def str_comp(s):
    s1=s[0]
    count=1
    for i in range(1,len(s)):
        curr=s[i]
        prev=s[i-1]
        if prev==curr:
            count+=1
        else:
            if count>1:
                s1+=str(count)
            count=1
            s1+=curr
    return s1
    
s="aaabbcccdeeef"
print(str_comp(s))
# o/p:a3b2c3de3f