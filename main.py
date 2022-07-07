from program import project
class main():
    print("Welcome to Library Management system")
    print("______________________________________")
    print("\nPlease enter the assigned number of the task\n  1 for displaying book and its information\n  2 for borrowing book\n  3 for returning book\n  4 for exiting the program")
    try:
        run = int(input("Enter the number:"))
    except:
        print("Enter the correct datatype")
        exit()
    while run != 4:
        if run != 1 and run != 2 and run != 3:
            print("Please enter only the assigned numbers")
        elif run == 1:
            project.display()
        elif run == 2:
            project.borrowing()
        elif run == 3:
            project.returning()

        print("\nPlease enter the assigned number of the task\n  1 for displaying book and its information\n  2 for borrowing book\n  3 for returning book\n  4 for exiting the program")
        try:
            run = int(input("Enter the number:"))
        except:
            print("Enter the correct datatype")
            exit()
    if run == 4: #if 4 is entered then the program end witht a message due to while loop and if statement
        print("Thank you using our services")

