# function 
#  function is used to run a code when it called. 
# Functions is a block of statements that return the specific task. 
# The idea is to put some commonly or repeatedly done tasks together 
#and make a function 
#so that instead of writing the same code again and again for different inputs,
# we can do the 
# function calls to reuse code contained in it over and over again.

#defining/creating  a function 

def function_name():
    print("hello world")


#calling a function 

function_name()   

#function parameter

def Function_parameter(para):
    print(para + 2)


Function_parameter(2)    


#multiple parameter 

def Function_multiparameter(p1,p2,p3):
    print(p1+p1+p3)
    print(p1+p2-p3)


Function_multiparameter(100,100,2763)    
Function_multiparameter(1,2,3)

#default parameters 
print("default parameter")
def function_deafault(var=10,var_2 = 20):
    print(var+var_2)

function_deafault()
function_deafault(10,7770)    



# returning from a function
# return is used to store a value.
 
print("return function")
def return_function(t1,t2):
    return t1*t2

result = return_function(11,10)

print(result)




