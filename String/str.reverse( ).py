def my_reverse(s):
    s1=list(s)
    i=0
    j=len(s1)-1
    while i<j:
        s1[i],s1[j]=s1[j],s1[i]
        i+=1
        j-=1
    return s1

s="xanbp" 
print(my_reverse(s))