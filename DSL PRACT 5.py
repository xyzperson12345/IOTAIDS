'''Write a Python program to store the first year percentage of
students in an array. Write function for sorting array of floating point
numbers in ascending order using 
a) Selection Sort 
b)Bubble sort 
and display top five scores.'''
marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students : ")
for i in range(0, n):
    ele = float(input())
    marks.append(ele) 

print("The marks of",n,"students are : ")
print(marks)

#<--bubble sort---------------------------------------------------------------->

def Bubble_Sort(marks):
    n = len(marks)
    c = 0    
    for i in range(n - 1): 
        c = c + 1
        for j in range(0, n - i - 1):             
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                
    print("no of comparision is equal to :",c)
    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i]) 

Bubble_Sort(marks)



#<---selection sort------------------------------------------------------------>

def Selection_Sort(marks):
    for i in range(len(marks)):      
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] < marks[j]:
                min_idx = j        
        marks[i], marks[min_idx] = marks[min_idx], marks[i]
    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])  
Selection_Sort(marks)
        
#<------Top Five Marks---------------------------------------------------------->

def find_top_five_marks(marks):
    marks.sort(reverse=True)
    top_five_marks = marks[:5]
    return top_five_marks


top_five_marks = find_top_five_marks(marks)
print("The top five marks are:", top_five_marks)


        
        
