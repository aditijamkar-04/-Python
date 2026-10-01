def my_sort(s):
    s1=list(s)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if ord(s1[i])>ord(s1[j]):
                s1[i],s1[j]=s1[j],s1[i]
    return s1
        
    
s="xanbp" 
print(my_sort(s))