# Check Armstrong number without loops
def armstrong(n):
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    if a**3 + b**3 + c**3 == n:
        return "Armstrong"
    else:
        return "Not Armstrong"

print(armstrong(153))