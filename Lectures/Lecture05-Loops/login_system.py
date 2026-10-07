correct_email = "sufyan@gmail.com"
correct_pass = "sufyan123"

max_attempts = 3
attempts = 0 

while attempts < max_attempts: 
    entered_email = input("Apni email likho bhai: ")
    entered_pass = input("Password do?? ")

    if entered_email == correct_email and entered_pass == correct_pass:
        print("Loggedin successfully! Welcome back!")
        break 
    else: 
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Invalid email and password! Remaining Attempts: {remaining}")
        continue



