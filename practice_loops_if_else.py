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

