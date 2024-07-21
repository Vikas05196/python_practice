#.format() => is used to concatenate string. in place of  concatenation "+" you can 
# can use .format

a = input("eneter a name ")
b = input("eneter a comp ")
c = input("eneter a dept ") 

print("my name is "+a+" work in a "+b+" in the department of "+c)

# using .format()

e = input("eneter a name ")
f = input("eneter a comp ")
g = input("eneter a dept ") 

print("my name is {}, work in a {}, in the department of {}".format(e,f,g))
print("my name is {} work in a {} in the department of {}".format(e,f,g))
print("my name is {} work in a {} in the department of {}".format("elot","flaot","goat"))

print("the {} {} {}".format("lazy","cara","bala"))
print("the {0} {0} {1}".format("lazy","cara","bala"))
print("the {2} {1} {0}".format("lazy","cara","bala"))


# f-string format method
print("f-string format method")
name = "vikas"
print(f"hello my name is {name }")






