'''a) Write a Python program to store roll numbers of students in an
array who attended a training program in random order. Write a function
for searching whether a particular student attended a training program or
not, using Linear search and Sentinel search.
b) Write a Python program to store roll numbers of students in an array who
attended a training program in sorted order. Write function for searching whether
particular student attended training program or not, using Binary search and Fibonacci
search'''
R=[]
a=int(input("Enter Total number of students present:"))
for i in range(a):
    b=int(input("Enter roll number of present student:"))
    R.append(b)
print(R)
#------------------------------------------------------------------------------
def linsearch():
    flag1=0
    for i in range(a):
        if R[i]==key:
            flag1=1
        
    if flag1==1:
        print("Student is present")
    else:
        print("Student is not present")
                
#------------------------------------------------------------------------------
def sensearch():
    i=0 
    R.append(key)
    while R[i]!=key:
        i+=1
    if i<a:
        print("Student is present")
    else:
        print("Student is absent")
    
#------------------------------------------------------------------------------    
low=0
high=a-1  
def binsearch(low,high):
    R.sort()
    global flag
    flag=0
    if high>=low:
        mid=(low+high)//2
        if key==R[mid]:
            print("Student is present")
        elif key<R[mid]:
            binsearch(low,mid-1)
        else:
            binsearch(mid+1,high)
    else:
        print("Student is absent")
#------------------------------------------------------------------------------

def fibsearch():
    R.sort()  
    
    flag = 0
    f = 1
    f1 = 1
    f2 = 0
    
   
    while f < a:
        f2 = f1
        f1 = f
        f = f1 + f2
    
    i = 0
    off = -1
    
  
    while f > 1:
        i = min(off + f2, a - 1)
        
        if R[i] == key:
            flag = 1
            break  
        
        elif key > R[i]:
            f = f1
            f1 = f2
            f2 = f - f1
            off = i
        
        else:
            f = f2
            f1 = f1 - f2
            f2 = f - f1
    
    if f==1 and R[off+1]==key:
        flag=1
    if flag == 1:
        print("Student is present")
    else:
        print("Student is not present")

#------------------------------------------------------------------------------
while(1):
            
    print("1.Linear search \n2.Sentinal search\n3.Binary search\n4.Fibonacci search\n5.Exit")
    choice=int(input("Enter the searching algorithm you want to impliment:"))
    if choice==1:
        while(1):
            key=int(input("enter key(search no):"))
            linsearch()
            x=int(input("Do you want to continue Linear Search(1/0):"))
            if x!=1:
                break
    if choice==2:
        while(1):
            key=int(input("enter key:"))
            sensearch()
            x=int(input("Do you want to continue Sentinel Search(1/0):"))
            if x!=1:
                break
    
    if choice==3:
        while(1):
            key=int(input("enter key:"))
            binsearch(low,high)
            x=int(input("Do you want to continue Binary Search(1/0):"))
            if x!=1:
                break
    if choice==4:
        while(1):
            key=int(input("enter key:"))
            fibsearch()
            x=int(input("Do you want to continue Fibonacci Search(1/0):"))
            if x!=1:
                break
    if choice==5:
        break