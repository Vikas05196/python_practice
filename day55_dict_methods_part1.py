# .keys()
# .values()
# .item()
# .get()

# .keys() method
# key method is used to fetch all the key from the dictionary

example_dict ={"apple":"fruit","ball":"game",123:324,1.22:333}

print(example_dict.keys())

# printing keys by using for loop

for key in example_dict.keys():
    print(key)
    pass

# .values()
# values method is used to fetch the values from the variable.

value_dict ={"apple":"fruit","ball":"game",123:324,1.22:333}
print(value_dict.values())

# printing values by using for loop

for value in value_dict.values():
    print(value)
    pass

# .items()
# items is used to fetch all the keys and  values from dictionary at the same time
# it will return the list of tuples 
items_dict ={"apple":"fruit","ball":"game",123:324,1.22:333}
print(items_dict.items())

# printng items by using for loop

for key,value in items_dict.items():
    print(key, value)
    pass

# checking type of a dictinory 
print(type(items_dict.keys()))
print(type(items_dict.values()))
print(type(items_dict.items()))

# use list function to convert dict into list
print(list(items_dict.keys()))
print(list(items_dict.values()))
print(list(items_dict.items()))

# using in and not in dictionary to find values

items_dict_in_not_in ={"apple":"fruit","ball":"game",123:324,1.22:333}

print("game" in items_dict_in_not_in.values())

# .get() method is used to fetch the key in the dict if not found return the error message we have passed.
print(".get method")
items_get ={"apple":"fruit","ball":"game",123:324,1.22:333}

print(items_dict.get("apple","key is not found in the dictionary items_get.")) # fruit

print(items_dict.get(1,"key is not found in the dictionary items_get.")) # it reurn the message.

# other thing we know about dictionary.
# dictonaries are immutable data types. as that of list 

mutable_dict ={"apple":"fruit","ball":"game",123:324,1.22:333}
print(mutable_dict)
people = mutable_dict
people["apple"] = "sabe"
print(mutable_dict)
print(people)

# dict in multiple lines
mutiple_dict ={"apple":"kashmir",
               "ball":"game",
               123:324,
               1.22:333}

print(mutiple_dict)

# len function return  the key value pair.

print(len(mutable_dict) ) # it return the 4 key value pair.



















    
