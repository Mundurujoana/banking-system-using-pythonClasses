from datetime import date, datetime
from functools import total_ordering

class Account:
    bank="postbank"
    def __init__(self,acc_name,acc_number):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.acc_balance=0
        self.transaction=100
        self.withdrawals=[]
        self.deposits=[]
        self.bank_both=[]
        self.now =datetime.now()
        self.loan_balance=0
       

        
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount must be greater than zero"
        else:
            self.acc_balance +=amount

        self.deposits.append({"date": self.now.strftime("%d/%m/%y"), "amount": amount,"narration": " deposit"}
)
        return f"Hello {self.acc_name}, you have deposited {amount},and your new balance is {self.acc_balance}"


    def withdraw(self,amount):
         if(amount+self.transaction)>self.acc_balance:
            return f"Insufficient funds"

         elif(amount+self.transaction)<=0:
          return f"amount must be greater than 0"

         else:
          self.acc_balance -= (amount+self.transaction)
          self.withdrawals.append({"date": self.now.strftime("%d/%m/%y"), "amount": amount,"narration": "withdrawal"})

          return f"Hello {self.acc_name}, you have withdrawn {amount}, and a transaction fee of {self.transaction} has been deducted  on your account and your new balance now is {self.acc_balance}"
       

    def deposits_statement(self):
        for depo in self.deposits:
              return f"your withdraw was:{depo}"

    def  withdrawals_statement(self):
        for withdrawal in self.withdrawals:
         return f"your withdraw was:{withdrawal}"

    def current_balance(self):
       return f"Hello{self.acc_name}, you curent balance is {self.acc_balance}"

    def full_statement(self):
          for item in self.bank_both :
            self.bank_both.sort(key=lambda item: item['date'], reverse=True)
            date = item['date']
            amount = item['amount']
            narration = item['narration']
            return f"{date}----------- {narration}----------- {amount}"


    def borrow(self,amount):
      sum = 0
      for depo in self.deposits:
        sum+=depo["amount"]
      # total =  sum([x[amount] for x in self.deposits])

      if len(self.deposits) < 10:
        return f"Hello {self.acc_name},you must have more than 10 deposits to be granted loan"

      elif amount > 100:
        return f"Sorry {self.acc_name},you cannot borrow an amount less than 100"

      elif amount > (sum//3):
        return f"hello{self.acc_name}, you can only qualify for a loan if you have amount upto 1/3 {sum//3}"
      

      elif self.acc_balance==0:
           return f" Hello {self.acc_name} you have an outstanding balance of: {self.acc_balance}"
      elif self.loan_balance>0:
           return f"hello {self.acc_name} you have an outstanding loanbalance of {self.loan_balance}"
      else:

       self.loan_balance+=(amount+(amount*0.03))
       self.acc_balance+=amount
       return f" Hello {self.acc_name} you have borrowed {self.loan_balance} and your balance is {self.loan_balance} with an interest rate of {amount*0.03}"

    def loan_repayment(self,amount):
      if amount <=self.loan_balance:
         self.loan_balance+=amount
         return f"you are not eligible to pay your loan"
      else:
            self.loan_balance-=amount
            overpay = amount - self.loan_balance
            self.acc_balance=0
            return f"Hello {self.acc_name} thank you, your loan of {self.loan_balance} and your current loan balance is {self.loan_balance}"


    def transfer(self,amount,new_account):
      if amount<=0:
            return f"invalid amount"
      elif amount>= self.balance:
            return f"insufficient amount in your account"

      elif isinstance(new_account, Account):
          self.acc_balance-= amount
          new_account.deposit(amount)
          return f"Hello {self.acc_balance},you have sent {amount} to {new_account} and your balance is {self.acc_balance}"








































