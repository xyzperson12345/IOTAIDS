'''Write a Python program to store the first year percentage of
students in an array. 
Write function for sorting array of floating point
numbers in ascending order using quick sort and display top five scores.'''
A = []
n = int(input("Enter the number of students:-"))
for i in range(n):
    A.append(float(input("enter the percentage of students")))
print("Before sorting")
print(A)
def partition(start,end):
 
    pivot = A[end]
    pindex = start
    for i in range(start,end):
        if A[i] < pivot:
            A[i] , A[pindex] = A[pindex] , A[i]
            
            pindex = pindex + 1
            
    A[pindex] , A[end] = A[end] , A[pindex]
  
    return pindex
        
 
def quicksort(start,end):
    
    if start < end :
        pindex = partition(start,end)
        quicksort(start, pindex - 1)
        quicksort(pindex + 1, end)
    
quicksort(0,n-1)
print("After sorting")
print(A)

def find_top_five_marks(A):
    A.sort(reverse=True)
    top_five_marks = A[:5]
    return top_five_marks


top_five_marks = find_top_five_marks(A)
print("The top five marks are:", top_five_marks)
