def vikas(name):
    print(f'my name is {name}')

vikas('funny')  

def into(named):
    print(named)
    return named


into(10)

#checking even number 

def even_check(num):
    return  num%2 ==0
    

tyyy = even_check(57)
print(tyyy)

#checking odd number 

def even_check(num_o):
    return  num_o%2 !=0
    

tyyy_1 = even_check(57)
print(tyyy_1)

#it will return true if there is any even number inside a list 
print("even_checks")
num_list =[1,2,3,4,5]
def even_checks(num_list):
    for number in num_list:
        if number%2 ==0:
            return True
        else:
            pass
        #return False
            
         
tayu = even_checks(num_list)
print(tayu)



# Python program to print
# even numbers in a list using recursion

print("test")

def f():
     x = 15
     print(x)
x = 12
print(x)
f()
print(x)

# print("check_even_odd.")
# def check_even_list_od(zoo):
#     e_n =[]
#     for num in zoo:
#         if num%2 ==0:
#             e_n.append(num)
#         else:
#             pass
#         return
    

# check_even_list_od(1)    


    
