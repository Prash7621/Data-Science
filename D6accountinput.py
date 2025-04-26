class BankAccount :
    def __init__(self , initialbalance , accountnumber):
        self.initialbalance = initialbalance
        self.accountnumber = accountnumber

    def checkbalance(self):
        print(f"Available Balance : {self.initialbalance}")
    def deposite(self, amount):
        if amount > 0:
            self.initialbalance += amount
            print(f"Deposite  ${amount} . New Balance : ${self.initialbalance}")
        else:
            print("Deposite amount must be positive.")
    
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.initialbalance:
                self.initialbalance -= amount
                print(f"Withdraw ${amount}. New Balance : ${self.initialbalance}")
            else:
                print("Insufficient balance for this withdrwal")
        else:
            print("Withdrwal amount must be positive")
initialbalance=int(input("Enter initial balance : "))
accountnumber=int(input("Enter your account number : "))
deposite_amount=int(input("Enter Amount to deposite : "))
withdrawl_amount=int(input("Enter withdrawl amount : "))
def main():
    account=BankAccount(initialbalance , accountnumber)
    account.checkbalance()
    account.deposite(deposite_amount)
    account.withdraw(withdrawl_amount) 
    account.checkbalance()
    
if __name__ == "__main__":
    main()


