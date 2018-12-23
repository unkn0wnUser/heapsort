def left(A, index):
    lNF_index = 2 * index + 1
    return lNF_index

def right(A, index):
    rNF_index = 2 * index + 2
    return rNF_index

# MAX HEAP
# This function assumes that 
# the left tree (root = left child of root) 
# and the right tree (root = right child of root)
# are already Max heaps
# It lets the (newly added) value @ the root sink into the tree
# while maintaining the max heap property
def heapify(A, index, heap_len):
    lNF_index = left(A, index)
    rNF_index = right(A, index)
    if(lNF_index < heap_len and A[lNF_index] > A[index]):
        maximum = lNF_index
    else:
        maximum = index
    if(rNF_index < heap_len and A[rNF_index] > A[maximum]):
        maximum = rNF_index
    if(maximum != index):
        A[index], A[maximum] = A[maximum], A[index]
        heapify(A, maximum, heap_len)

def build_heap(A):
    for index in range((len(A)-1)//2, -1, -1):
        heapify(A, index, len(A))

def heapsort(A):
    build_heap(A)
    print("Heap:\n{}".format(A))
    heap_len = len(A)
    for index in range(len(A)-1, -1, -1):
        # swap A[0] (root) with A[index]
        A[0], A[index] = A[index], A[0]
        heap_len -= 1
        heapify(A, 0, heap_len)

global A
A = [5, 9, 1, 4, 6, 7, 3, 2, 8]
heapsort(A)
print("Sorted:\n{}".format(A))