import json
class User:
    def __init__(self):
        self.name=""
        self.balance=0
        self.pin=""


    def user_menu(self):
        while True:
            user_input=input("1.Deposit \n2.Withdraw \n3.Check Balance\n4.Change Pin\n5.Delete Account\n6.Exit\nEnter your choice: ")
            if user_input=='1':
                self.deposit()
            elif user_input=='2':
                self.withdraw()
            elif user_input=='3':
                self.check_balance()
            elif user_input=='4':
                self.change_pin()
            elif user_input=='5':
                deleted=self.delete_account()
                if deleted:
                    return

            elif user_input=='6':
                self.current_user = None
                print("Logged out successfully")

            else:
                print("invalid choice")

    def deposit(self):
        while True:
            amount=input("Enter amount:")
            if amount.isnumeric():
                amount=int(amount)

                if amount > 0:
                    self.current_user['balance']+=amount
                    self.save_users()
                    print("Deposit successful\nYour balance is : ",self.current_user['balance'])

                elif amount <= 0:
                    print("Please enter a positive number")

            else:
                print("Please enter a number")
            while True:

                choice = input("do you want to deposit more(y/n) ").lower()

                if choice == "y":
                    break
                elif choice == "n":
                    return
                elif choice != "y" and choice != "n":
                    print("Please enter y or n")
                    continue

    def withdraw(self):
        while True:
            amount=input("Enter amount to withdraw: ")
            if amount.isnumeric():
                amount=int(amount)
                if amount > self.current_user['balance']:
                    print("insufficient funds\nYour balance is : ",self.current_user['balance'])
                elif amount <= self.current_user['balance']:
                    self.current_user['balance']-=amount
                    self.save_users()
                    print("Withdraw successful\nYour balance is : ",self.current_user['balance'])
            else:
                print("Please enter a number")
            while True:
                choice = input("do you want to withdraw more(y/n) ").lower()
                if choice == "y":
                    break
                elif choice == "n":
                    return
                elif choice != "y" and choice != "n":
                    print("Please enter y or n")
                    continue

    def check_balance(self):
        print("Your balance is : ",self.current_user['balance'])
        user_choice = input("press any key to go back")
        return

    def change_pin(self):

        current_pin = input("Enter your current pin: ")

        if current_pin.isnumeric():

            current_pin = int(current_pin)

            if self.current_user['pin'] == current_pin:

                while True:

                    new_pin = input("Enter your new pin: ")

                    if new_pin.isnumeric():

                        new_pin = int(new_pin)

                        self.current_user['pin'] = new_pin
                        self.save_users()
                        print("PIN changed successfully")

                        return

                    else:
                        print("Please enter a valid pin")

            else:
                print("PIN mismatch, please enter a valid pin")

        else:
            print("Please enter a numeric pin")



    def delete_account(self):

        while True:
            pin = input("Enter your pin: ")
            if pin.isnumeric():
                pin = int(pin)

                if self.current_user['pin'] == pin:
                    print("correct PIN")
                    while True:
                        choice = input("do you want to delete account(y/n) ").lower()
                        if choice == "y":
                            self.users.remove(self.current_user)
                            self.save_users()
                            self.current_user=None
                            print("account deleted")
                            return True
                        if choice == "n":
                            print("account deletetion cancelled")
                            return  False
                        else:
                            print("please enter a y or n")
                            continue
                else:
                    print("Account credentials doesn't match")
                    return
            else:
                print("Please enter a valid pin")




class Atm(User):
    def __init__(self):
        self.name=''
        self.pin=''
        self.balance=0
        self.current_user=None
        try:
            with open("atm.json","r") as f:
                self.users=json.load(f)
        except FileNotFoundError:
            self.users=[]
        if self.users:
            self.account_no=max(user["Account number"] for user in self.users)
        else:
            self.account_no=0
    def save_users(self):
        with open("atm.json","w") as f:
            json.dump(self.users,f,indent=4)
    def atm_menu(self):
        while True:
            user_input=input("1.Create Account\n2.Log in \n3.Exit\nEnter your choice: ")
            if user_input=='1':
                self.create_account()
            elif user_input=='2':
                self.login()
            elif user_input=='3':
                exit()
            else:
                print("invalid choice")

    def create_account(self):
        while True:
            name=input("Enter your name: ")
            if name.isalpha():
                break
            else:
                print("Please enter a valid name")
                continue
        while True:
            pin=input("Enter your pin: ")
            if pin.isnumeric():
                pin=int(pin)
                break
            else:
                print("Please enter a valid pin")
                continue
        while True:
            amount=input("Enter your balance:")
            if amount.isnumeric() and int(amount) > 0:
                amount = int(amount)
                break
            elif amount.isnumeric() and amount <= 0:
                print("Please enter a positive number")
                continue
            else:
                print("Please enter a valid number")
                continue
        self.account_no+=1
        user={
            "Account number":self.account_no,
            "name":name,
            "pin":pin,
            "balance":amount,
        }
        self.users.append(user)
        self.save_users()
        print("Account created successfully\n" 'Your account number is',self.account_no,"\nYour balance is : ",self.users[0]['balance'])
        print(self.users)

    def login(self):
        while True:
            account_no=input("Enter your account number: ")
            pin=input("Enter your pin: ")
            if account_no.isnumeric() and pin.isnumeric():
                account_no=int(account_no)
                pin=int(pin)
                for account in self.users:
                    if account['Account number'] == account_no and account['pin'] == pin:
                        self.current_user=account
                        print(account['name'],"account number",account_no,"is logged in")
                        self.user_menu()
                        break
                else:
                    print("User not found ")
                    break
                break
            else:
                print("Please enter a valid account number or password")


#u1=User()
#u1.user_menu()
r1=Atm()
r1.atm_menu()
