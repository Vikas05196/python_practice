# del => is used to delete statement from list.

del_element =["man","gora","kala","pila"]

print(del_element)
del del_element[2] # it will delete the value from index 2 i.e., is kala
print(del_element)

# .remove()  => method is used to remove the element that
# is pased in the argument.
print("remove function")
list_remove =["man","gora","kala","pila"]

print(list_remove)
print(list_remove.remove("man"))
print(list_remove)

# removing more than one value. this will remove 
#the the value which comes first.

colours = ["red","blue","green","yellow","white","black","blue","voilet"]

print(colours.remove("blue"))

print(colours)

# del vs .remove()
# del remove the value based on index
# remove delete the element based on value that passed in the argument.


# .append() it is used to append the element at the last.
print("appending in a list")
list_append = ["apple","mango","banana","pineapple"]
print(list_append)

print(list_append.append("watermelon"))

print(list_append)

# .insert() is used to add any element on the list at any position.
print("insert")
list_insert =["name","place","happy","worry"]

list_insert.insert(0,"habibi")

print(list_insert)

# .sort() method is used to sort the element.

print("sort.")

list_a = [1,2,-3,4,-5,-33,66,0,9]
list_a.sort(reverse=True)  # reverse = True it will print the list in 
# asceding order
print(list_a)

#print(list_a,reversed=True)

str_list =["bob",'tailey','vici','karman']
str_list.sort
print(str_list)

#note:
# .sort() method is not used in the mixed data types.
#for example

mixed_datatype =["ram","kam",1,1.2,3333,11.3323]

#mixed_datatype.sort() # it will throw a error 

print(mixed_datatype) 


# .sort() method sort the element in asciibetical order that is capital letter 
# sorter fisrst and then small letter.

# for example

asciibetical = ["Aman","boman","Apple","Biriyani","kamine","Kamini"]

print(asciibetical.sort())

print(asciibetical)

print(asciibetical.sort(key=str.lower)) # key = str.lower it will print in alphabetical oredr

print(asciibetical)

# .index() it is used to find the index of the element we pased it.

index_number  = ["karan","nita","Aman","boman","Apple","Biriyani",
                 "kamine","Kamini"]

print(index_number.index("Aman"))

# if the item is does not in the list it will throw a error
#print(index_number.index("sanam")) # throw a error

# if we have have multiple value in a list the list will return the the first element.

list_multiple =[1,3,4,8,3,4,3,9,33,34,55,999]

print(list_multiple.index(3)) # it will return the index 1

# .pop() method is used to remove iteam from list

list_pop = ["Aman","boman","Apple","Biriyani","kamine","Kamini"]

list_pop.pop() # it will remove the last element from the list.
list_pop.pop(3) # it will remove the element from index 3
print(list_pop)

