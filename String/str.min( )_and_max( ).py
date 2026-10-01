def min_max(s):
    min_ele=max_ele=s[0]
    for i in range(1,len(s)):
        if ord(max_ele)<ord(s[i]):
            max_ele=s[i]
        if ord(min_ele)>ord(s[i]):
            min_ele=s[i]
    return min_ele,max_ele
    
s="abzrogilelc"
print(min_max(s))



# WAP max and min length word
def max_min(s):
    lst=s.split()
    max_word=min_word=lst[0]
    for ele in range (len(lst)):
        if len(lst[ele])>len(max_word):
            max_word=lst[ele]
    for ele in range (len(lst)):
        if len(lst[ele])<len(min_word):
            min_word=lst[ele]
    return min_word,max_word
        

s="This is a python programming"
print(max_min(s))