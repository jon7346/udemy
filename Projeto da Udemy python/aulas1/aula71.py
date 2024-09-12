frase = 'quero me tornar um programador'
qtd_mais_vezes= 0
letra_apareceu_mais_vezes = 0 
i = 0 
while i < len(frase): 
 i += 1
 letra = frase[i]
 if letra == ' ':
     continue 
 qtd = frase.count(letra)
 if qtd_mais_vezes < qtd:
  qtd_mais_vezes = qtd


    

