lista_a = [1,2,3]
lsita_b = [4,5,6]
lista_c = lista_a + lsita_b
#não é possivel adicionar o extend em outras variaveis pois ele altera a lista_a em si
lista_a.extend(lista_b)
print(lista_a)