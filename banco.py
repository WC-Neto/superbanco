from datetime import datetime
from typing import List
class Bank:
    def __init__(self, name: str, cnpj: str, adress: str, phone: str):
        self._name = name
        self._cnpj = cnpj
        self._adress = adress
        self._phone = phone
        self._bankbranch: List['BankBranch'] = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, value):
        self._fone = value
    
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

class Pessoa:
    pass

class Cliente:
    pass

class Funcionario:
    pass

class Transation:
    def __init__(self, tipo:str, valor:float, conta: 'Account'):
        self._tipo = tipo
        self._valor = valor
        self._conta = conta
        self._data = datetime.now()

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, value):
        self._conta = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


        
class Account:

    def __init__(
        self,
        number: str,
        titular: str,
        saldo: float,
        senha: str,
    ):
        self._number = number
        self._titular = titular
        self._senha = senha
        self._saldo = saldo
        self._transacoes: List['Transacao'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        self._titular = value

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value):
        self._senha = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    def autenticar(self, senha: str):
        pass
    
    def sacar(self, valor: float):
        pass

    def depositar(self, valor: float):
        pass
    
    def extrato(self):
        pass

    def imprimir_extrato(self):
        pass

class CurrentAccount(Account):
    def __init__(self, number: str, titular: str, saldo: float, senha: str, limite: float):
        super().__init__(number, titular, saldo, senha)
        self._limite = limite
        self._taxa_manutencao = 10.0  # class a, b, c

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        self._limite = value

    @property
    def taxa_manutencao(self):
        return self._taxa_manutencao

    @taxa_manutencao.setter
    def taxa_manutencao(self, value):
        self._taxa_manutencao = value


class ContaPoupanca(Account):
    def __init__(self, number: str, titular: str, saldo: float, senha: str, taxa_rendimento: float):
        super().__init__(number, titular, saldo, senha)
        self._taxa_rendimento = taxa_rendimento
        self._data_aniversario = datetime.now().day

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, value):
        self._taxa_rendimento = value

    @property
    def data_aniversario(self):
        return self._data_aniversario
