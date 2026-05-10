
import os

while True:
    Choices = input("=== DREAMS LIFE MANAGER ===\n\n"
                    
                    "1. Read inspiring messages\n"
                    "2. Add new inspiring message\n"
                    "3. Rewirte the entire file\n"
                    "4. Exit\n\n"
                    
                    "Enter your choice: ")

    if Choices == "1":
        os.system('cls')
        file = open("dreams.txt","r")
        print("=== Inspiring Mesages ===\n")
        print(file.read())

    elif Choices == "2":
        os.system('cls')
        file = open("dreams.txt","a")
        new_message = input("Enter your inspiring message: ")
        file.write(new_message + "\n\n")
        file.close()

    elif Choices == "3":
        os.system('cls')
        while True:
            warning = input("This will overwrite your entire inspiring messages.\n"
                            "Are you sure? (yes/no)").lower()
            if warning == "yes":
                file = open("dreams.txt","w")
                new_message = input("Enter your new inspiring message: ")
                file.write(new_message + "\n\n")
                file.close()
                break
            elif warning == "no":
                print("Operation cancelled. Returning to main menu.")
                break
            else:
                print("Invalid input. Returning to main menu.")

    elif Choices == "4":
        os.system('cls')
        print("Exiting the program. Goodbye!")
        break

    else:
        os.system('cls')
        print("Invalid choice. Please try again.")
        