menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = []
num_saques = 0
espacador = 50
LIMITE_SAQUES = 3
SEP = ' | '

while True:
    print(' Menu '.center(espacador, '#'))
    opcao = input(menu)

    if opcao == 'd':
        print(' Depósito '.center(espacador, '#'), '\n\n')
        deposito = float(input('Digite o valor que deseja depositar: '))
        if deposito > 0:
            saldo += deposito
            extrato.append(f'Depósito: || R$ {deposito:.2f}')
            print('\nDepósito realizado com sucesso.\n\n'
                  f'Saldo atual: R$ {saldo:.2f}.\n\n')
        else:
            print('O valor não é válido, digite um número maior que 0!\n')

    elif opcao == 's':
        print(' Saque '.center(espacador, '#'), '\n\n')
        
        if saldo == 0:
            print('Você não tem nenhum saldo.\n\n')
            continue

        if num_saques >= LIMITE_SAQUES:
            print('Você atingiu o limite de saques diários '
                  f'atual que é de {LIMITE_SAQUES} saques.\n\n')
            continue

        valor_saque = float(input('Digite o valor que deseja sacar: '))
        
        if valor_saque > limite:
            print(f'Valor do saque maior que o permitido, insira um valor menor que {limite}.\n')
        elif valor_saque <= 0:
            print('Valor inválido, digite um número maior que 0!\n')
        elif valor_saque > saldo:
            print('\nO valor do saque é maior que o saldo atual, insira um valor menor ou igual a R$ {saldo:.2f}\n')
        else:
            saldo -= valor_saque
            num_saques += 1
            extrato.append(f'Saque: || R$ {valor_saque:.2f}')
            print('\n\nSaque realizado com sucesso.\n'
                  f'Saldo atual é de R$ {saldo:.2f}\n\n')

    elif opcao == 'e':
        print(' Extrato '.center(espacador, '#'), '\n\n')

        if extrato:
            print('\nAqui estão todas as suas operações:\n')

            for operacao in extrato:
                tipo, valor = operacao.split('||')
                print(tipo.center(15), valor)

            print(f'\nSaldo atual: R$ {saldo:.2f}\n\n')

        else:
            print('Não foram realizadas movimentações.\n\n')

    elif opcao == 'q':
        print('Sair...')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
