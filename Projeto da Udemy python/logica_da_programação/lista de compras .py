#lista de compras usando listas
lista = []
frase =(f'(i)inserir, (a)apagar, (l)listar ' )
client=''
import os

while client != 'sair':
 print(frase)
 client = input('insira um comando: ')  
 if client == 'i' :
     os.system('clear')
     novo_item = input('insira o novo item: ')
     lista.append(novo_item)
     continue
 if client == 'a' :
    os.system('clear')
    delete = int(input('insira o indice do numero para apagar: '))
    lista.pop(delete) 
    continue
 if client == 'l' :
    os.system('clear')
    print(lista)
    continue
 else:
  print('por favor escreva um dos comando listados corretamente')
  continue