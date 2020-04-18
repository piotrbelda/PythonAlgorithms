# first solution

def isMonotonic(array):
    if len(array) < 3:
        return True
    condition=True
    for i in range(0,len(array)-1):
        if array[i] != array[i+1]:
            condition=False
            index_to_start_from=i+1
            if array[i] < array[i+1]:
                pattern=True #increasing
            else:
                pattern=False #decreasing
            break
    if not condition:
        for a in range(index_to_start_from,len(array)-1):
            if array[a] == array[a+1]: continue
            if (array[a] < array[a+1]) != pattern:
                return False
    return True

arr=[-1,-5,-10,-1100,-1103,-1104,-9001]

print(f'{isMonotonic.__name__} solution output: {isMonotonic(arr)}')

# second, simpler solution
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            isNonDecreasing=False
        if array[i] > array[i-1]:
            isNonIncreasing=False
    return isNonDecreasing or isNonIncreasing

print(f'{isMonotonic.__name__} solution output: {isMonotonic(arr)}')