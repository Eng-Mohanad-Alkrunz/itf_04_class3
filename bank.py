import datetime
import random


class Transaction:


    def __init__(self,amount,type,id):
        self.amount = amount
        self.type = type
        self.date = datetime.date.today()
        self.id  = id


    def get_transaction(self):
        print(self.id,"|\t\t",self.amount,"|\t\t|",self.type,"|\t\t",self.date)


class Account:

    def __init__(self,account_number,client_name):
        self._account_number = account_number
        self._client_name = client_name
        self._balance = 0
        self._transactions = []


    def get_account_number(self):
        return self._account_number

    def get_client_name(self):
        return self._client_name

    def __generate_id(self):
        id_list = []
        for transaction in self._transactions:
            id_list.append(transaction.id)
        while True:
            temp = random.randint(10000,99999)
            if temp not in id_list:
                return temp

    def deposit(self,amount):
        if amount >= 0:
            self._balance += amount
            transaction = Transaction(amount,"Deposit",self.__generate_id())
            self._transactions.append(transaction)
            print("Deposit Done Successfully")
        else:
            print("Insufficient Process")

    def withdrawal(self,amount):
        if amount >= 0 and amount <= self._balance:
            self._balance -= amount
            transaction = Transaction(amount, "Withdrawal",self.__generate_id())
            self._transactions.append(transaction)
            print("Withdrawal Done Successfully")
        else:
            print("Insufficient Process")

    def get_transactions(self):
        print("ID","|\t\t","Amount","|\t\t|","Type","|\t\t","Date")
        print("__________________")
        for transaction in self._transactions:
            transaction.get_transaction()
        print("__________________")
        print("Total Balance = ",self._balance)


account_1 = Account("00000","Mohanad")
account_1.deposit(100)
account_1.withdrawal(10)
account_1.withdrawal(20)
account_1.withdrawal(30)
account_1.get_transactions()
print(account_1.get_account_number())
print(account_1.get_client_name())
