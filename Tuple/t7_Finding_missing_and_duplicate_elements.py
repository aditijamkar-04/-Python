def finding_missing_duplicate_elements(t):
    for i in range(len(t)):
        if i==t[i]:
            return i+1,t[i]

t=(1,2,3,3,5)
print(finding_missing_duplicate_elements(t))