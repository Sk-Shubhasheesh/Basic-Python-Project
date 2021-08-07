# Hello, In the 15th challenge we create a Average Calculator App Program
print("Welcome to the Grade Point Average Calculator App")

# Get user name
name = input("What is your name: ").title().strip()
grade_num = int(input("How many grades would you like to enter: "))

# Get the user's grade
grades = []
for i in range(grade_num):
    grades.append(int(input("Enter grade: ")))

# Sort the grades and print them to the screen
grades.sort(reverse=True)
print("\nGrades Highest to Lowest: ")
for grade in grades:
    print("\t" + str(grade))

# calculate the average
average = sum(grades)/len(grades)
average = round(average, 2)

# Print A grade summary
print("\n" + name + "'s Grade Summary: ")
print("\tTotal Number of Grade: " + str(len(grades)))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average))

# Get the user Desired average calculate and what they need to get on the next assignment
desired_avg = float(input("\nWhat is your desired average: "))
grade_req = desired_avg*(len(grades)+1)-sum(grades)
grade_req = round(grade_req, 2)

# Print a summary
print("\nGood luck " + name + "!")
print("You will need to get a " + str(grade_req) + " On your next assignment to earn a " + str(desired_avg) + "average.")

#  Make a copy of the original grades and swap out one of the grades
new_grades = grades[:]
print("\nLets see what you average have been if you did better/worse on an assignment.")
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade = int(input("What grad would like " + str(grade_change) + " to: "))
new_grades.append(new_grade)

# Sort the new grades and print them to the screen
new_grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest: ")
for grade in new_grades:
    print("\t" + str(grade))

# calculate the average
new_average = sum(new_grades)/len(new_grades)
new_average = round(new_average, 2)

# Print A grade summary
print("\n" + name + "'s New Grade Summary: ")
print("\tTotal Number of Grade: " + str(len(new_grades)))
print("\tHighest Grade: " + str(max(new_grades)))
print("\tLowest Grade: " + str(min(new_grades)))
print("\tAverage: " + str(new_average))

# print a summary on how the average change
print("\nYour new average would be a " + str(new_average) + " compared to your real average of " + str(average) + "!")
average_change  = new_average - average
average_change = round(average_change, 2)
print("That is change of " + str(average_change) + " points!")

# Too bad the original grades are still intact!
print("\nToo bad your orginal grades are still the same!")
print(grades)
print("You should go for extra credit!")




