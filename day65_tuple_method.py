# the tuple inside the tuple is accepted in python.
nested_tuples =(1,2,3,(1,2,3,55,4,4,5,),(1,2,4,5),(2223,44,4,455,987))

print(nested_tuples[4]) # it is same as list we can call it by index.
print(nested_tuples[4][2]) 

# .count()
# count method is used to find the values in tuples appeared how many times
print("count")
tuple_example =(1,2,3,4,4,4,8,9,10,8,5,5,5,7,5,7,5,55,7,99,8,8,8,7)

print(tuple_example.count(4))
print(tuple_example.count(5))
print(tuple_example.count(8))

#.index find the value of a element in a value 
print("index")
tuple_example =(29,1,2,3,4,5,6,7,8,9,10,29,29,12)

print(tuple_example.index(8))
print(tuple_example.index(6))
print(tuple_example.index(7))
print(tuple_example.index(3))
print(tuple_example.index(29)) # if the value appears multiple times it will print the first instance.
print(tuple_example.index(99)) # if we find the index value that doesnot exist in a a tuple it throws a error.

