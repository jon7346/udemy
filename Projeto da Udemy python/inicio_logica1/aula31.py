v1 = 'a'
v2 = 'b'

print(id(v1))
print(id(v2))

"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None

#ou seja se a variavel 'condicao' for True a variavel passaou_no_if se torna True ao inveis de None 
if condicao:
    passou_no_if = True
    print('Faça algo')

else:
    print('Não faça algo')


print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

