# Create a variable and assign it a list that contains an integer, a float,
# a Boolean value, a string, and a list of 3 integers.
list_a = [1,3.4,True,False,"habibi",[3,4,6]]
print(list_a)

# Create another variable and assign it a call of the list() function with a
# string as its argument.
list_b = "shop"
print(list(list_b))
# Use the keyword "in" to check if the letter "e" is in the list
# assigned to the variable from step 2 and print the result.
list_b_in = 'h' in list_b
print(list_b_in)

# Use the keyword "not in" to check if the letter "a" is not in the list 
# assigned to the variable from step 2 and print the result.

list_b_not_in = 'h' not in list_b
print(list_b_not_in)
