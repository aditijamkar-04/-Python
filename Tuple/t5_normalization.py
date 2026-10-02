#WAP each value in  the tuple should be in the range of 0 to 1
# normalization -> nor
def nor(t):
    min_val = min(t)
    max_val = max(t)
    normalized_list = []
    for x in t:
        normalized_list.append((x - min_val) / (max_val - min_val))
    return tuple(normalized_list)

   
t=(12,45,23,11,27,17)
print(nor(t))