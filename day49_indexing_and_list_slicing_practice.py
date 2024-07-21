# Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
list_example = [[0, 2], [4, 6], [8, 10], [12, 14]]

# Access the first list from the list of lists in step 1 by index then print it.
print(list_example[1])
# Access the 14 from the list in step 1 then print it.

print(list_example[3][1])
# Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
var_2 = ["chair", "table", "desk", "lamp", "bed"]
# Use a negative integer to access "chair" from the variable in step 4 by index then print it.
print(var_2[-5])
# Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and 
# the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.
print("Most people own at least 2 chairs."+str(list_example[0][1])+ var_2[-5] +" Most people own at least,. ")
# Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
create_variable = [0.98, 8.76, 6.54, 4.32]
# Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
print(create_variable[1:])
# Print the slice [8.76, 6.54] from the variable you created in step 7.
print(create_variable[1:3])

# Print the slice [0.98, 8.76] from the variable you created in step 7.
print(create_variable[:2])


# coding solutions

up_by_two = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + " " + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])

