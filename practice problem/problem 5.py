#5.	Write a program that prompts the user to enter the number of students. Then for each student program asks to enter the score, and then displays the highest and second highest scores.
no_of_students=int(input("enter the number of students"))
all_marks=[]
count=1
for i in range(no_of_students):
    print("student",count,"enter your marks")
    marks=int(input(""))
    count+=1
    all_marks.append(marks)
all_marks=sorted(all_marks,reverse=True)
print("highest marks are ",all_marks[0])
print("second highest marks are",all_marks[1])

