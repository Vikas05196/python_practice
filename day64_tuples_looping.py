# tuples using for loop and while loop in python 

a= (1,23,"mango",'banana',"summer","litchi")
for example in a:
    print(example)
    pass
# by using while loop 
print("while loop in tuple.....")
fruits = (1,23,"mango",'banana',"summer","litchi")

count = 0
while count<len(fruits):
    print(fruits[count])
    count +=1
    pass

# printing while loop in the reverse order.   
     
print(" printing while loop in the reverse order.  ")  

ro = (1,23,"mango",'banana',"summer","litchi")

backward = len(ro) - 1

while backward >=0:
    print(ro[backward])
    backward-= 1
    pass

# tuple slicing with step.

example =(1,2,3,4,5,6,7,8,9,10,)

print(example[::2]) 
print(example[1::2]) 
print(example[7::-1]) 
print(example[8::-2]) 
#print(example[::2]) 



    



        