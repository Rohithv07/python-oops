
import abc,six,random
from abc import ABCMeta,abstractmethod
from random import randint
@six.add_metaclass(abc.ABCMeta)
class Account():
    @abc.abstractmethod
    def createAccount():
        return 0
    @abc.abstractmethod
    def authenticate():
        return 0
    @abc.abstractmethod
    def withdraw():
        return 0
    @abc.abstractmethod
    def deposit():
        return 0
    @abc.abstractmethod
    def displayBalance():
        return 0
    

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts={}
    def createAccount(self,name,initialDeposit):
        self.accountNumber=randint(10000,99999)
        self.savingsAccounts[self.accountNumber]=[name,initialDeposit]
        print("Account creation successful and the number is:",self.accountNumber)
    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0]==name:
                print("Authentication Successful")
                self.accountNumber=accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentocation Failed")
            return False
        
    def withdraw(self,withdrawAmount):
        if withdrawAmount>self.savingsAccounts[self.accountNumber][1]:
            print("Insufficent Amount")
        else:
            self.savingsAccounts[self.accountNumber][1]-=withdrawAmount
            print("Withdrawal was succesfful")
            self.displayBalance()
    def deposit(self,depositAmount):
        self.savingsAccounts[self.accountNumber][1]+=depositAmount
        print("Deposit was successful")
        self.displayBalance()

    def displayBalance(self):
        print("Available balance:",self.savingsAccounts[self.accountNumber][1])


savingsAccount=SavingsAccount()
while(True):

    print("Enter 1 to create a new account")
    print("Enter 2 to access an exixting account")
    print("Enter 3 to exit")
    userChoice=int(raw_input())
    if userChoice is 1:
        print("ENter your name:")
        name=raw_input()
        print("Enter the initial deposit:")
        deposit=int(raw_input())
        savingsAccount.createAccount(name,deposit)
    elif userChoice is 2:
        print("Enter your name:")
        name=raw_input()
        print("Enter your account number:")
        accountNumber=int(raw_input())
        authenticationStatus=savingsAccount.authenticate(name,accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to previous menu")
                userChoice=int(raw_input())
                if userChoice is 1:
                    print("Enthe the withdrawla amount:")
                    withdrawAmount=int(raw_input())
                    savingsAccount.withdraw(withdrawAmount)
                elif userChoice is 2:
                    print("Enter the amount to be deposited:")
                    depositAmount=int(raw_input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()
