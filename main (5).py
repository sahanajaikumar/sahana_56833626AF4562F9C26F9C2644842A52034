class BankAccount:

  def __init__(self, account_number, account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      #self.__account_balnce = self.__account_balance+amount
      print("deposited RS{}. New balance: RS{}".format(amount,

self.__account_balance))
    else:
      print("Invalid deposit amount. please deposit a positive amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      # self.__account_balance = self.__account_balance - amount
      print("withdraw RS{}. New balance: RS{}".format(amount,
                                                      
self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficiant balance.")
  def display_balance(self):
      print("Account balance for {} (Account #{}): RS{}".format(
      self.__account_holder_name, self.__account_number,
      self.__account_balance))
# creat an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      account_holder_name="sahana",
                      initial_balance=5000.0)

# test deposit and withdrawal functionality
account.display_balance()
#account.deposit(500.0)
#account.withdraw(200.0)
#account.display_balance()               