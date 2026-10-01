# WAP to find a no. of a's and no. b's
def find_a_and_b(s):
    a_count=0
    b_count=0
    for i in s:
        if i=="a":
            a_count+=1
        else:
            b_count+=1
    return a_count,b_count

s="aabbabababababababa"
print(find_a_and_b(s))