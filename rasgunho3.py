from os import system
system('cls')

print('*'*80)
print('Adivinhe quaL é o número:'.center(80,'*'))
print('*'*80)

rodada = 1
total_tentativas = 3
NUMERO_SECRETO = 82

while(rodada <= total_tentativas):
    print(f'\nTentativa {rodada:02d} de {total_tentativas:02d}')
    tentativa = input('Tente acertar o número:')
    print('Voce digitou:', tentativa)
    tentativa_int = int(tentativa)
    
    acerto = tentativa_int == NUMERO_SECRETO
    ehmaior = tentativa_int > NUMERO_SECRETO
    ehmenor = tentativa_int < NUMERO_SECRETO
    
    if acerto:
        print('Boa tentativa. ACERTOU!!!!')
        break
    else:
        print('Nao foi dessa vez. ERROU!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto')
    rodada += 1
    
print('Obrigado por participar')
    
    
    
    