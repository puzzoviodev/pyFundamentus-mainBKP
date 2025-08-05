# Importa módulo para criar classes abstratas
from abc import ABC, abstractmethod  # ABC = "Abstract Base Class", ou seja, uma classe base abstrata

# ============================
# CLASSE BASE: Pessoa
# ============================

# Criamos uma classe chamada Pessoa que será abstrata.
# Uma classe abstrata é como um modelo: ela define o que outras classes devem ter,
# mas não pode ser usada diretamente para criar objetos.
class Pessoa(ABC):  # ABC indica que essa classe é abstrata
    # Atributo de classe: é compartilhado por todas as instâncias da classe
    especie = "Humano"  # Todas as pessoas são da espécie "Humano"

    # Método construtor: é chamado automaticamente quando criamos um objeto
    def __init__(self, nome: str, idade: int):
        # Atributos de instância: são dados que pertencem a cada objeto individualmente
        self._nome = nome          # Atributo protegido (por convenção, usamos _ para indicar que não deve ser acessado diretamente)
        self.__idade = idade       # Atributo privado (com __, significa que não pode ser acessado diretamente de fora da classe)

    # Método comum: define uma ação que o objeto pode realizar
    def falar(self, mensagem: str):
        print(f"{self._nome} diz: {mensagem}")

    # Método especial __str__: define como o objeto será exibido quando usamos print()
    def __str__(self):
        return f"{self._nome}, {self.__idade} anos"

    # Método especial __eq__: define como dois objetos são comparados com ==
    def __eq__(self, outro):
        # Compara nome e idade para dizer se os objetos são iguais
        return self._nome == outro._nome and self.__idade == outro._idade

    # ============================
    # PROPRIEDADE: idade
    # ============================

    # Getter: permite acessar o atributo __idade como se fosse público
    # Usamos @property para transformar um método em um "atributo inteligente"
    @property
    def idade(self):
        print("Obtendo idade...")  # Mensagem para mostrar que estamos usando o método
        return self.__idade        # Retorna o valor da idade

    # Setter: permite modificar o atributo __idade com regras
    # Usamos @idade.setter para controlar como a idade pode ser alterada
    @idade.setter
    def idade(self, nova_idade):
        print("Tentando definir nova idade...")
        if nova_idade >= 0:  # Validação: idade não pode ser negativa
            self.__idade = nova_idade
        else:
            print("Idade inválida! Deve ser >= 0")

    # ============================
    # MÉTODOS ESPECIAIS
    # ============================

    # Método abstrato: é um método que não tem implementação aqui
    # Ele serve para obrigar as subclasses (como Estudante e Professor) a criarem esse método
    # Assim garantimos que toda "Pessoa" terá uma profissão definida
    @abstractmethod
    def profissao(self):
        pass  # Aqui não fazemos nada, só dizemos que esse método deve existir nas subclasses

    # Método de classe: acessa a própria classe (não o objeto)
    # Usamos @classmethod quando queremos trabalhar com atributos da classe, como especie
    @classmethod
    def especie_humana(cls):
        print(f"Todos somos da espécie: {cls.especie}")

    # Método estático: não acessa nem a classe nem o objeto
    # Usamos @staticmethod para criar funções úteis que pertencem à classe, mas não dependem dela
    @staticmethod
    def saudacao():
        print("Olá! Seja bem-vindo ao mundo da POO.")

# ============================
# SUBCLASSE: Estudante
# ============================

# Estudante herda de Pessoa, ou seja, Estudante é um tipo de Pessoa
# Herança permite reaproveitar código e criar especializações
class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str):
        # Chama o construtor da classe pai (Pessoa) para definir nome e idade
        super().__init__(nome, idade)
        self.curso = curso  # Atributo específico do estudante

    # Aqui estamos IMPLEMENTANDO o método abstrato profissao
    # Isso é obrigatório, pois Pessoa exige que toda subclasse tenha esse método
    def profissao(self):
        print("Sou estudante")  # Define o que essa pessoa faz

    # Sobrescreve o método falar da classe Pessoa
    # Isso significa que Estudante tem uma versão própria do método falar
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

    # Implementa o método abstrato profissao
    def profissao(self):
        print("Sou professor")

# ============================
# POLIMORFISMO
# ============================

# Polimorfismo significa que diferentes objetos podem responder de formas diferentes à mesma função
# Aqui temos uma função que aceita qualquer objeto do tipo Pessoa
def apresentar_profissao(pessoa: Pessoa):
    # Chama o método profissao da subclasse correta
    pessoa.profissao()  # Se for Estudante, diz "Sou estudante"; se for Professor, diz "Sou professor"

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
# Encapsulamento      → Protege atributos com _ ou __ para evitar acesso direto
# @property           → Permite acessar métodos como se fossem atributos
# @idade.setter       → Permite modificar atributos com regras
# @abstractmethod     → Método obrigatório em subclasses (sem implementação na classe base)
# super()             → Chama métodos da classe pai
# @classmethod        → Método que acessa a classe (cls), útil para atributos de classe
# @staticmethod       → Método que não acessa nem classe nem instância, usado para utilidades
# __str__             → Define como o objeto aparece no print()
# __eq__              → Define como objetos são comparados com ==
# Polimorfismo        → Mesma função, comportamento diferente dependendo da subclasse
