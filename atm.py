class Account:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited Rs{amount}. New balance: Rs{self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew Rs{amount}. New balance: Rs{self.balance}"
        else:
            return "Insufficient funds"

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None

    def create_account(self, user_id, pin, initial_balance):
        account = Account(user_id, pin, initial_balance)
        self.accounts[user_id] = account

    def login(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id].pin == pin:
            self.current_user = self.accounts[user_id]
            return "Login successful"
        else:
            return "Invalid user ID or PIN"

    def logout(self):
        self.current_user = None

    def menu(self):
        while self.current_user:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Balance: Rs{self.current_user.check_balance()}")
            elif choice == "2":
                amount = float(input("Enter deposit amount: Rs"))
                print(self.current_user.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: Rs"))
                print(self.current_user.withdraw(amount))
            elif choice == "4":
                self.logout()
                print("Logged out")
            else:
                print("Invalid choice")

if __name__ == "__main__":
    atm = ATM()
    atm.create_account("user1", "1234", 1000.0)
    atm.create_account("user2", "5678", 500.0)

    while True:
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")

        login_result = atm.login(user_id, pin)
        print(login_result)

        if login_result == "Login successful":
            atm.menu()
