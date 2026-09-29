# i/p:10 , o/p:5
n = int(input("n:"))
binary = bin(n)[2:]     # '0b1010' --> [2:] removes the 1st 2 char "0b"  so binary ="1010"
toggle = ""
for i in binary:        # 1 → 0 → 1 → 0      loop takes one character at a time
    if i == "0":        # i = '1'    --> '1' == '0' → False
        toggle += "1"
    else: 
        toggle += "0"   # toggle='0' ---> toggle='01'......
result = int(toggle, 2)     # onvert binary 0101 to decimal....0×8 + 1×4 + 0×2 + 1×1= 5
print(result)