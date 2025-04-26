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

def main():
    account=BankAccount(1000 , 23674317262)
    account.checkbalance()
    account.deposite(500)
    account.withdraw(200) 
    account.checkbalance()
    account.withdraw(2000)
    account.deposite(-100)

if __name__ == "__main__":
    main()


