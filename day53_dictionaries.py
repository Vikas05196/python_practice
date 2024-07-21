# dictinoary :
# dictionary is a data type which can store the value is like a list 
# it's store the value is like a key and value pairs
# in list data is assigned to index in dictinary data is assigned to key.
# keys can be integers,strings,float and booleans etc.,
# dictinaries cannot contain duplicate values.

dict_example ={"school":"boys","country":"capital"} #{"key":"value"}

print(dict_example)

# accesing dictinary by keys
print(dict_example['school'])

# values in the dict can also be assigned to variable
var_a = dict_example["country"]
print(var_a)
# dict can be also used in the concatenation of the element.
print("the "+  dict_example["country"] + " is under threat.")
    

# different types of keys string,integer,booleans etc.

string_example = dict_example ={"school":"boys","country":"capital"}
int_example = {1: 2,5:55,8:88}
float_example ={1:1.6,2:5.77,1.98:12.768}
mixed_example ={"name ":"vikas",True:"kotan",1.68:1.77,1.22:333}

print(string_example)
print(int_example)
print(float_example)
print(mixed_example)

# dictinaries are unordered when the  value assigned to key and value are equal.

print([1,2,3]==[1,2,3]) # order 
print([1,2,3]==[3,1,2]) # undorder

print("dict order")
mixed_example ={1:"vikas",2:"kotan",3:1.77}
float_example ={2:"kotan",1:"vikas",3:1.77}

print(mixed_example == float_example) # in both dictionary example key and value are equal.

# key error => if we call a key if the key does not exist in the dictionary.

not_in_dict_example ={1:"vikas",2:"kotan",3:1.77}
#print(not_in_dict_example[6]) # it wil throw a error keyerror

print("in and not in python.")
# in and not in dict used to find key

# in => if the key  found it  returns True. if not fund return false
# not in => if key found return false. if not found reurn true
not_in_dict_example ={1:"vikas",2:"kotan",3:1.77,1:88,2:222}

print(1 in not_in_dict_example) # 1 key found in not_in_dict_example so it return true.
print(55 in not_in_dict_example) # 55 key not in not_in_dict_example so it return false
print(8 not  in not_in_dict_example) # 8 key not in not_in_dict_example so it return true.
print(1 not in  not_in_dict_example) ## 1 key is in not_in_dict_example so it return false









