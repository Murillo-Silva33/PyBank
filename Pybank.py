import os
username = "admin"
password = "admin123"
balance = float(1000)
deposit = float()
withdrawal = 0
selection = int()
num_deposits = 0
num_withdrawl = 0
amo_deposits = 0
amo_withdrawl = 0
print("="*7, "PyBank", "="*7, "\n       Sign In\n")
for i in range(3):
    insert_username = input("Insert your username\n")
    insert_password = input("Insert your password\n")

    if insert_username == username and insert_password == password:
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
                    input("Press enter to return to the main menu...")
                    
                case 2:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("=======PyBank Deposit=======")
                    deposit = float(input("Enter the amount you want to deposit: R$"))

                    if deposit <= 0:
                        print("Invalid deposit amount!")
                    else:
                        num_deposits += 1
                        amo_deposits += deposit
                        balance = balance + deposit
                        print("Deposit sucessfull!\n Current Balance:", balance, "R$")
                    input("Press enter to return to the main menu...")
                case 3:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("=======PyBank Withdrawl=======")
                    withdrawal = float(input("Enter the amount you want to withdrawl: R$"))

                    if withdrawal <= 0:
                        print("Invalid withdrawal amount ")
                    else:
                        num_withdrawl += 1
                        amo_withdrawl += withdrawal
                        balance = balance - withdrawal
                        print("Withdrawl completed\n Current Balance:", balance, "R$")
                    input("Press enter to return to the main menu...")
                case 4:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("=======PyBank Hitory=======")
                    print(num_deposits)
                    print(amo_deposits,"R$")
                    print(num_withdrawl)
                    print(amo_withdrawl,"R$")
                    print(balance)
                    input("Press enter to return to the main menu...")
                case 6:
                    if os.name == "nts":
                        os.system("cls")
                    else:
                        os.system("clear")                    
                    print("Thank you for using PyBank\n Exiting...")
                    raise SystemExit
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
