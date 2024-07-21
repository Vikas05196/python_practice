#nested if else statement.

student_gpa =float(input("enter a student gpa."))
student_laon =input("enter yes or no.")

if student_gpa>3.5:
    if student_laon == "yes":
        print("student is eligible for loan.")
    else:
        print("due to less grade student are not eligible.")
else:
    print("please work hard to get student laon.")        
            