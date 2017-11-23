# 0 1 2 3 4 5 6 7
def merge(A,inicio,meio,fim):
    n1 = meio - inicio + 1
    n2 = fim - meio
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0,n1):
        L[i] = A[inicio + i]
    for j in range(0,n2):
        R[j] = A[meio+j+1]
    print A
    print 'comparar '
    print L
    print 'com'
    print R
    i = 0
    j = 0
    k= inicio
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j +1
        k = k + 1

    while i < len(L):
        A[k] = L[i];
        k = k + 1
        i = i + 1

    while i < len(R):
        A[k] = R[i];
        k = k + 1
        i = i + 1


def mergeSort(A,inicio,fim):
    if inicio < fim:
        #DIVISAO
        meio = (inicio+fim)/2

        #CONQUISTA
        mergeSort(A,inicio,meio)
        mergeSort(A,meio+1,fim)

        #COMBINACAO
        merge(A,inicio,meio,fim)

elements = [5,2,4,6,1,3,8,7,9,11,10,3,6,98,34,44,43,32,12,25,26,13]
fim = len(elements)

mergeSort(elements,0,fim-1)
print elements