# Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"
mixed_case = "A Song Of Ice And Fire"
# Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.
a= mixed_case.isupper()
print(mixed_case.isupper())
print(a)
# Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.
print(mixed_case.islower())
# Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.
print(mixed_case.upper())
# Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.
print(mixed_case.lower())
# Use the .istitle() method to check if mixed_case is title case and print the result.
print(mixed_case.istitle())
# Create a variable called title_case and assign it the result of .title() being called on mixed_case.
title_case =mixed_case.title()
# print() title_case
print(title_case)
# Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.
print(mixed_case.startswith("A"))
# Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.
print(mixed_case.endswith("e"))
# Create a variable called words and assign it the result of split() being used on mixed_case.
word = mixed_case.split()

# print the variable "words"
print("word")
print(word)
#print(type(x))
# Use the .join() method to join together all of the items in the list assigned to words as a single string.  Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.

print("  ".join(["ram","shyam","kam","dham"]))


mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())  
print(mixed_case.islower())  
print(mixed_case.upper())  
print(mixed_case.lower())  
print(mixed_case.istitle())  
title_case = mixed_case.title()
print(title_case)  
print(mixed_case.startswith("A"))  
print(mixed_case.endswith("e"))  
words = mixed_case.split()
print(words)  
print("".join(words).isalpha())  
