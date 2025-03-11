# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10
    def __init__(self, nome) -> None:
        self.nome = nome
    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.valor}"

    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para {cls.valor}"

    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"

obj = MinhaClasse(nome="Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)

print(MinhaClasse.metodo_classe())

print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def novo_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
config1 = "Toyota, Corolla,2022"
carro1 = Carro.novo_carro(config1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b
    
print(Matematica.soma(5, 3))