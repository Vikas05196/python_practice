# list vs strings.
# list and string have similar properties 
# we can perform the same operations on list and strings.

# list => mutable(we can chnage )
# string => immutable(we cannot change )

ex_1 =[1,2,3,4]
ex_1[1] = 3333
print(ex_1)

my_str = "happy" 
#my_str[1] = "j" # we cannot change the immutable string.
print(my_str)

# creating new string from old string.
# we can use slicing to concatenate from string.

my_var = " you are very sad"
my_var_a = my_var[0:4] + ' are ' + "genious."
print(my_var_a)


# reference
# reference means we can assign one value to another value

a = 123
b = "happy"
c =a
d = b

print(c)
print(d)

list_a =[1,2,3,4]
lsit_c = list_a
list_a[1] = 4
lsit_c[2] = 3333
print(list_a)
print(lsit_c)

# why does python  have references?
# due to large amount of heavy data in a list. it will take more storage in 
# a memory due to this 
# copy module and deepcopy() module is used 
print("copy and deepcopy() methods.")
import copy

list_d = [1,2,3,4,5]
list_e = copy.deepcopy(list_d) # the copy in a deepcopy method hold the various references in a memory 
list_e[1] = 55555 # list_e value only will change due to deepcopy method. 
print(list_d)
print(list_e)

# list line continuation 

list_z =[1,2, # list follows the next line continuation.
         3,
         4,
         5,6,7]
print(list_z)

# backward \ is used as a continuation of any string.

var_a = 1 + 3 \
+4\
+1000
print(var_a)

# line continuation in string
# backward \  is usd at the end of string to write more than one line.
string_a = "you are a \
great human\
 being "
          
print(string_a)
