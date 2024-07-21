#string:
# string is stored in a double quotes amd single quotes 
# everything enclosed in a single quote is called string 

a1 = "this is a string "
a2 = 'this is also a string '
a3 =" "
a4 = "1235"
a5 = "!@#$%^&&**(())"
a6 = "are you a LIAR eee./dj"
print(a1)
print(a6)

#indexing in a string starts from 0 to n
# indexing is used to aacess the element 
#[start:stop:step]
var = "lemon"
print(var[3])
print('apples'[2])

# string slicing :
# string slicing is used to slice the string into various parts.
 
var_a = "vikasthakur"
print(var_a[:4] )
print(var_a[3:5] )
print(var_a[6:8] )
print('slicing')

print(var_a[::])
print(var_a[-11::1])
print(var_a[:])

my_list = [1, 2, 3, 4, 5]
print(my_list[::2])

my_list = [1, 2, 3, 4, 5]
print(my_list[::-2])

my_list = [1, 2, 3, 4, 5]
print(my_list[1:4:2])

#concatenation 
# adding two string with + sign is known as concatenation .

concat = "hello" +" "+'world'
print(concat)
print(concat[1:3])
print(concat[1:5])





