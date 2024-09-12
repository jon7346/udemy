nome = ' luiz otavio '
altura =  '1.80'
peso = 95
imc = ... # IMC = peso / (altura * altura)

# resuldado
# luiz otavio tem 1.80 de altura 
# pesa 95 quilos e seu imc é 
#29 .320...


nome =  str(input('insira o seu nome:'))
altura =  float(input('insira a sua altura:'))
peso =  float(input('inira o seu peso:'))
imc = peso // altura ** 2

print(nome,'tem', altura, 'de altura'  )
print('pesa', peso, 'quilos e seu imc é ')
print(imc)