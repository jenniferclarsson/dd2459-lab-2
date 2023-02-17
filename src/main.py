def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    return A

def insertion_sort(A) :
    for i in range(1, len(A)):
        j = i
        while(j > 0 and A[j-1] > A[j]):
            A = swap(A, j, j-1) # Error 4: j-1 TO j
            j -= 1
        i += 1
    return A

def binary_search(A, key):
    l = 0
    r = len(A)-1
    while True:
        x = round((l+r)/2)
        if key < A[x]: # Error 5: key < A[x] TO key >= A[x]
            r = x - 1 
        else:
            l = x + 1
        if key == A[x] or l > r: # Error 2: l > r TO l <= r
            break
    if key == A[x]: # Error 3: key == A[x] TO key != A[x]
        return x
    else:
        return -1 # Error 6: return -1 TO return 1
    
def member(A, key):
    sorted = insertion_sort(A)
    index = binary_search(sorted, key)
    return (index > -1) # Error 1: index > -1 TO index <= -1
