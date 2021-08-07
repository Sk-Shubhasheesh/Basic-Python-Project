# Hello, In the 10th challenge we create a Favorite Teachers  Program
print("Welcome to The Favorite Teachers  Program")
fav_teachers = []

# Get user input
fav_teachers.append(input("\nWho is your first favorite teacher: ").title())
fav_teachers.append(input("Who is your second favorite teacher: ").title())
fav_teachers.append(input("Who is your third favorite teacher: ").title())
fav_teachers.append(input("Who is your fourth favorite teacher: ").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " +str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " +str(sorted(fav_teachers, reverse=True)))
print("Your top two favorite teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last two favorite teachers are: " + fav_teachers[-1] +  ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Insert a new favorite teacher
fav_teachers.insert(0, input("\nOpps," + fav_teachers[0] + " is no longer your first favorite teacher. Who is your new Favorite teacher: ").title())
# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " +str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " +str(sorted(fav_teachers, reverse=True)))
print("Your top two favorite teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last two favorite teachers are: " + fav_teachers[-1] +  ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")


# Remove a Specific teacher
fav_teachers.remove(input("\nYou've decided you no longer teacher. Which teacher would like to remove from your list:").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " +str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " +str(sorted(fav_teachers, reverse=True)))
print("Your top two favorite teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last two favorite teachers are: " + fav_teachers[-1] +  ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")


