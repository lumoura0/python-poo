#  Um decorador é um tipo especial de função que permite modificar ou
#  estender o comportamento de outras funções,
#  sem precisar alterar o código original delas.

def decorator_func(func):
    def wrapper():
        # Ação antes da chamada da função original
        print("Executando a função antes da chamada")
        func()  # Chamada da função original
        print("Depois da função ser chamada")
    return wrapper

# Definindo uma função simples

@decorator_func
def func_simples():
    print("Função simples")

# Chamando a função decorada

func_simples()

class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("Executando a função antes da chamada")
        self.func()
        print("Depois da função ser chamada")
    

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda Função decorada")

segunda_funcao()