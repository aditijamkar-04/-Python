# Write a Python program to create a tuple containing multiple data types.
# Include strings, floats, integers, and booleans in the tuple.
# Assign the values directly while creating the tuple.
# Print the tuple to display all its elements.

s, f, i, b = input().split()
t = (s, float(f), int(i), b == "True")
print(t)
