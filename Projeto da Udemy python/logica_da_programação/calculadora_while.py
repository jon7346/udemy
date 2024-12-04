while True:
    numero_1 = input('Digite o número: ')
    numero_2 = input('Digite outro número:')
    operador = input('Digite o operador: ')
    
    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except: 
       numeros_validos = None 

    if numeros_validos == None:
       print("um ou mais numeros digitados são inválidos:")
       continue
    
    operadores_logicos_permitidos = '*+-/'
    if operador not in operadores_logicos_permitidos:
       
     print('o operador digitado é inválido')
     continue
  
    if len(operador) > 1:
     print('digite apenas um operador:')
     continue

    elif operador == '+':
     print(num_1_float + num_2_float)
    elif operador == '-':
     print(num_1_float - num_2_float)
    elif operador == "/":
     print(num_1_float / num_2_float)
    elif operador == "*":
     print(num_1_float * num_2_float)


    Sair = input('Quer sair? ').lower().startswith('s')
    if sair is True:
        break