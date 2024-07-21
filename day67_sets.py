# .add()
# add method is used to add the element in a list 
print("add")
example = {1,2,3,4,5,6,7,8,9,1,33,4,4,4,5,6,7,8} 
example.add("vikas")
print(example)

# when we add to element that already exist in a list nothing will be changed 
example.add(2)
print(example)

# .remove() method is used to remove element from a set 
print("remove.")
example_2 = {1,2,3,4,5,6,7,8,9,1,33,4,4,4,5,6,7,8} 

example_2.remove(3)
print(example_2)

# if we want to remove the elemet that does not exist in a set it will throw a error

#example_2.remove(9999)
print(example_2) # it will throw a error

print("discard")
# .discard()
# discard is used when we want to remove an element it doesnot throw the error when 
# element is not found.

example_3 = {1,2,3,4,5,6,7,8,9} 
example_3.discard(2)
print(example_3)
example_3.discard(6666) # it will not throw a error message
print(example_3)

# .clear()
# clear  method is used to remove  the element.
print("clear")
example_4 = {1,2,3,4,5,6,7,8,9} 
example_4.clear()
print(example_4)

# .copy()
# copy method is used to return a copy of element that has it own place 
print("copy")
example_5 = {1,2,3,4,5,6,7,8,9} 
example_6=example_5.copy()
print(example_6 is example_5) # it will print false because both are not same 

# .union()
# union method is used to combine two set into one set 

print("union")

example_8 = {1,2,3,4,5,6,7,8,9} 
example_9 = {10,11,12,13,16,19} 

set_union=example_8.union(example_9)
print(set_union)

# union can also be used as pipe character (|)

pipe = example_8|example_9
print(pipe)

# .intersection is used to find the common element in two sets
print("intersection")
example_12 = {1,2,3,4,5,6,7,8,9} 
example_13 = {1,2,3,4,10,11,12,13,16,19} 

s_intersction = example_12.intersection(example_13)
print(s_intersction)

# intersection can also be used by & sybol

a_intersection = example_12 & example_13
print(a_intersection)

# subtraction and .differenec()
# subtraction and difference are the same method 
# it keeps the value after removing from another sets.
print("sub")
example_21 = {1,2,3,4,5,6,7,8,9} 
example_22 = {10,11,12,13,16,19} 

sub_1 = example_21 -example_22
sub_2 = example_22 -example_21

print(sub_1)
print(sub_2)

diff_1 = example_21.difference(example_22)
diff_2 = example_22.difference(example_21)

print(diff_1)
print(diff_2)













