'''Write a Python program to compute following computation on matrix:
a) Addition of two matrices b) Subtraction of two matrices
c) Multiplication of two matrices d) Transpose of a matrix'''
m=int(input("Enter the number of rows:"))
n=int(input("Enter the nmber of columns:"))

A=[]
for i in range(m):
    sublist=[]
    for j in range(n):
        sublist.append(int(input(f"Enter the element of {i} row and {j} column:")))
    A.append(sublist)
print(A)

B=[]        
for i in range(m):
    sublist=[]
    for j in range(n):
        sublist.append(int(input(f"Enter the element of {i} row and {j} column:")))
    B.append(sublist)

print(B)

Add=[]

for i in range(m):
    sublist=[]
    for j in range(n):
        b=A[i][j]+B[i][j]
        sublist.append(b)
    Add.append(sublist)
print("Addition of two matrix is :",Add)
        
Sub=[]

for i in range(m):
    sublist=[]
    for j in range(n):
        a=A[i][j]-B[i][j]
        sublist.append(a)
    Sub.append(sublist)
print("substraction of two matrix is:",Sub)

Mul=[]
for i in range(m):
    sublist=[]
    for j in range(n):
       c=0
       for k in range(m):
           c=c+A[i][k]*B[k][j]
       sublist.append(c)
    Mul.append(sublist)
print("multiplication of two matrix is:",Mul)    
        

R=[]
trans=[]
2
for i in range(m):
    sublist=[]
    for j in range(n):
        R=A
        J=R[j][i]
        sublist.append(J)
    trans.append(sublist)
print("transpose of matrix is:",trans)    
        
