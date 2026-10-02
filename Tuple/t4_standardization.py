def std(t):
    sum=0
    mean=0
    var=0
    sd=0
    result=[]
    for i in t:
        sum+=i
    mean=sum/len(t)
    for i in t:
        var+=(i-mean)**2
    var/=len(t)
    sd=var**0.5
    for i in t:
        res=(i-mean)/sd
        result.append(res)
    return tuple(result)

t=(3,4,5,6,7,8,9,10) 
print(std(t))