'''
desafio 
'''
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('digite outro valor: ')
linha_1 = f'{primeiro_valor} é maior que {segundo_valor}'
linha_2 = f'{segundo_valor}, é maior que, {primeiro_valor}' 
linha_3 = 'o primeiro valor e o segundo valor são iguais'

if primeiro_valor > segundo_valor:
 print(linha_1)

elif segundo_valor > primeiro_valor:
    print(linha_2)
else :
    print(linha_3)