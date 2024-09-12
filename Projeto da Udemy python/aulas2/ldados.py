'''
nome = 'luiz'
noutra_variavel=nome
nome='joão'
print(nome) 
print(noutra_variavel)
'''
"""
cuidados com dados mutaveis 
= copiado o valor (imutaveis)
= aponta para o mesmo id ou valor na memoria (mutavel)
"""
lista_a =['luiz', 'maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)