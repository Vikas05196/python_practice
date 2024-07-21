# sets:
# set is a collection of data type which consists is same like list but doesnot 
# contain duplicates.
# sets are denoted by curly brackets {}
#  sets are unordered
# we cannot do indexing in a set

example = {1,2,3,4,5,6,7,8,9} 
set_1 = set({"a","b","c","d"})
print(example)
print(set_1)
print(type(example))
print(type(set_1))

example_duplicates = {1,2,3,4,5,6,7,8,9,1,33,4,4,4,5,6,7,8} 
print(example_duplicates) # duplicates will be removed.

# creating a empty set

exam = set()
print(exam)

# creating a set by using range 

example_2 = set(range(20))
print(example_2)

# set with different data types
a = {122,"b",True,3.25}
print(a)

# set cannot be accesed by using index 
index_xample_duplicates = {1,2,3,4,5,6,7,8,9,1,33,4,4,4,5,6,7,8} 
#print(index_xample_duplicates[6]) # it will throws a error.

# printing set by using for loop 

example_l = {1,2,3,4,5,6,7,8,9} 

for loops in example_l:
    print(loops)
    pass


# checking value exist in the set or not 
example = {1,2,3,4,5,6,7,8,9,10} 
print(10 in example) # it will print true because 10 in the example
print(12 in example) # it will print false as the 12 is not in the example.


# checking len of the list
length = {1,2,3,4,5,6,7,8,9} 
print(len(length))
# converting set to list 
print(list(length))

# finding length of the list 
print(len(list(length)))





