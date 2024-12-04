import os
palavra_secreta = "perfume"
letras_acertadas= ""
tentativas = 0 
os.system('clear')  
while True :
    letra_digitada = input("insira uma letra:")
    tentativas += 1 
    
    if len(letra_digitada) > 1 :
        print("digite apenas uma letra pfrv")
        continue
    
           
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''     
   
    for letras in palavra_secreta:
      
        if letras in letras_acertadas:
            palavra_formada += letras
        else :
            palavra_formada += "*"
   
    print(palavra_formada)    

    if palavra_formada == palavra_secreta:
     print('VOCê GANHOU! PARABÉNS')
     print('palavra formada:',palavra_formada)
     print('tentativas',tentativas)
     letras_acertadas= ""
     tentativas = 0 
   