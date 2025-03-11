# POO

# Classe exemplo
class Pessoa:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

pessoa1 = Pessoa("Shiro", 2)
print(pessoa1.name)
print(pessoa1.age)