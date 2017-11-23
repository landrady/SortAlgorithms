def printArray(start, end, v):
    newV = [0] * (end-start)
    for x in range(0,end-start):
        newV[x] = v[start+x]
    return newV

def buscaBinaria (x, n, v):
    e = 0
    d = n - 1
    while e <= d:
        print printArray(e,d,v)
        m = (e + d) / 2
        if(v[m] == x):
            return m
        if(v[m] < x):
            e = m + 1
        else:
            d = m - 1
    return -1

vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
print buscaBinaria(7,50,vetor)