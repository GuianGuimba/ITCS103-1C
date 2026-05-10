import os

current_dir = os.getcwd()
print("current dir:",current_dir)

file_path = os.path.join(current_dir,"example.txt")
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print("File content:\n",file.read())    
else:
    print("File does not exist")

#Checking the file with OS module