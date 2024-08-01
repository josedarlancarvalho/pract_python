Projeto: Sistema de Gestão de Contas Bancárias
Requisitos:
Crie uma classe ContaBancaria com os seguintes atributos:

numero (número da conta)
titular (nome do titular)
saldo (saldo da conta, inicializado com zero)
limite (limite de saque da conta, inicializado com um valor padrão, ex: 500)

A classe ContaBancaria deve ter os seguintes métodos:

depositar(valor): Adiciona o valor ao saldo da conta.
sacar(valor): Subtrai o valor do saldo da conta, considerando o limite disponível.
exibir_saldo(): Exibe o saldo atual da conta.

Crie uma classe Banco que gerencia várias contas bancárias com os seguintes métodos:

adicionar_conta(conta): Adiciona uma nova conta ao banco.
remover_conta(numero): Remove uma conta do banco pelo número da conta.
listar_contas(): Lista todas as contas registradas no banco.


Passos:
Defina as classes e métodos conforme descrito.
Crie algumas instâncias de ContaBancaria.
Adicione essas contas ao Banco.
Realize operações de depósito, saque e exibição de saldo para testar o funcionamento do sistema.