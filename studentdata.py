import os

# Step 1: Create a directory to store student data
data_folder = "student_data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Step 2: Prompt the user to enter student data
while True:
    # Get student data from the user
    student_name = input("Enter student name (or type 'exit' to quit): ").strip()
    if student_name.lower() == 'exit':
        break
    student_id = input("Enter student ID: ").strip()
    student_grade = input("Enter student grade: ").strip()
    student_phone = input("Enter student phone no: ").strip()

    # Step 3: Create a text file to store student data
    file_name = f"{student_id}_{student_name}.txt"
    file_path = os.path.join(data_folder, file_name)

    with open(file_path, "w") as file:
        file.write(f"Student Name: {student_name}\n")
        file.write(f"Student ID: {student_id}\n")
        file.write(f"Student Grade: {student_grade}\n")
        file.write(f"Student Phone: {student_phone}\n")

    print(f"Student data saved to {file_path}\n")

print("Program terminated.")
