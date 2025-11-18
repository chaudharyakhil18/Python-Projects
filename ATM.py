class Atm:

    def __init__(self):     # Constructor
        self.pin = ""
        self.balance = 0
        self.menu()        # Calling the Menu() method for the object

    def menu(self):
        while True:
            user_input = input('''Hello, how will you like to proceed?
                                    1. Create Pin
                                    2. Deposit
                                    3. Withdraw
                                    4. Check Balance
                                    5. Exit\n''')
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exiting...")
                break
            else:
                print("Enter Valid Input.")


    def create_pin(self):
        self.pin = input("Enter your pin : ")
        print("Pin set successfully.")

    def deposit(self):
        temp = input("Enter the pin : ")
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            self.balance += amount
            print("Deposited",amount,"successfully.")
        else:
            print("Invalid Pin.")

    def withdraw(self):
        temp = input("Enter the pin : ")
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient Balance.")
        else:
            print("Invalid pin.")

    def check_balance(self):
        temp = input("Enter the pin : ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin.")

sbi = Atm()