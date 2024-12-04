''''
formatação basica de strings 
s - strigs
d - int
f- float

>- Esquerda
< - direita
^ - centro
sinal -+ ou -
Ec.:0>100,.if
Conversion flags - !r !s !a 
'''
variavel ='ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.45153153255151351353:-,.1f}')
print(f'O hexadecima de 1500 é {1500:08X} ')
print(f'{variavel!r}')