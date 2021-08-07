# Hello, In the 22th challenge we create a Database Admin Program
print("Welcomt to the Database Admin Program")
# Create A dictionary to hold all username:password key-value
log_on_information ={
    'shubhasheesh':'9889988264ss',
    'akarshit':    'ak12345@!',
    'prateek':'pr@tb12@*!',
    'akash':'Ak@gmail123',
    'admin00':'admin1234',
}
# Get user input
username = input("Enter your username: ")

# Simulate log on ...
# Get user password
if username in log_on_information.keys():
    password = input("Enter your password: ")
    if password == log_on_information[username]:
        print("\nHello " + username + "! You are logged in!")
        if username == 'admin00':
            print("Here is the current user database:")
            for key, value in log_on_information.items():
                print("Username: " + key + "\t\tPassword: " + value)
        else:
            # Allow standard user to change the password
            password_change = input("Would you like to change your password (yes/no): ").lower().strip()
            if password_change == 'yes':
                new_password = input("What would you like your new password to be (min 8 chars): ")
                if len(new_password)>=8:
                    log_on_information[username] = new_password
                else:
                    print(new_password + " is not the minimum eight characters.")
                print("\n" + username + " your password is " + log_on_information[username] + ".")
            else:
                print("\nThank you, goodbye.")
    else:
        print("Password incorrect!")
else:
    print("UserName not in Database. Goodbye.")





