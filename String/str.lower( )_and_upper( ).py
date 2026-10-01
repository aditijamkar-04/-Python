# if converting lower case to upper case---->ASCII-32
# if converting upper case to lower case---->ASCII+32

def convert(s):
    res=""
    for char in s:
        if ord(char)>=65 and ord(char)<97:
            var=ord(char)+32
            res+=chr(var)
        else:
            var=ord(char)-32
            res+=chr(var)
    return res
    

s="MaYuR"
print(convert(s))



def my_upper(s):
    res=""
    for i in s:
        var=ord(i)-32
        res+=chr(var)
    return res

s="mayur"
print(my_upper(s))