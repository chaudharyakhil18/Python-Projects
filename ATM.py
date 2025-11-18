class Atm:

    def __init__(self):     # Constructor
        self.__pin = ""         # Private variable
        self.__balance = 0      #    "      "
        self.__menu()           #    "      "

    def get_pin(self):                  # Getter Method
        print("Pin =",self.__pin)

    def set_pin(self,new_pin):          # Setter Method
        if type(new_pin) is str:
            self.__pin = new_pin
            print("Pin set successfully.")
        else:
            print("Invalid format.")

    def __menu(self):       # Private method
        while True:
            user_input = input('''Hello, how will you like to proceed?
                                    1. Create Pin
                                    2. Deposit
                                    3. Withdraw
                                    4. Check Balance
                                    5. Get Pin
                                    6. Set Pin
                                    7. Exit\n''')
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                self.get_pin()
            elif user_input == "6":
                new_pin = input("Enter new pin : ")
                self.set_pin(new_pin)
            elif user_input == "7":
                print("Exiting...")
                break
            else:
                print("Enter Valid Input.")


    def create_pin(self):
        self.__pin = input("Enter your pin : ")
        print("Pin set successfully.")

    def deposit(self):
        temp = input("Enter the pin : ")
        if temp == self.__pin:
            amount = int(input("Enter the amount : "))
            self.__balance += amount
            print("Deposited",amount,"successfully.")
        else:
            print("Invalid Pin.")

    def withdraw(self):
        temp = input("Enter the pin : ")
        if temp == self.__pin:
            amount = int(input("Enter the amount : "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient Balance.")
        else:
            print("Invalid pin.")

    def check_balance(self):
        temp = input("Enter the pin : ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin.")

sbi = Atm()