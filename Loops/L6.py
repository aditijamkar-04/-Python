# You are given a positive integer n and an integer k. You need to rotate the digits of the number n by k places to the right
# n = 12345 and k= 2,   o/p:45123

n=input("n:")
k=int(input("k:"))
for i in range(k): 
    n=n[-1]+n[:-1]
print(n)