# this file will hold the classes for several different types of bank accounts
class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        if type(amount) is int and amount > 0:
            self.balance += amount
            print(f"\nDeposit Complete.")
            self.getBalance()
        else:
            print("\nInvalid Amount Deposited. Please Try Again")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()

        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nBeginning Transfer.. 🚀\n\n")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer Complete! ✅\n\n**********")

        except BalanceException as error:
            print(
                f"\nTransfer Interrupted: ❌ {error}"
            )


class InterestsRewardsAcct(BankAccount):
    def deposit(self, amount):
        # 1.05 to add reward of 5% on amount
        self.balance = self.balance + (amount * 1.05)
        print("\nDepost Complete")
        self.getBalance()


class SavingsAccount(InterestsRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")
