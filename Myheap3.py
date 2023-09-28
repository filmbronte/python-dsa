def Insert(A, n):
    j = n  
    i = n// 2
    data = A[n]
    while  i > 0 and A[i] < data:
         A[j] = A[i]
         j = i
         i = i // 2
    A[j] = data
 	
def Heapify(A): 
    for i in range(1,len(A)-1):
      Insert(A,i)
 

def  MakeHeap(A, n):
    for i in range(n//2,0,-1):
      FixHeap(A,n,i)

 
def FixHeap(A, n, i):
    j = 2*i
    data = A[i]
    while j <= n:
        if j < n and A[j] < A[j+1]:
           j = j + 1
        if  data >= A[j]:
            break		
        else:
            A[j//2] = A[j]
            j = j*2
            A[j//2] = data
 
def HeapSort(A, n):
    MakeHeap(A,n)
    for i in range(n,1,-1):
       temp = A[i]
       A[i] = A[1]
       A[1] = temp
       FixHeap(A,i-1,1)
    


	
A = [0, 3, 4, 2, 9, 1, 2, 1, 5, 7] #The first number A[0] is not used

print(A)
n = len(A) - 1

HeapSort(A, n)
print(A)

MakeHeap(A,n)
print(A)

print(A)
Heapify(A)
print(A)

data = 8
A.append(data)
print(A)

n = len(A) - 1
Insert(A,n) 
print(A) 
