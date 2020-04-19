# Write a function that takes in an n x m two-dimensional array
# (that can be square-shaped when n==m) and returns a one-dimensional array of all the array's
# elements in spiral order; Spiral order starts at the top left corner of the two-dimensional array, goes
# to the right, and proceeds in a spiral pattern all the way until every element has been visited

mat=[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

# 1st, "pythonic" version
def spiralTraverse(matrix):
    arr_to_sort=[]
    for element in matrix:
        arr_to_sort.extend(element)
    arr_to_sort.sort()
    return arr_to_sort

print(spiralTraverse(mat))

# 2nd, with algorithmic approach
def spiralTraverse(matrix):
    sC,eC,sR,eR=0,len(matrix[0])-1,0,len(matrix)-1
    spiral_list=[]
    while len(matrix)*len(matrix[0]) != len(spiral_list):
        for x in range(sC,eC+1):
            spiral_list.append(matrix[sC][x])
        for y in range(sR+1,eR+1):
            spiral_list.append(matrix[y][eC])
        for z in range(eC-1,sC-1,-1):
            if sR==eR:break
            spiral_list.append(matrix[eR][z])
        for k in range(eR-1,sR,-1):
            if sC==eC:break
            spiral_list.append(matrix[k][sC])
        sC+=1
        eC-=1
        sR+=1
        eR-=1
    return spiral_list

