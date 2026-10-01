def pallidromic_substring(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            str=s[i:j]
            if is_pallidrome(str):
                print(str)
def is_pallidrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
    
s="abababababababababaabababababa"
print(pallidromic_substring(s))