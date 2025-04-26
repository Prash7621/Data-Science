class bankaccount :
    def __init__(self , accountnumber , initialbalance):
          self.accountnumber = accountnumber
          self.initialbalance = initialbalance
    def checkbalance(self):
         print(f"Available balance : {self.initialbalance}")
    def deposite(self , amount):
         if amount > 0:
          self.initialbalance += amount
          print(f"Deposited amount : ${amount} . New balance ${self.initialbalance}")
         else:
             print("DEposite amount must be positive.")
    def withdraw(self , amount):
         if amount > 0:
              if amount <= self.initialbalance:
               self.initialbalance -= amount
               print(f"withdraw : ${amount} . New balance : ${self.initialbalance}")
              else:
                print("Insufficient balance for this withdrwal")
         else:
            print("Withdrwal amount must be positive")

def main():
    print("Welcome to the Bank Account Manager!")
    account_number=int(input("Enter your account number : "))
    initial_balance=float(input("Enter your initial balance : "))
    account = bankaccount(account_number, initial_balance)
    print(account.accountnumber)
    while True:
        try:
          print("1.check balance")
          print("2.deposite")
          print("3.withdraw")
          print("4.exit")
          choice = int(input("Enter your choice : "))
          if choice == 1:
               account.checkbalance()
          elif choice == 2:
               amount = float(input("Enter the amount to be deposited : "))
               account.deposite(amount)
          elif choice == 3:
               amount = float(input("Enter the amount to be withdrawn : "))
               account.withdraw(amount)
          elif choice == 4:
               break
          else:
               print("Invalid choice")
        except ValueError:
           print("Invalid amount")
      

if __name__=="__main__":
  main()