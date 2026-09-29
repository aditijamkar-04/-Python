# Check if the given year is a leap year or not.
year=int(input("year:"))
if year%100!=0 and year%4==0 or year%400==0:
    print("yes")
else:
    print("not")