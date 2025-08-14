# Importa o módulo datetime da biblioteca padrão do Python.
# Esse módulo permite trabalhar com datas e horas.
import datetime

# Define uma classe chamada Cliente, que representa um cliente bancário.
class Cliente:
    # Método especial __init__ é o construtor da classe.
    # Ele é chamado automaticamente quando um novo objeto Cliente é criado.
    def __init__(self, nome, sobrenome, cpf):
        # Atributo 'nome' armazena o primeiro nome do cliente.
        self.nome = nome
        # Atributo 'sobrenome' armazena o sobrenome do cliente.
        self.sobrenome = sobrenome
        # Atributo 'cpf' armazena o CPF do cliente, que é um identificador único.
        self.cpf = cpf

# Define uma classe chamada Conta, que representa uma conta bancária.
class Conta:
    # Método construtor da classe Conta.
    def __init__(self, numero, titular, saldo, limite=1000.0):
        # Imprime uma mensagem no console informando que uma conta está sendo inicializada.
        print("Inicializando uma conta")
        # Atributo 'numero' armazena o número da conta.
        self.numero = numero
        # Atributo 'titular' armazena o cliente associado à conta.
        self.titular = titular
        # Atributo 'saldo' armazena o valor atual disponível na conta.
        self._saldo = saldo
        # Atributo 'limite' define o limite de crédito da conta (valor padrão: 1000.0).
        self.limite = limite
        # Atributo 'historico' armazena um objeto da classe Historico, que registra as transações.
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")

        else:
            self._saldo = saldo



    # Método para realizar depósitos na conta.
    def deposita(self, valor):
        # Adiciona o valor depositado ao saldo atual.
        self.saldo += valor
        # Registra a transação no histórico da conta.
        self.historico.transacoes.append("depósito de {}".format(valor))

    # Método para realizar saques da conta.
    def saca(self, valor):
        # Verifica se o saldo é suficiente para o saque.
        if self.saldo < valor:
            # Se não houver saldo suficiente, retorna False.
            return False
        else:
            # Se houver saldo suficiente, subtrai o valor do saldo.
            self.saldo -= valor
            # Registra a transação no histórico (OBS: erro aqui! Está registrando como depósito).
            self.historico.transacoes.append("depósito de {}".format(valor))  # Deveria ser "saque de"
            # Retorna True indicando que o saque foi realizado com sucesso.
            return True

    # Método para exibir o extrato da conta.
    def extrato(self):
        # Imprime o número da conta e o saldo atual formatado.
        print("Número: {}\nSaldo: {}".format(self.numero, self.saldo))
        # Registra a ação de tirar extrato no histórico.
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    # Método para transferir dinheiro para outra conta.
    def transfere(self, destino, valor):
        # Tenta sacar o valor da conta atual.
        if not self.saca(valor):
            # Se o saque falhar, retorna False.
            return False
        # Se o saque for bem-sucedido, deposita o valor na conta de destino.
        destino.deposita(valor)
        # Registra a transferência no histórico da conta origem.
        self.historico.transacoes.append("transferência de {} para conta {}".format(valor, destino.numero))
        # Retorna True indicando que a transferência foi realizada com sucesso.
        return True

# Define uma classe chamada Historico, que registra as transações de uma conta.
class Historico:
    # Método construtor da classe Historico.
    def __init__(self):
        # Imprime uma mensagem informando que o histórico está sendo inicializado.
        print("Inicializando um histórico")
        # Atributo 'data_abertura' armazena a data e hora atual da criação do histórico.
        self.data_abertura = datetime.datetime.today()
        # Atributo 'transacoes' é uma lista que armazenará as descrições das transações realizadas.
        self.transacoes = []

    # Método para imprimir o histórico de transações.
    def imprime(self):
        # Imprime uma mensagem indicando que o histórico está sendo exibido.
        print("Inicializando uma impressão do histórico")
        # Imprime a data de abertura da conta.
        print("Data de abertura: {}".format(self.data_abertura))
        # Imprime todas as transações registradas.
        print("Transações:")
        for t in self.transacoes:
            # Para cada transação, imprime com um marcador "-".
            print("-", t)

# Abaixo estão exemplos de uso das classes definidas acima.

# Cria um cliente chamado João Oliveira com CPF fictício.
cliente = Cliente('João', 'Oliveira', '1111111111-1')

# Cria uma conta associada ao cliente João, com saldo inicial de 120.0 e limite de 1000.0.
minha_conta = Conta('123-4', cliente, 120.0, 1000.0)

# Imprime o nome do cliente.
print(cliente.nome)

# Imprime o saldo da conta.
print(minha_conta.saldo)

# Imprime o sobrenome do titular da conta (acessando o atributo do objeto Cliente).
print(minha_conta.titular.sobrenome)

# Cria dois clientes diferentes.
cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')

# Cria duas contas associadas aos clientes acima, ambas com saldo inicial de 1000.0.
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)

# Realiza um depósito de 100.0 na conta1.
conta1.deposita(100.0)

# Realiza um saque de 50.0 na conta1.
conta1.saca(50.0)

# Transfere 200.0 da conta1 para a conta2.
conta1.transfere(conta2, 200.0)

# Chama o método extrato da conta1 (mas não imprime porque falta os parênteses).
conta1.extrato  # ERRO: deveria ser `conta1.extrato()`

# Imprime o histórico de transações da conta1.
conta1.historico.imprime()
vars(Cliente)
conta6 = Conta
conta6.numero = 1
