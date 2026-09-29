# A mysterious sequence of numbers is formed by a pattern. The sequence starts with the number 1, and each subsequent number is generated based on the previous number, but with a twist. The sequence grows based on two specific rules:
# 1. If the number is odd, the next number is number * 3 + 1.
# 2. If the number is even, the next number is number / 2.
# The sequence continues until the number reaches 1.


n=int(input("n:"))
while n!=1:
    print(n,end=",")
    if n%2!=0:
        n=n*3+1
    else:
        n=n//2
print(1)