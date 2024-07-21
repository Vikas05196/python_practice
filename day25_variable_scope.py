example = "hello world."  #global
def loc_var():
    example = "hello world."  #local
    return example

print(example)
print(loc_var())




#1.  local variable cannot be used by code in the global scope.

# def loc_ex():
#     breakfast = "waffle"
#     return breakfast

# loc_ex()
# print(breakfast)

#2. global variables can be accessed by code in a local scope.
print("#2")
def print_global():
    print(global_var)

global_var = "this a global variable."    
print(global_var)

print("#2 example2")

def print_global_23():
    local_var_2 = "this is long"
    print(local_var_2 + print_global_2)

print_global_2 = "this is a double string."
print_global_23()





#3. the local scope of one function can't  use variable from 
#another function local scope.
# print("#number3")
# def first():
#     loc =2 
#     return loc

# def second():
#     return loc

# first()
# second()

#4. you can use the same name for different variables as long as they 
# are in different scope.

print("#number 4")

def local_ex1():
    fruit = "papaya"
    print(fruit)

def local_ex2():
    fruit ="grapes"    
    print(fruit)

fruit = "apple."    

local_ex1()
local_ex2()
print(fruit)



# global statement 

print("#global statement.")

def local_ex3():
    global fruit
    fruit = "papaya"
    print(fruit)

# def local_ex4():
#     fruit ="grapes"    
#     print(fruit)

fruit = "apple."    

local_ex3()
#local_ex4()
print(fruit)




