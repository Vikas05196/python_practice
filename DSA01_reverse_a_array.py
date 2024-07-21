
'''
print("hello world",end=" @")
print("welcome")

a=[1,2,3,4,5]
print(a[::-1])

#output
[5, 4, 3, 2, 1]

'''

# 1. Array Reverse Using an Extra Array (Non In-place):
def array_reverse_using_extra_arr(arr):
    reversed_arr = arr[::-1]
    print("the reversed arrry is ",reversed_arr)
    for i in reversed_arr:
        print(i,end=" ")


arr=[1,2,3,4,5]
array_reverse_using_extra_arr(arr)


# 2. Array Reverse Using a Loop (In-place):

def reverse_list(A,start,end):
    while start < end:
        A[start],A[end]=A[end],A[start]
        start = start+1
        end = end-1

A = [1,2,3,4,5,6,7]
#print(A)
print("revrese array is using a reverse loop  ")
reverse_list(A,0,6)
print(A)


# Array Reverse Inbuilt Methods (In-place)

x = [1,2,3,4,5,6,8]

new_arry = list(reversed(x))
print('inbuilt method')
print(new_arry)


#Array Reverse Recursion (In-place or Non In-place)

def reverse_recursion(a,staart,endd):
    if staart >= endd:
        return
    a[staart],a[endd]=a[endd],a[staart]
    reverse_recursion(a,staart+1,endd-1)

a=[10,9,8,7,6,5]
print(a)
reverse_recursion(a,0,5)
print("reversed recursion") 
print(a)   

# Array Reverse Stack (Non In-place)

def array_using_reverse_stack(array):
    stack = []
    for element in array:
        stack.append(element)
    for i in range(len(array)):
        array[i]=stack.pop()
            
    

array = [9,8,7,6,5,4]
array_using_reverse_stack(array)
print("reverse arry using stack is:",array)