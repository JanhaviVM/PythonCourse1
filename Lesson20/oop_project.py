from bank_accounts import *


Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")


Sarah.getBalance()
Dave.getBalance()

Sarah.deposit(500)

Dave.withdraw(10)

Dave.transfer(10000, Sarah)
Dave.transfer(100, Sarah)

print("\n\n")

Jim = InterestsRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sarah)
Blaze.transfer(1000, Sarah)
