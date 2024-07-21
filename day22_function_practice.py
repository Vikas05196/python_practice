# Create a function called hello_world_printer() 
# which takes no parameters and prints the string "hello world"

# Call the function hello_world_printer()

def hello_world_printer():
    print("hello world.")

hello_world_printer()    


# Create a function called name_printer which takes 1 parameter and prints it

# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.

# Call name_printer() with the variable "name" as its argument.

print("function with one argument ")
name = input("enter your name.")

def name_printer(name):
    print(name + "  Thanks you for name.")


name_printer(name)  

#

def name_printer(user_name):
    print(user_name)
 
 
name = input("Please enter your name.")
name_printer(name)

print("#########")

def name_printer(kaka):
    print(kaka)
 
 
vikas = input("Please enter your name.")
name_printer(vikas)

#rectangular prism 

#qPrint("rectangular prism volume")


l = int(input("length"))
w = int(input("width"))
h = int(input("height"))

def recatngular_prism(l,w,h):
    return l*w*h

volume = recatngular_prism(l,w,h)
print(recatngular_prism(l,w,h))
#print("The volume of the rectangular prism is [call function  here to calculate volume] cubic feet.",l*w*h)
print(volume)




print("celsius and farehheit")
c=int(input("celsius"))
def f_c(c): 
    return  1.8*c

f = f_c(c)
print(f)
print("The Fahrenheit equivalent of " + str(c) + " degrees Celsius is " + str(f_c(c)) + ".")