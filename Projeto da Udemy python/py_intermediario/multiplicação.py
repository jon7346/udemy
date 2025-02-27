usuario = int(input('insira o primeiro numero:'))
usuario2 = int(input('insira o segundo numero: '))

#multiplicação
def multiplicação(*args) :
 total = 0 
 total = usuario * usuario2  

 return total

total = multiplicação(usuario, usuario2)
print(total)
#par ou impar 
def verificação(*args):
 
 for args in args :
  numero = 0 
  str(ord) = 0 + 1 
  numero = args(ord)
 if numero % 2 == 0 : 
  return 'o numero é par'
 else :
  return ' o numero é impar'

verifi = verificação(total)
print(verifi) 


 