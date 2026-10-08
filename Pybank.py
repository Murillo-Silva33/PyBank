import os
username = "admin"
password = "admin123"
balance = float(1000)
deposit = float()
selection = int()
print("=======PyBank=======\n     Sing in\n")
for i in range(3):
    insert_username = input("Insert your username\n")
    insert_passoword = input("Insert your password\n")

    if insert_username == username and insert_passoword == password:
        if os.name == "nts":
            os.system("cls")
        else:
            os.system("clear")
        while True:
            selection = int(input("=======Pybank Main Menu=======\n[1]-Balance\n[2]-Deposit\n[3]-Withdrawal\n[4]-Transaction History\n[5]-Input validation\n[6]-Exit\n"))
            match selection:
                case 1:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("=======PyBank=======\nBalance:", balance)
                    input("Press enter to main menu...")
                case 2:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("=======PyBank Deposit=======")
                    deposit = float(input("Enter the amount you want to deposit: R$"))

                    if deposit < 0:
                        print("Invalid deposit amount!")
                    else: 
                        balance = balance + deposit
                        print("Deposit sucefull\n Current Balance: R$", balance)
                    input("Press enter to main menu...")
                case 6:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")                    
                    print("Thank you for using PyBank\n Exiting...")
                    break
                case _:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("Invalid option! Please try again.")
                    input("Press enter to main menu..")
    else:
        print("Incorrect username or password. Please try again.")
print("Maximum number of attempts exceeded. Please try again later.")
