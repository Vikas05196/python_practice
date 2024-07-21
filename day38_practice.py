def fact(n):
    f= 1
    for i in range(1,n+1):
        f = f * i

    return f 
    

n = 5
result = fact(n)

print(result) 


# recursion in python 

print("recursion.")

# def greet():
#     print('geet')
#     greet()# function calling itself. and it will print number of times.
# greet()   

# factorial using recursion.
print("factorial by using recursion.") 

def facto(b):
    if b==0:
        return 1
    return b*fact(b-1)

x = facto(3)
print(x)

