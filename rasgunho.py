print('*'*80)
print('Adivinhe qual é o número?'.center(80,'*'))
print('*'*80)

NUMERO_SECRETO = 83
tentativa = input('Tente acertar o número:')
print('Voce digitou: ', tentativa)

try:
    tentativa_int = int(tentativa)
except ValueError:
    print('Valor inválido. Informe um número inteiro')
    exit()
except Exception as e:
    print(f'ERRO: {e}')
    exit()
else:
    print('\n entrou no ELSE')
finally:
    print('\n entrou no FINALLY')
if (NUMERO_SECRETO == tentativa_int):
    print('Boa tentativa. ACERTOU!')
else:
    print('Nao foi dessa vez. ERROU!')
print('GAME OLVER!')
print('OLbrigado por participar')

    

