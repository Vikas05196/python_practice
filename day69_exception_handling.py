# exception handling is used when program throws a error to catch the 
# error we use exception handling.
# when program throw a error the code stops there 
# for handling of error we use exception handling by using.
# try 
# except 

print("example-1")
a=2
b=0
try:
    print(a/b)
except Exception as e:
    print(e)

print("example-2")   

#c = int(input("enter a number."))
#try:
#    print("cramp" ==c)
#except ValueError:
#    #print(e)
#
#    print("finished.")



try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound    


#var = int(input("enter a number: "))
#print(var)
print("example-3")
try:
    var=int(input("enter a number."))
    print(var)
except ValueError:
    print("enter the correct value.")    
except Exception as e:
    print(e)
finally:
    print("wooh")

print("completed.,")    