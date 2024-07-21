# len() function is used to fetch the lenght of a iteable data type such as 
#string 
#len()
print(len("string"))
print("this"+ " is called "+ "string")
print(len("this"+ " is called "+ "string."))
print("amanwithbank"[3:7])
print(len("amanwithbank"[3:7]))


######practice string ################

# num = input("enter a number")

# for n in num:
#     print(n)

user_string = input("Please enter a string.")
reversed = ""
 
for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]
 
print(reversed)




