#mini = float('inf')
#print(mini)

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9

# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#               Maximum element is: 35

# a= [1,2,3,4,5]

# b = max(a)
# print(b)
##########################################################################
# Python program to find Maximum and minimum of an array 
# using minimum number of comparisons

def set_mini(A):
    mini = float("inf")
    for num in A:
        if num < mini:
            mini = num
    return mini 

def set_max(A):
    maxi = float("-inf")
    for num in A:
        if num > maxi :
            maxi  = num
    return maxi

A =[1,2,3,4,5]
N = len(A)

print("max is :",set_max(A))
print("min is :", set_mini(A))   

####################################################

# max and min of array using sorting
print("max and min by using sorting the element ")
def getminmax(arr):
    arr.sort()
    minmax = {"mini" : arr[0],"maxi" : arr[-1]}
    return minmax

arr = [10,203,666,99]
minmax = getminmax(arr)

print("minimum is :",minmax['mini'])
print("maximum is ",minmax["maxi"])

############################################################

# Maximum and minimum of an array using Linear search:

print("Maximum and minimum of an array using Linear search:")

class Pair:
    def __init__(self): 
        self.min = 0
        self.max = 0

def getMinMax(arr:list,n:int) -> Pair:
    MinMax = Pair()

        # If there is only one element then return it as min and max both
    if n==1:
        MinMax.min = arrr[0]
        MinMax.max = arrr[0]
        return MinMax
    # If there are more than one elements, then initialize min

    if arrr[0]>arrr[1]:
        MinMax.max = arrr[0]
        MinMax.min = arrr[1]
    else:
        MinMax.max = arr[1]
        MinMax.min = arr[0]  

    for i in range(2,n):
        if arrr[i]<MinMax.min:
            MinMax.min = arrr[i]
        else:
            arrr[i]>MinMax.max
            MinMax.max = arrr[i]
    return MinMax
#if __name__ == "__main__":

#arrr =[1,2,3,4,5,6] 
arrr = [1,2,3,4,5,6]
arr_size = 6
MinMax = getMinMax(arrr,arr_size)
print("max element is :",MinMax.min)
print("min element is :",MinMax.max)



#########################################################
'''
# Python program of above implementation

# structure is used to return two values from minMax()

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

# Driver Code
if __name__ == "__main__":
    arr = [1000, 1000001, 445, 10786, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

# This code is contributed by
# sanjeev2552
'''




