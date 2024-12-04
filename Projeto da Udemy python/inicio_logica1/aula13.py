nome =  str(input('insira o seu nome:'))
altura =  float(input('insira a sua altura:'))
peso =  float(input('inira o seu peso:'))
imc = peso // altura ** 2

linha_1 = f'{nome} tem {altura:2f} de altura'
linha_2 = f'pesa{peso} quilos e seu imc é'
linha_3 = f'{imc}'

print(linha_1)
print(linha_2)
print(linha_3)

# resuldado
# luiz otavio tem 1.80 de altura 
# pesa 95 quilos e seu imc é 
#29 .320...

