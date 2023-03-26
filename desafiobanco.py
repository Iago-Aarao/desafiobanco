#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

#Deve ser possível depositar valores positivos para a minha
#conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
#dessa forma não precisamos nos preocupar em identificar qual
#é o número da agência e conta bancária. Todos os depósitos
#devem ser armazenados em uma variável e exibidos na
#operação de extrato.

#O sistema deve permitir realizar 3 saques diários com limite
#máximo de R$ 500,00 por saque. Caso o usuário não tenha
#saldo em conta, o sistema deve exibir uma mensagem
#informando que não será possível sacar o dinheiro por falta de
#saldo. Todos os saques devem ser armazenados em uma
#variável e exibidos na operação de extrato.

#Essa operação deve listar todos os depósitos e saques
#realizados na conta. No fim da listagem deve ser exibido o
#saldo atual da conta. Se o extrato estiver em branco, exibir a
#mensagem: Não foram realizadas movimentações.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
#exemplo:
#1500.45 = R$ 1500.45



menu = """" 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
valor_limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor para o depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(valor_deposito)

        else:
            print("A operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > valor_limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha! Saldo insuficiente para saque.")
        
        elif excedeu_limite:
            print("Falha! O limite de R$500.00 de saque foi atingido.")
        
        elif excedeu_saques:
            print("Falha! O limite de 3 saques foi atingido.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        
        else:
            print("Falha! O valor informado é inválido.")
    
    elif opcao == "e":
        print("################Extrato################")
        print("Não há movimentações realizadas" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#######################################")
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida! Favor digitar uma opção válida do menu.")