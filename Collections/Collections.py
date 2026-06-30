def findLetter(grade):
    if grade>=90:
        return "A"
    elif grade>=80:
        return "B"
    elif grade>=70:
        return "C"
    elif grade>=60:
        return "D"
    elif grade>=50:
        return "E"
    else:
        return "F"

name=input("Enter student name: ")
grade1=int(input("Enter a grade: "))
grade2=int(input("Enter a grade: "))
grade3=int(input("Enter a grade: "))
grade4=int(input("Enter a grade: "))
grade5=int(input("Enter a grade: "))
print()

gradeList=[grade1,grade2,grade3,grade4,grade5]
avg=sum(gradeList)/len(gradeList)
#output
print(name)
print("Average:",avg)
print("Letter Grade:",findLetter(avg))