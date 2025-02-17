class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo de {self.__titular}: R$ {self.__saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque!")
