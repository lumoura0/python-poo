print("\nExemplo de herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f"{self.nome} está andando")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"

dog = Cachorro(nome="Max")
cat = Gato(nome="Cat")
print("\nExemplo de Polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz {animal.emitir_som()}")

print("\nExemplo de encapsulamento")

class ContaBancaria:
    def __init__(self,  saldo) -> None:
        self.__saldo = saldo # atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    

conta = ContaBancaria(saldo=800)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta: {conta.consultar_saldo()}")

print("\nExemplo de abstração")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado"

    def desligar(self):
        return "Carro desligado"

carro1 = Carro()

print(carro1.ligar())