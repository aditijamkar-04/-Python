# Separate positive, negative, and zero values.
n= [10, -5, 0, 20, -10, 0, 30]
positive=[]
negative=[]
zero=[]
for i in n:
    if i>0:
        positive.append(i)
    elif i<0:
        negative.append(i)
    else:
        zero.append(i)
print(positive)
print(negative)
print(zero)