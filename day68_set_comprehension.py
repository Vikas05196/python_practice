# set comprehension is a way to create a set 

a = {even+2 for even in range(1,11)}
print(a)

b = {even for even in range(1,11)}
print(b)

# printing the lower leeters

d = {char.lower() for char in "ABCDEFG"}
print(d)
