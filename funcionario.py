class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            print("Salário inválido!")

func = Funcionario("Carlos", 5000)

print(f"Nome: {func.get_nome()}, Salário: {func.get_salario()}")

func.set_nome("Ana")
func.set_salario(6000)

print(f"Nome atualizado: {func.get_nome()}, Salário atualizado: {func.get_salario()}")
