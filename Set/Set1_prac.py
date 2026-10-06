#1 
s1={}
print(type(s1))

#2
s2=set()
print(type(s2))

#3
s3={2,3,4,5,6,7}
for i in s3:
  print(i)

#4 add()---->adding a single elements
s3.add(1000)
print(s3)

#5 Update() ---> adding multiple elements
s3.update([45,67,90])
print(s3)
