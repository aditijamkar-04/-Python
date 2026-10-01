# alphabets---> #,  Special symbols----> *,  numbers---->_
def my_replace(s):
    res=""
    for i in  s:
        if i.isalpha():
            res+="#"
        if i.isdigit():
            res+="_"
        else:
            res+="*"
    return res
    
s="gkjhdjf;woejfpiwo63t4324gfhg2394%^819238enw@E%^^^*()^*I^&QP"
print(my_replace(s))