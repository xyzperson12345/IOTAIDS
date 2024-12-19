'''Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency'''
U=[]
P=[]
M=[]
u=int(input("Enter strengths of student:"))
for i in range (1,u+1):
    U.append(i)
print(U)
p=int(input("Enter number of student present for test:"))
for i in range(p):
    x=int(input("Enter roll no of student present for test:"))
    P.append(x)
print("Total present students are= ",P)
def marks(M,P):
    for i in P:
        m=int(input(f"Enter the marks scored by roll no.:({i}):"))
        M.append(m)
    return M
marks(M,P)
def avarage(M):
    sum=0
    for i in M:
        sum=sum+i
    print("avarage = ",sum/p)
avarage(M)
def maxi(M):
    maximum=M[0]
    for i in M:
        if i > maximum:
            maximum=i
    print("maximum=",maximum)
    return maximum
maxi(M)
def mini(M):
    minimum=M[0]
    for i in M:
        if i < minimum:
            minimum=i
    print("minimum =",minimum)
mini(M)
T=[]
def result2(U,P):
    for i in range(len(U)):
        flag=0
        for j in range(len(P)):
            if U[i]==P[j]:
                flag=1
                break
        if flag==0:
            T.append(U[i])
    print("students who were absent",T)
    return T
result2(U,P)

def freq(M):
    X=[]
    for i in range(p):
        X.append(1)
    for i in range(p):
        for j in range(i+1,p):
            if M[i]==M[j]:
                X[i]+=1
    print("maximum frequency is",maxi(X)) 
    return X
freq(M)    
