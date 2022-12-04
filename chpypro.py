print("#"*60)
print(" "*20,"... WELCOME ...")
print()
print(" "*24,"XYZ ATM")
print("*"*60)
pin="ankit"
login=input("Enter pin (ankit): ")
print("*"*60)
amount=10000
name="ANKIT"
if pin==login:
    while True:
        if amount<5000:
            print("Low balance")
        print("""I or i for account detail
D or d for cash deposite
W or w for cash withdrawal
C or c for changing pin
E or e for exit""")
        print("-"*30)
        com=input("Enter the command: ")
        print("-"*60)
        if com in "Ii":
            print("Account holder name:",name)
            print("Saving account balance:",amount)
            print("*"*60)
        elif com in "Dd":
            dep=int(input("Enter the amount to be deposited:"))
            amount+=dep
            print("-"*30)
            print("Amount deposited successfully...")
            print("Current balance:",amount)
            print("*"*60)
        elif com in "Ww":
            dep=int(input("Enter the amount to be withdrawn:"))
            amount-=dep
            print("-"*30)
            print("Amount withdrawn successfully...")
            print("Current balance:",amount)
            print("*"*60)
        elif com in "Cc":
            opin=input("Enter the current pin:")
            if opin==pin:
                print("-"*30)
                npin=input("Enter new pin: ")
                print("-"*30)
                pin=npin
                print("Pin changed successfully")
                print("*"*60)
            else:
                print("-"*60)
                print(" "*20,"Wrong pin, Try again..")
                print("*"*60)
        elif com in "Ee":
            print(" "*20,"Thanks, Visit Again")
            print("#"*60)
            break
        else:
            print(" "*15,"Invalid entry, Try again...")
            print("*"*60)
else:
    print(" "*15,"! Invalid pin, Try again...")
    print("#"*60)
