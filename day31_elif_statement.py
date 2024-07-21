#elif statement
#elif statement is used to more than one condition

var_a = int(input("enter a number. "))

if var_a <0:
    print("less than zero.")
elif var_a <= 10:
    print("value islies b/w 1 and 10.")
elif 0<var_a<=100:
    print("value is lies between 0 and 100.")
else:
    print(' value is greater than 100.')    
