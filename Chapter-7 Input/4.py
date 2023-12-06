print("     ----------Registration Form----------     \n\n")

student_name = input("Enter a student name: ")
student_age = int(input("Enter a student age: "))  # Corrected input prompt
data = f"{student_name}\n {student_age}"  # Combine name and age into a string

file_path = r"C:\Users\godsu\Desktop\my_file.txt"  # Use a raw string (r) for the file path

with open(file_path, "w") as file:
    # Write the user input to the file
    file.write(data)
    print(f'Successfully saved in {file_path}')
