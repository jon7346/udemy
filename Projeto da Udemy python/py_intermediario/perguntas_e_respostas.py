
pergunta = {
 {
     'pergunta': 'Quanto é 2+2?',
     'opções': ['1','2','3','4','5'],
     'Resposta': '4',
 },
{
     'pergunta': 'Quanto é 5*5?',
     'opções': ['25', '55', '10','51'],
     'Resposta': '25 ',
},
{
    'pergunta': '',
    "opções":['4','5','2','1'],
    "Resposta": '5',
},


}

qtd_acertos = 0 
for pergunta in perguntas:
    print('pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['opções']

    