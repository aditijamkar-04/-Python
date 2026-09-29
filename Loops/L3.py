# Given a and b, find prime numbers in a given range [a,b]
a=int(input("a:"))
b=int(input("b:"))
for n in range(a, b + 1):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, end=" ")