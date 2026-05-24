from turtledemo.nim import computerzug

student ={}

#load existing data from file
try:
    with open("students.txt","r") as file:
        for line in file:
            (
                name,
                math,
                english,
                science,
                social_science,
                computer,
                assamese
            ) = line.strip().split(",")

            student[name] ={

                "Math": int(math),
                "English": int(english),
                "Science": int(science),
                "Social Science": int(social_science),
                "Computer": int(computer),
                "Assamese": int(assamese)
            }


except FileNotFoundError:
    print("No previous student records found!")


while True:
    print("\n-------------STUDENT MANAGER APPLICATION-----------")
    print("1. ADD Student ")
    print("2. View Students ")
    print("3. Check Result ")
    print("4.Delete Student ")
    print("5.Update Student Marks ")
    print("6.Search Student ")
    print("7. Rank  ")
    print("8. Topper ")
    print("9. Exit !")

    choice =input(" Enter Your Choice : ")
    #If user enters 1 . - to add the student details
    if choice == "1":

        name = input("Enter the name of the student: ")

        try:
            math = int(input("Enter Math marks : "))
            english = int(input("Enter English marks : "))
            science = int(input("Enter Science marks : "))
            social = int(input("Enter Social marks : "))
            assamese = int(input("Enter Assamese marks : "))
            computer = int(input("Enter Computer marks : "))

            student[name] = {
                "Math":math,
                "English":english,
                "Science":science,
                "Social Science":social,
                "Computer":computer,
                "Assamese":assamese
            }
            #Save into file
            with open("students.txt","w") as file:
                for student_name,subjects in student.items():
                    file.write(
                        f"{student_name},"
                        f"{subjects['Math']},"
                        f"{subjects['English']},"
                        f"{subjects['Science']},"
                        f"{subjects['Social Science']},"
                        f"{subjects['Computer']},"
                        f"{subjects['Assamese']}\n"
                    )
            print(f"{name} successfully added!")

        except ValueError:
            print("Invalid marks input!")




    # 2.View Student
    elif choice =="2":
        if not student:
            print("No student found!")

        else:
            print("\n========Student Records:==========")
            for name,subjects in student.items():
                total = sum(subjects.values())

                percentage = total / len(subjects)
                print(f"""
                        Name :{name}
                        Math :{subjects['Math']}
                        English :{subjects['English']}
                        Science :{subjects['Science']}
                        Social Science :{subjects['Social Science']}
                        Computer :{subjects['Computer']}
                        Assamese :{subjects['Assamese']}
                        
                        Total: {total}
                        Percentage: {percentage:.2f}%
                        
                        """)

    #Check result of the student
    elif choice =="3":
        name = input("Enter the name of the Student: ")
        if name in student:
            subjects = student[name]
            total =sum(subjects.values())
            percentage = total / len(subjects)
            print(f"\nPercentage: {percentage:.2f}%")
            if percentage >= 90:
                print("Grade: A")
            elif percentage >= 75:
                print("Grade: B")
            elif percentage >= 40:
                print("Grade : C")
            else:
                print("FAIL")

        else:
            print(" Student Not Found! ")
    #4.Delete Student
    elif choice == "4" :
        del_name = input("Enter the name of the student to delete: ")
        if del_name in student:
            del student[del_name]

            #update file after deletion
            with open("students.txt","w") as file:
                for student_name, subjects in student.items():
                    file.write(
                        f"{student_name},"
                        f"{subjects['Math']},"
                        f"{subjects['English']},"
                        f"{subjects['Science']},"
                        f"{subjects['Social Science']},"
                        f"{subjects['Computer']},"
                        f"{subjects['Assamese']}\n"
                    )
            print(f"{del_name} deleted successfully!")
        else:
            print("Student not found!")
    # 5. Update student marks
    elif choice == "5":
        update_name = input("Enter the name of the student: ")
        if update_name in student:
            subject = input("Enter the subject to update: ")
            if subject in student[update_name]:
                try:
                    new_marks = int(input("Enter the new marks: "))

                    #Update only selected subject marks
                    student[update_name][subject] = new_marks
                    #Rewrite updated data into file
                    with open("students.txt","w") as file:
                        for student_name, subjects in student.items():
                            file.write(
                                f"{student_name},"
                                f"{subjects['Math']},"
                                f"{subjects['English']},"
                                f"{subjects['Science']},"
                                f"{subjects['Social Science']},"
                                f"{subjects['Computer']},"
                                f"{subjects['Assamese']}\n"
                            )
                    print(f"{update_name}'s {subject} marks updated successfully")
                except ValueError:
                    print(" Invalid marks input! ")
            else:
                print(" Subject not found! ")
        else:
            print("Student not found! ")

    # 6 . Search Student
    elif choice == "6":

       search_name =input("Enter student name to search: ")
       if search_name in student:
           print(" \nStudent Found! ")
           print("Name: ",search_name)
           print("Marks: ",student[search_name])
       else:
           print(" Student not found! ")
    # 7. Rank List
    elif choice == "7":

        if not student:
            print("No student records found!")

        else:

            ranked_students = sorted(
                student.items(),
                key=lambda x: sum(x[1].values()),
                reverse=True
            )

            print("\n====== RANK LIST ======")

            rank = 1

            for name, subjects in ranked_students:
                total = sum(subjects.values())
                percentage = total / len(subjects)

                print(f"""
    Rank: {rank}
    Name: {name}
    Total: {total}
    Percentage: {percentage:.2f}%
    """)

                rank += 1
    #8. Topper
    elif choice == "8":

        if not student:
            print("No student records found!")

        else:

            topper = max(
                student.items(),
                key=lambda x: sum(x[1].values())
            )

            name = topper[0]
            subjects = topper[1]

            total = sum(subjects.values())
            percentage = total / len(subjects)

            print("\n===== TOPPER =====")

            print(f"""
    Name: {name}
    Total: {total}
    Percentage: {percentage:.2f}%
    """)


    # Exit the application
    elif choice == "9":
        print("Exiting......")
        break
    else:
        print(" In-Valid input! ")


