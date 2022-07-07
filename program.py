from datetime import date, datetime
class project():
    global bookinfo
    bookinfo = []
    book = open("stock.txt","r")
    books = book.readlines()
    book.close()

    for i in books: # create 2d list from the text file stock.txt
        bookline = i.replace("\n","").split(",")
        bookinfo.append(bookline)

    def display(): #displays the text file stock.txt which contains information of the books
        disp = open("stock.txt","r")
        print("________________________________________________________________________________________________________________________________________________\nBook details\n________________________________________________________________________________________________________________________________________________\nName of Books   |Author	    |Stock	|Price	\n------------------------------------------------------------------------------------------------------------------------------------------------\n"+disp.read())
        disp.close()

    def borrowing(): # to borrow book from the library
        borrowmoney = 0
        borrownote = ""
        borrowedbooks = ""
        booksentered = []
        name = str(input("Enter your name:"))
        issuedate = date.today()
        issuedate1 = str(issuedate.strftime("%d/%m/%Y"))
        day = int(issuedate.strftime("%d"))
        issuetime = datetime.now()
        issuetime1 = str(issuetime.strftime("%H:%M"))
        borrowmore = "yes"
        borrownote = name + "," + issuedate1 + "," + issuetime1
        newbookinfo = ""
        already = False

        while borrowmore.lower() == "yes":
            print("\nInput the assigned numbers of the book to borrow it:\n  1 for The Book Thief\n  2 for Fahrenheit 451\n  3 for The Help\nNote - If you have not returned the book until the duration of 10 days, you will be fined by $1 per day.")
            try:
                bookno = int(input("The book you want to borrow:"))
            except:
                print("Enter the correct datatype")
                exit()
            if bookno == 1:
                for i in range(len(booksentered)): #to check if the book has not been borrowed before
                    if len(booksentered) > 0 and booksentered[i] == 1:
                        already = True
                        break
                    else:
                        already = False
                if already == True:
                    print("The book has already been borrowed")
                    break
                else:
                    if int(bookinfo[0][2]) > 0: #to check if the book is available in stock
                        booksentered.append(bookno)
                        bookinfo[0][2] = str(int(bookinfo[0][2]) - 1)
                        borrowmoney = borrowmoney + int(bookinfo[0][3].replace("$",""))
                        borrowedbooks = borrowedbooks + "The Book Thief" + "/"
                        print("You have successfully borrowed the book")

                    else:
                        print("The book is not in stock")

            elif bookno == 2:
                for i in range(len(booksentered)): #to check if the book has not been borrowed before
                    if (len(booksentered) > 0 and booksentered[i] == 2):
                        already = True
                        break
                    else:
                        already = False
                if already == True:
                    print("The book has already been borrowed")
                    break
                else:
                    if int(bookinfo[1][2]) > 0: # to check if the book is available in stock
                        booksentered.append(bookno)
                        bookinfo[1][2] = str(int(bookinfo[1][2]) - 1)
                        borrowmoney = borrowmoney + int(bookinfo[1][3].replace("$", ""))
                        borrowedbooks = borrowedbooks  + "Fahrenheit 451" + "/"
                        print("You have successfully borrowed the book")
                    else:
                        print("The book is not in stock")


            elif bookno == 3:
                for i in range(len(booksentered)): #to check if the book has not been borrowed before
                    if (len(booksentered) > 0 and booksentered[i] == 3):
                        already = True
                        break
                    else:
                        already = False
                if already == True:
                    print("The book has already been borrowed")
                    break
                else:
                    if int(bookinfo[2][2]) > 0: # to check if the book is available in stock
                        booksentered.append(bookno)
                        bookinfo[2][2] = str(int(bookinfo[2][2]) - 1)
                        borrowmoney = borrowmoney + int(bookinfo[2][3].replace("$", ""))
                        borrowedbooks = borrowedbooks + "The Help" + "/"
                        print("You have successfully borrowed the book")
                    else:
                        print("The book is not in stock")
            else:
                print("Please enter only the assigned number")
            borrowmore = ""
            while borrowmore.lower() != "yes" and borrowmore.lower() != "no":
                borrowmore = str(input("Do you want to borrow more books?\nInput yes or no:"))


        if borrowmore.lower() == "no":
            borrownote = "Note - If you cant return the book until the duration of 10 days, you will be fined by $1 per day.\n________________________________________________________________________________________________________________________________________________\nBorrowed note\n________________________________________________________________________________________________________________________________________________\nName	|Date	|Time	|Price	|Borrowed Books\n------------------------------------------------------------------------------------------------------------------------------------------------\n" + borrownote + "," + "$" + str(borrowmoney) + "," + borrowedbooks + "\n"
            borrownote1 = name + "," + issuedate1.replace("/","-") + "(Borrowed)" + ".txt" #name of the file
            for i in range(len(bookinfo)):  # to convert the 2dlist into string
                word = ""
                for j in range(len(bookinfo[i])):
                    if j == len(bookinfo[i]) - 1:
                        word = word + bookinfo[i][j] + "\n"
                    else:
                        word = word + bookinfo[i][j] + ","
                newbookinfo = newbookinfo + word
            print("\nUpdated book information\n_______________________________________________________________________")
            print(newbookinfo)
            print("\nBorrow note\n_______________________________________________________________________")
            print(borrownote)
            print("\nBorrowed books information")
            borrowread1 = open("stock.txt", "w")
            borrowread1.write(newbookinfo)
            borrowread1.close()

            borrowread2 = open(borrownote1, "w")
            borrowread2.write(borrownote)
            borrowread2.close()

            borrowread3 = open("borrower's names(Not for viewing).txt","a") #to store only the names of the borrowers which is used in return
            borrowread3.write(name+"\n")
            borrowread3.close()

            borrowread4 = open(borrownote1 , "r")
            print(borrowread4.read())
            borrowread4.close()


    def returning(): # to return book from the library

        returnbookinfo = []
        returnbook = open("borrower's names(Not for viewing).txt", "r")
        returnbooks = returnbook.readlines()
        returnbook.close()

        returnername = str(input("Enter your name:"))
        returnmoney = 0
        returnedbooks = ""
        returndate = date.today()
        returndate1 = str(returndate.strftime("%d/%m/%Y"))
        returntime = datetime.now()
        returntime1 = str(returntime.strftime("%H:%M"))
        returnmore = "yes"
        returnnote = returnername + "," + returndate1 + "," + returntime1
        newbookinfo = ""
        booksentered = []
        returnmore = "yes"
        ralready = False
        validreturnname = False

        for i in range(len(returnbooks)): #checks if the name has been registered or not
            if returnername.lower() == returnbooks[i].replace("\n","").lower():
                validreturnname = True
                break
            else:
                validreturnname = False
        if validreturnname == True:
            while returnmore.lower() == "yes":
                print("\nInput the assigned numbers of the book to return it:\n  1 for The Book Thief\n  2 for Fahrenheit 451\n  3 for The Help\nNote - If you have not returned the book until the duration of 10 days, you will be fined by $1 per day.")
                try:
                    returnno = int(input("The book you want to return:"))
                except:
                    print("Enter the correct datatype")
                    exit()
                if returnno == 1:
                    for i in range(len(booksentered)):#to check if the book has been returned before or not
                        if (len(booksentered) > 0 and booksentered[i] == 1):
                            ralready = True
                            break
                        else:
                            ralready = False
                    if ralready == True:
                        print("The book has already been borrowed")
                        break
                    else:
                        booksentered.append(returnno)
                        bookinfo[0][2] = str(int(bookinfo[0][2]) + 1)
                        returnmoney = returnmoney + int(bookinfo[0][3].replace("$", ""))
                        returnedbooks = returnedbooks + "The Book Thief" + "/"
                        print("You have successfully returned the book")
                elif returnno == 2:
                    for i in range(len(booksentered)):#to check if the book has been returned before or not
                        if (len(booksentered) > 0 and booksentered[i] == 2):
                            ralready = True
                            break
                        else:
                            ralready = False
                    if ralready == True:
                        print("The book has already been borrowed")
                        break
                    else:
                        booksentered.append(returnno)
                        bookinfo[1][2] = str(int(bookinfo[1][2]) + 1)
                        returnmoney = returnmoney + int(bookinfo[1][3].replace("$", ""))
                        returnedbooks = returnedbooks + "Fahrenheit 451" + "/"
                        print("You have successfully returned the book")
                elif returnno == 3:
                    for i in range(len(booksentered)):#to check if the book has been returned before or not
                        if (len(booksentered) > 0 and booksentered[i] == 3):
                            ralready = True
                            break
                        else:
                            ralready = False
                    if ralready == True:
                        print("The book has already been borrowed")
                        break
                    else:
                        booksentered.append(returnno)
                        bookinfo[2][2] = str(int(bookinfo[2][2]) + 1)
                        returnmoney = returnmoney + int(bookinfo[2][3].replace("$", ""))
                        returnedbooks = returnedbooks + "The Help" + "/"
                        print("You have successfully returned the book")
                else:
                    print("Please enter only the assigned number")
                returnmore = ""
                while returnmore.lower() != "yes" and returnmore.lower() != "no":
                    returnmore = str(input("Do you want to return more books?\nInput yes or no:"))
        else:
            print("This name has not been registered in our system.")



        if returnmore.lower() == "no":
            returnmin = ""
            while returnmin.lower() != "yes" and returnmin.lower() != "no":
                returnmin = str(input("Have you crossed the 10 days time limit?\nInput yes or no:"))#ask user to input if they have crossed time limit or not
            if returnmin.lower() == "yes":
                try:
                    returnmin1 = int(input("How many days has it been after the 10 days time limit?\nInput only integer:")) #name of the file
                except:
                    print("Enter the correct datatype")
                    exit()
                returnmoney = returnmoney + returnmin1 * 1#if yes add the appropiate values
            returnnote = "Note - If you cant return the book until the duration of 10 days, you will be fined by $1 per day.\n________________________________________________________________________________________________________________________________________________\nReturned note\n________________________________________________________________________________________________________________________________________________\nName	|Date	|Time	|Price	|Returned Books\n------------------------------------------------------------------------------------------------------------------------------------------------\n" + returnnote + "," + "$" + str(returnmoney) + "," + returnedbooks + "\n"
            returnnote1 = returnername + "," + returndate1.replace("/", "-") + "(Returned)" + ".txt"
            print(returnnote)
            for i in range(len(bookinfo)):  # to convert the 2dlist into string
                word = ""
                for j in range(len(bookinfo[i])):
                    if j == len(bookinfo[i]) - 1:
                        word = word + bookinfo[i][j] + "\n"
                    else:
                        word = word + bookinfo[i][j] + ","
                newbookinfo = newbookinfo + word
            print("\nUpdate book information\n_______________________________________________________________________")
            print(newbookinfo)
            print("\nReturnn note\n_______________________________________________________________________")
            print(returnnote)
            print("Returned Books information")
            returnread1 = open("stock.txt", "w")
            returnread1.write(newbookinfo)
            returnread1.close()

            returnread2 = open(returnnote1, "w")
            returnread2.write(returnnote)
            returnread2.close()

            returnread3 = open(returnnote1, "r")
            print(returnread3.read())
            returnread3.close()
