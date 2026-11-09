class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.__balance += amount
            print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    def get_balance(self):
        return self.__balance


account = BankAccount("Hana", 1000)


print("Account Holder:", account.account_holder)


account.deposit(500)

account.withdraw(200)


print("Current Balance:", account.get_balance())