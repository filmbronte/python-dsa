def MaxMin(A,n):   #Finding max and min without D&C
    min = A[0]
    max = A[0]	
    for i in range(n):
         if A[i] > max:
             max = A[i]
         if A[i] < min:
             min = A[i]
    return max, min
 
def DCMaxMin(A,n,i,j): #Finding max and min with D&C
    if i == j:
       fmax = A[i]
       fmin = A[i]
    elif i == j - 1:
         if A[i] > A[j]:
              fmin = A[j]
              fmax = A[i]
         else:
              fmin = A[i]
              fmax = A[j]
    else:
          mid =(i+j)//2
          [gmax,gmin] = DCMaxMin(A,n,i,mid)
          [hmax,hmin] = DCMaxMin(A,n,mid+1,j)
          fmax = max(gmax,hmax)
          fmin = min(gmin,hmin)
    return  fmax,fmin 		  





A = [8, 3, 4,6,100, 4, 2,30,65,20]
print(A)
n=len(A)  
[fmax,fmin] = DCMaxMin(A,n,0,n-1)
print('Max and min with Divide and Conquer:') 
print(fmax,fmin)

	   
 
 
[max,min] = MaxMin(A,n)
print('Max and min without Divide and Conquer:') 
print(max,min)
