#Question 0
"""
Rectangle=> Area
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

l=float(input("length: "))
w=float(input("Width: "))

rect1 = Rectangle(length=l, width=w)
print(f"Area: {rect1.area()} cm^2")


#Question 5

"""
Bank_Account
"""


class Bank_Account:

    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.name=customer_name
        self.acct=account_number
        self.balance=balance
        self.date=date_of_opening

    """
    To make the balance update when you deposit or withdraw money, 
    you need to update the self.balance attribute 
    of the Bank_Account object within the deposit and withdraw
    """

    def deposit(self,new_deposit):
        self.balance += new_deposit
        print(f"Balance(Before): ${self.balance}")
        print(f"New_Balance: ${self.balance}")

    def withdraw(self,removed):
         print(f"Balance(Before): ${self.balance}")
         if removed <self.balance:
             self.balance -= removed
             print(f"Remained Balance:${self.balance}")
      

    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    

Account1=Bank_Account("00_123_86_45000",9840,"09-10-2023","Ail")
Account1.deposit(new_deposit=float(input("Deposit ($): ")))

options=input("Do you want to withdraw? (yes/no): ")
if options=='yes':
    print('\n')
    print("REMOVE AMOUNT LESS THAN YOUR BALANCE")
    Account1.withdraw(removed=float(input("Remove ($): ")))


print("\n")
Account1.check_balance()


# QUESTION 6
