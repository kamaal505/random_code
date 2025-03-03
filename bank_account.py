class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def balance_inquiry(self):
        return self.__balance
    
    def make_deposit(self, amount):
        if amount <= 0:
            print("Amount for deposit can only be a positive number")
            return self.__balance
        
        self.__balance += amount
        return self.__balance
    
    def make_withdrawal (self, amount):
        if amount <= 0:
            print("Amount for withdrawal should be a positive number")
            return self.__balance
        if amount > self.__balance:
            print ("Insufficient balance")
            return self.__balance
        
        self.__balance -= amount
        return self.__balance

account_holder = BankAccount(1000)

def run_interaction():

    while True:
        try:
            message = int(input("Please select an option: For balance inquiry: 1 \nFor deposit: 2\nFor withdrawal 3\nTo exit the app: 4\n"))
            if message == 1:
                print (f"Your current balance is: {account_holder.balance_inquiry()}")
            elif message == 2:
                deposit = float(input("Please enter the amount to deposit: "))
                new_balance = account_holder.make_deposit(deposit)
                print(f"Deposit successful! Your current balance is: {new_balance}")
            elif message == 3:
                withdrawal = float(input("Please enter the amount you'd like to withdraw: "))
                new_balance = account_holder.make_withdrawal(withdrawal)
                if new_balance != account_holder.balance_inquiry():
                    print(f"Your current balance is: {new_balance}")
                else:
                    print("Withdrawal failed. Please check the amount and try again.")
            elif message == 4:
                print("Thank you for banking with us")
                break
            else:
                print("Invalid option; please select a valid option fromt the menu (1-4)")

        except ValueError:
            print("Invalid input. Please enter a valid number")

run_interaction()
            
