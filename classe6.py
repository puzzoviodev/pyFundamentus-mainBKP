# Importa módulo para criar classes abstratas
from abc import ABC, abstractmethod

# ============================
# CLASSE BASE: Pessoa
# ============================

# Criamos uma classe abstrata chamada Pessoa
# ABC significa "Abstract Base Class", ou seja, uma classe que não pode ser instanciada diretamente
class Pessoa(ABC):
    # Atributo de classe: é compartilhado por todas as instâncias
    especie = "Humano"

    # Método construtor: chamado automaticamente quando criamos um objeto
    def __init__(self, nome: str, idade: int):
        # Atributos de instância: únicos para cada objeto
        self._nome = nome          # Atributo protegido (por convenção, com _)
        self.__idade = idade       # Atributo privado (com __, não acessível diretamente)

    # Método comum: comportamento que o objeto pode executar
    def falar(self, mensagem: str):
        print(f"{self._nome} diz: {mensagem}")

    # Método especial: define como o objeto será exibido com print()
    def __str__(self):
        return f"{self._nome}, {self.__idade} anos"

    # Método especial: define como objetos são comparados com ==
    def __eq__(self, outro):
        return self._nome == outro._nome and self.__idade == outro._idade

    # ============================
    # PROPRIEDADE: idade
    # ============================

    # Getter: permite acessar __idade como se fosse um atributo
    @property
    def idade(self):
        print("Obtendo idade...")
        return self.__idade

    # Setter: permite modificar __idade com validação
    @idade.setter
    def idade(self, nova_idade):
        print("Tentando definir nova idade...")
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida! Deve ser >= 0")

    # ============================
    # MÉTODOS ESPECIAIS
    # ============================

    # Método abstrato: obriga subclasses a implementarem esse método
    @abstractmethod
    def profissao(self):
        pass

    # Método de classe: acessa a própria classe, útil para atributos de classe
    @classmethod
    def especie_humana(cls):
        print(f"Todos somos da espécie: {cls.especie}")

    # Método estático: não acessa nem a instância nem a classe
    @staticmethod
    def saudacao():
        print("Olá! Seja bem-vindo ao mundo da POO.")

# ============================
# SUBCLASSE: Estudante
# ============================

# Estudante herda de Pessoa
class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str):
        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome, idade)
        self.curso = curso  # Atributo específico do estudante

    # Implementa o método abstrato
    def profissao(self):
        print("Sou estudante")

    # Sobrescreve o método falar
    def falar(self, mensagem: str):
        print(f"{self._nome} (estudante) diz: {mensagem}")

# ============================
# SUBCLASSE: Professor
# ============================

# Professor também herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplina: str):
        super().__init__(nome, idade)
        self.disciplina = disciplina  # Atributo específico do professor

    def profissao(self):
        print("Sou professor")

# ============================
# POLIMORFISMO
# ============================

# Função que aceita qualquer objeto do tipo Pessoa
def apresentar_profissao(pessoa: Pessoa):
    # Chama o método profissao da subclasse correta
    pessoa.profissao()

# ============================
# TESTES E DEMONSTRAÇÃO
# ============================

# Cria objetos
joao = Estudante("João", 20, "Engenharia")
maria = Professor("Maria", 40, "Matemática")

# Usa métodos
joao.falar("Estou estudando POO")
maria.falar("Vamos aprender herança")

# Imprime objetos (usa __str__)
print(joao)
print(maria)

# Compara objetos (usa __eq__)
print(joao == maria)  # False

# Acessa e modifica idade com propriedade
print(joao.idade)     # Chama o getter
joao.idade = 21       # Chama o setter
print(joao.idade)

# Tenta definir idade inválida
joao.idade = -5       # Setter rejeita

# Chama método de classe e estático
Pessoa.especie_humana()
Pessoa.saudacao()

# Polimorfismo: mesma função, comportamento diferente
apresentar_profissao(joao)
apresentar_profissao(maria)
