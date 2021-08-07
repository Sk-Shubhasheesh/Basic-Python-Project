# Hello, In the 6th challenge we create a Grader Sorter App

print("Welcome to the Grader Sorter App")

name = input("\nWhat is Your name : ").title().strip()
print("Hello, ",name ,"!!")


# Initialize list and get user input:
grades = []
grade = int(input("\nWhat is your First Grade (0-100): "))
grades.append(grade)
grade = int(input("What is your Second Grade (0-100): "))
grades.append(grade)
grade = int(input("What is your Third Grade (0-100): "))
grades.append(grade)
grade = int(input("What is your Fourth Grade (0-100): "))
grades.append(grade)
print("\nYour Grades are : ", str(grades))
# sort the list from highest to lowest
grades.sort(reverse=True)
print("\nYour Grades from highest to lowest are :" ,str(grades))

# Removing the lowest two grades:
print("\nThe lowest two Grades will now be dropped.")
removed_grade=grades.pop()
print("Removed Grades :" +str(removed_grade))
removed_grade=grades.pop()
print("Removed Grades :" +str(removed_grade))

# Recap remaining Grades:
print("\nYour Remaining Grades are : " +str(grades))
print("Nice work ",name ,"!" ,"Your highest Grade is :" + str(grades[0]) +  ".")



