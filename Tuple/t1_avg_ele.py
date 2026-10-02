#WAP to find avg of element of the tuple
def avg_tuple(t):
    sum=0
    svg=0
    for i in t:
        sum+=i
    avg=sum/len(t)
    return avg

t=(2,3,4,5,6,7)
print(avg_tuple(t))