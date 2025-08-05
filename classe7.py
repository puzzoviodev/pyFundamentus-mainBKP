# Importa módulo para criar classes abstratas
from abc import ABC, abstractmethod  # ABC = Abstract Base Class

# ============================
# CLASSE BASE: Pessoa
# ============================

# Criamos uma classe abstrata chamada Pessoa
# Uma classe abstrata serve como modelo e não pode ser instanciada diretamente
class Pessoa(ABC):
    # Atributo de classe: é compartilhado por todas as instâncias da classe
    especie = "Humano"

    # Método construtor: chamado automaticamente ao criar um objeto
    def __init__(self, nome: str, idade: int):
        # Atributos de instância: únicos para cada objeto
        self._nome = nome          # Atributo protegido (por convenção, com _)
        self.__idade = idade       # Atributo privado (com __, não acessível diretamente)

    # Método comum: define um comportamento da classe
    def falar(self, mensagem: str):
        print(f"{self._nome} diz: {mensagem}")

    # Método especial __str__: define como o objeto será exibido com print()
    def __str__(self):
        return f"{self._nome}, {self.__idade} anos"

    # Método especial __eq__: define como objetos são comparados com ==
    def __eq__(self, outro):
        return self._nome == outro._nome and self.__idade == outro._idade

    # ============================
    # PROPRIEDADE: idade
    # ============================

    # Getter: permite acessar __idade como se fosse um atributo comum
    @property
    def idade(self):
        print("Obtendo idade...")  # Mensagem para mostrar que é um método
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
        pass  # Não tem implementação aqui, será definido nas subclasses

    # Método de classe: acessa atributos da própria classe
    @classmethod
    def especie_humana(cls):
        print(f"Todos somos da espécie: {cls.especie}")

    # Método estático: não acessa nem atributos da classe nem da instância
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

    # Implementa o método abstrato obrigatoriamente
    def profissao(self):
        print("Sou estudante")

    # Sobrescreve o método falar da classe pai
    def falar(self, mensagem: str):
        print(f"{self._nome} (estudante) diz: {mensagem}")

# ============================
# SUBCLASSE: Professor
# ============================

# Professor também herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplina: str):
        # Chama o construtor da classe pai
        super().__init__(nome, idade)
        self.disciplina = disciplina  # Atributo específico do professor

    # Implementa o método abstrato obrigatoriamente
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

# Cria objetos das subclasses
joao = Estudante("João", 20, "Engenharia")
maria = Professor("Maria", 40, "Matemática")

# Usa métodos específicos de cada objeto
joao.falar("Estou estudando POO")       # Método sobrescrito
maria.falar("Vamos aprender herança")   # Método herdado

# Imprime objetos (usa __str__)
print(joao)  # João, 20 anos
print(maria) # Maria, 40 anos

# Compara objetos (usa __eq__)
print(joao == maria)  # False, pois nome e idade são diferentes

# Acessa e modifica idade com propriedade
print(joao.idade)     # Chama o getter
joao.idade = 21       # Chama o setter
print(joao.idade)

# Tenta definir idade inválida
joao.idade = -5       # Setter rejeita

# Chama método de classe e estático
Pessoa.especie_humana()  # Todos somos da espécie: Humano
Pessoa.saudacao()        # Olá! Seja bem-vindo ao mundo da POO.

# Polimorfismo: mesma função, comportamento diferente
apresentar_profissao(joao)   # Sou estudante
apresentar_profissao(maria)  # Sou professor

# ============================
# RESUMO DOS CONCEITOS USADOS
# ============================

# class               → Cria uma estrutura personalizada (classe)
# __init__            → Construtor, executado ao criar o objeto
# self                → Referência ao próprio objeto
# Atributos           → Variáveis que pertencem ao objeto (ex: nome, idade)
# Métodos             → Funções dentro da classe (ex: falar, profissao)
# Herança             → Subclasses herdam atributos e métodos da classe pai
# Encapsulamento      → Protege atributos com _ ou __
# @property           → Permite acessar métodos como se fossem atributos
# @idade.setter       → Permite modificar atributos com validação
# @abstractmethod     → Método obrigatório em subclasses
# super()             → Chama métodos da classe pai
# @classmethod        → Método que acessa a classe (cls)
# @staticmethod       → Método que não acessa nem classe nem instância
# __str__             → Define como o objeto aparece no print()
# __eq__              → Define como objetos são comparados com ==
# Polimorfismo        → Mesma função, comportamento diferente dependendo da subclasse
