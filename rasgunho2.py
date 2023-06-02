from os import system
system('cls')

print('*'*80)
print('Adivinhe qual é o número?'.center(80,'*'))
print('*'*80)
numero_secreto= 83
rodada = 0
total_de_tentativas =3
acerto = False

while (rodada <= total_de_tentativas):
    rodada += 1
    tentativa = input('Tente acertar o número:')
    print('Voce digitou:' ,tentativa)
    print(f'\nTentativa {rodada:02d} de {total_de_tentativas:02d}')
    
    try:
        tentativa_int = int(tentativa)
    except ValueError:
        print('Valor inválido. Informe um número inteiro')
        break
    except Exception as e:
        print(f'ERRO: {e}')
        break
    else:
        pass
    finally:
        pass
    
    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto
    
    if acerto:
        print('Boa tentativa. ACERTOU!!!')
        break
    else:
        print('Nao foi dessa vez.ERROU!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto. ')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto.')
            
if not acerto:
    print('GAME OVER!')
    print('Obrigado por participar')
           
    
        
    
