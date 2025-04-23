from datetime import datetime
from typing import List
from abc import ABC, abstractmethod 

class Authenticable(ABC):
    @abstractmethod
    def authenticate(self, password:str)->bool:
        pass

class Taxable(ABC):
    @abstractmethod
    def get_tax_value(self) ->bool :
        pass
    
class Rentable(ABC):
    @abstractmethod
    def get_profitability_value(self) ->bool :
        pass
    

class Bank:
    def __init__(self, name: str, cnpj: str, adress: str, phone: str):
        self._name = name
        self._cnpj = cnpj
        self._adress = adress
        self._phone = phone
        self._bankbranch: List['BankBranch'] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    
    def add_bankbranch(self, bankbranch: 'BankBranch'):
        self._bankbranch.append(bankbranch)


class BankBranch:
    def __init__(self, number:str,name:str, adress: str, phone : str):
        self._number = number
        self._adress = adress
        self._phone = phone
        self._name = name
        self._contas: List['Account'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Person:
    pass

class Customer:
    pass

class Employee:
    pass

class Transaction:
    def __init__(self, typev:str, value:float, account: 'Account'):
        self._typev = typev
        self._value = value
        self._account = account
        self._date = datetime.now()

    @property
    def typev(self):
        return self._typev

    @typev.setter
    def typev(self, value):
        self._typev = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value


        
class Account:

    def __init__(
        self,
        number: str,
        holder: str,
        balance: float,
        password: str,
    ):
        self._number = number
        self._holder = holder
        self._password = password
        self._balance = balance
        self._transactions: List['Transaction'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, value):
        self._holder = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def authenticate(self, password: str):
        return self._password == password
    
    def withdraw(self, value: float):
        if value > self._balance:
            raise ValueError("Saldo insuficiente")
        self._balance -= value
        self._transactions.append(Transaction("WITHDRAW", -value, self))

    def deposit(self, value: float):
        if value <= 0:
            raise ValueError("Valor do depósito deve ser positivo")
        self._balance += value
        self._transactions.append(Transaction("DEPOSIT", value, self))
    
    def print_statement(self):
        if not self._transactions:
            print(" Nenhuma transação registrada.")
        else:
            header = f"""
            === BANK STATEMENT ===
            ----------------------------------------
            Holder: {self._holder}
            Account: {self._number}
            Balance: R$ {self._balance:.2f}
            ----------------------------------------
            TRANSACTIONS:
            """
            print(header)
            
            for t in self._transactions:
                print(f"[{t._date.strftime('%d/%m/%Y %H:%M')}] {t._typev}: R$ {t._value:+.2f}") 
            
            print("----------------------------------------")

class CurrentAccount(Account):
    def __init__(self, number: str, holder: str, balance: float, password: str, limit: float):
        super().__init__(number, holder, balance, password)
        self._limit = limit
        self._fee_maintance = 10.0  # class a, b, c

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    @property
    def fee_maintance(self):
        return self._tax_maintance

    @fee_maintance.setter
    def fee_maintance(self, value):
        self._tax_maintance = value


class SavingAccount(Account):
    def __init__(self, number: str, holder: str, balance: float, password: str, yield_rate: float):
        super().__init__(number, holder, balance, password)
        self._yield_rate = yield_rate
        self._birthday = datetime.now().day

    @property
    def _yield_rate(self):
        return self._yield_rate

    @_yield_rate.setter
    def yield_rate(self, value):
        self._yield_rate = value

    @property
    def birthday(self):
        return self._birthday

conta01 = Account(1, "Walter", 0, "beto")

conta01.deposit(11.0)
conta01.withdraw(10.0)
conta01.print_statement()