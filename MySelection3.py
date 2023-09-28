def Swap(A,i,j):   
    temp = A[j]
    A[j] = A[i]
    A[i] = temp
	
def Partition(A,first,last):  #Partition  A[first:Last]
    v = A[first]
    i = first
    j = last
    i = i+1
    j = j-1
    while i < j:
 #      i = i+1
       while A[i] < v:
          i = i+1
       while A[j] > v:
          j = j-1
       if i < j:
          Swap(A,i,j)
    A[first] = A[j]
    A[j] = v
    return j
	
def Selection(A,k):  #Find the kth smallest element in list A
     first = 0
     last = len(A)-1
     while  True:
        j = Partition(A,first,last)+1
        B = A[first:last +1]
        v = B[j-1]
        print(first,last,j)
        print("\nSublist")
        print(A[first:last+1])
        if k == j:
             break
        elif k < j:
             last = j - 1
        else:
             first = j + 1		
        return j,v	

	
A =[5,7,4,1,10,6]
print("Original list")
print(A)
Swap(A,0,2)
print("After swap between A[0] and A[2]")
print(A)

A =[5, 8,7,4,1,10,6, 9]
print("\nOriginal list")
print(A)
Partition(A,0,len(A)-1)
print("After partition")
print(A)

A =[5,7,4,1,10,6]
print("\nOriginal list")
 
print(A)
[j,v] =Selection(A,2)
print("the kth smallest   value")
print(v)
 
 
