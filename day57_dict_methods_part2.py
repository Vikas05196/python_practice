# .fromkeys()
# .pop()
# .popitem()


# .formkeys() return a key value pair it  passed in the argument. the first argument is keys and the second argument is values.
# when we pass string argument in keys it return a key character a key 
# when the string has duplicate caharcter it will print only one character ex: addr it will take the letter adr only 
# if we  do not pass the second argument it will return the None.
var_1 = {}.fromkeys(["key"],"value of the key is. ")

print(var_1)

var_2 ={}.fromkeys("key","value of the key is. ")
print(var_2)

var_2 ={}.fromkeys("keeen","value of the key is. ")
print(var_2)

var_one = {}.fromkeys(["key"]) #argument passed as list so it returning word key 
print(var_one)

var_on = {}.fromkeys("key") # argument passes as string so it rurtned the every character in the key K e y 
print(var_on)


# .pop()
# .pop() method is used to remove the key value pair from the dictionary.
print('.pop()')
var_pop = {"name ":"vikas","village":"kaka",1:333}
var_pop.pop("village")

print(var_pop)

var_pop_2 = {"name ":"vikas","village":"kaka",1:333}
b = var_pop_2.pop(1) # assigned pop to a variable 

print(var_pop_2)

print(b)

# key does not exists in a dictionary 

var_pop_3 = {"name ":"vikas","village":"kaka",1:333}

#var_pop_3.pop("type") # popping the elemnt that does not exist in a dictionary  
print(var_pop_3)

# .popitem() remove the last iteam in a dictionary 

var_popitem = {"peru ":"vikas","ooru":"kaka",1:333}

var_popitem.popitem()
#var_popitem.popitem("peru") # when we try to pass an argument it returns a error.
print(var_popitem)









