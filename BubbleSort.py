def bubbleSort(A):
    for i in range(0,len(A)):
        for j in range(len(A)-1,i, -1):
            if A[j] < A[j - 1]:
                aux = A[j]
                A[j] = A[j-1]
                A[j-1] = aux
            print A

elements = [5,2,4,6,1,3,8,7,9,11,10,3,6,98,34,44,43,32,12,25,26,13]
print elements
bubbleSort(elements)
print elements