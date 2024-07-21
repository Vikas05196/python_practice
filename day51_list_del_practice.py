# Create a variable called arctic_animals and assign it the 
#list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arcritic_anmials = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# Use del to remove "tiger" from the list assigned to arctic_animals.
del arcritic_anmials[4]
print(arcritic_anmials)
# Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
print(arcritic_anmials.remove("elephant"))
print(arcritic_anmials)
# Use the .append() method to add the string "arctic fox" to the list arctic_animals.
print(arcritic_anmials.append("artic animal"))
print(arcritic_anmials)
# Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
print(arcritic_anmials.insert(2,"snowy owl"))
print(arcritic_anmials)
# Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
sort_a = arcritic_anmials.sort()
# Use print() to display the list assigned to arctic_animals
print(sort_a)
print(arcritic_anmials)
# Use .index() to get the index number of "reindeer" from arctic_animals then print it.
print(arcritic_anmials.index("reindeer"))
# Use .pop() to get the last item from the list arctic_animals then print it.

print(arcritic_anmials.pop())

print(arcritic_anmials)


# answers 
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")  
arctic_animals.sort()  
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())