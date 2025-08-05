# Importa módulo ABC para criar classes abstratas
from abc import ABC, abstractmethod

# Define uma classe base abstrata chamada Pessoa
# ABC significa "Abstract Base Class"
class Pessoa(ABC):
    # Atributo de classe (compartilhado por todas as instâncias)
    especie = "Humano"

    # Construtor: chamado ao criar uma instância
    def __init__(self, nome: str, idade: int):
        # Atributos de instância (únicos para cada objeto)
        self._nome = nome          # Usamos _ para indicar que é protegido
        self.__idade = idade       # Usamos __ para indicar que é privado

    # Método comum: comportamento da classe
    def falar(self, mensagem: str):
        print(f"{self._nome} diz: {mensagem}")

    # Método especial: define como o objeto será impresso
    def __str__(self):
        return f"{self._nome}, {self.__idade} anos"

    # Método especial: define como objetos são comparados
    def __eq__(self, outro):
        return self._nome == outro._nome and self.__idade == outro.__idade

    # Propriedade getter: permite acesso controlado ao atributo privado
    @property
    def idade(self):
        return self.__idade

    # Propriedade setter: permite modificar o atributo com validação
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida")

    # Método abstrato: deve ser implementado pelas subclasses
    @abstractmethod
    def profissao(self):
        pass

    # Método de classe: recebe a própria classe como primeiro argumento
    @classmethod
    def especie_humana(cls):
        print(f"Todos somos da espécie: {cls.especie}")

    # Método estático: não acessa nem a instância nem a classe
    @staticmethod
    def saudacao():
        print("Olá! Seja bem-vindo ao mundo da POO.")

# Subclasse que herda de Pessoa
class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str):
        # Chama o construtor da classe pai
        super().__init__(nome, idade)
        self.curso = curso

    # Implementa o método abstrato
    def profissao(self):
        print("Sou estudante")

    # Sobrescreve o método falar
    def falar(self, mensagem: str):
        print(f"{self._nome} (estudante) diz: {mensagem}")

# Outra subclasse
class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplina: str):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def profissao(self):
        print("Sou professor")

# Demonstração de polimorfismo
def apresentar_profissao(pessoa: Pessoa):
    pessoa.profissao()  # Chama o método correto dependendo da subclasse

# Criação de objetos
joao = Estudante("João", 20, "Engenharia")
maria = Professor("Maria", 40, "Matemática")

# Uso de métodos
joao.falar("Estou estudando POO")
maria.falar("Vamos aprender herança")

# Impressão com __str__
print(joao)
print(maria)

# Comparação com __eq__
print(joao == maria)  # False

# Acesso e modificação com propriedade
print(joao.idade)
joao.idade = 21
print(joao.idade)

# Chamada de método de classe e estático
Pessoa.especie_humana()
Pessoa.saudacao()

# Polimorfismo em ação
apresentar_profissao(joao)
apresentar_profissao(maria)
