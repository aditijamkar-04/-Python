n=int(input("n:"))
max_digit=0
min_digit=9
while n>0:
    digit=n%10
    if max_digit<digit:
        max_digit=digit
    if min_digit>digit:
        min_digit=digit
    n//=10
print("Largest digit",max_digit)
print("Smallest digit",min_digit)