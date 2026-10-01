# str compresssion
# if no. of char is even no. of times --> a2       else---> only 'b'
def str_comp(s):
    s1 = ""
    count = 1
    for i in range(1, len(s)):
        curr = s[i]
        prev = s[i-1]
        if prev == curr:
            count += 1
        else:
            # if count is even → add char+count
            if count % 2 == 0:
                s1 += prev + str(count)
            else:  # if count is odd → add only char
                s1 += prev
            count = 1
    # handle last group
    if count % 2 == 0:
        s1 += s[-1] + str(count)
    else:
        s1 += s[-1]
    return s1

s = "aabbbccccdddeeeeff"
print(str_comp(s))
