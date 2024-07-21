#one_a = range (1,50)

# for i in range(1,51):
#     if i%3 == 0 and i%5 ==0:
#         print("Fizbuzz")
#     elif  i%3 ==0:
#         print("fizz")
#     elif i%5 ==0:
#         print("buzz.") 
#     else:
#         print(i)   


# print("###############")

# for num in range(1, 51):
#     # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     # If num is only divisible by 3, "Fizz" will be printed.
#     elif num % 3 == 0:
#         print("Fizz")
#     # If num is only divisible by 5, "Buzz" will be printed.
#     elif num % 5 == 0:
#         print("Buzz")
#     # num itself will be printed in all other cases.
#     else:
#         print(num)


# The argument fac_num's name is short for factorial number.
def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item
 
    # returns returned, which now holds the value of fac_num's factorial
    return returned
 
 
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120

print("factorial.")
def factorialofnumber(fav):
    factorial_p = 1

    for i in range(fav,1,-1):
        factorial_p *=i

    return factorial_p
    

print(factorialofnumber(8))   


# num = 9
# def facti(typo):
#     fact = 1
# for q in range (1,num+1):
#     fact = fact*q

# return fact

print("factorial.")

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


